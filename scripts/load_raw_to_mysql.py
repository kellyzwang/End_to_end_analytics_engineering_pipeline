import pandas as pd
from pathlib import Path
import mysql.connector

# 1. Map Pandas data types to MySQL data types
def map_dtype_to_mysql(col_name, dtype):
    # Check for string/object fields
    if str(dtype) == "object":
        return f"`{col_name}` TEXT"
    # Check for integer fields
    elif "int" in str(dtype):
        return f"`{col_name}` BIGINT"
    # Check for decimal/float fields
    elif "float" in str(dtype):
        return f"`{col_name}` DOUBLE"
    # Check for datetime fields
    elif "datetime" in str(dtype):
        return f"`{col_name}` DATETIME"
    # Fallback default
    else:
        return f"`{col_name}` TEXT"


# 2. Establish connection
conn = mysql.connector.connect(
    host="localhost", port=3306, user="root", password="password", database="ecommerce"
)
cursor = conn.cursor()


DATA_DIR = Path("data/samples")


# Find the first file to dynamically generate the table structure
sample_files = list(DATA_DIR.glob("*_sample.csv"))


if sample_files:
    first_file = sample_files[0]
    print(f"Analyzing {first_file.name} to generate table schema...")


    # Read just the first 5 rows to figure out the column names and types
    sample_df = pd.read_csv(first_file, nrows=5)


    # Convert the columns into MySQL-friendly definitions
    sql_columns = [
        map_dtype_to_mysql(col, dtype)
        for col, dtype in zip(sample_df.columns, sample_df.dtypes)
    ]

    # Join definitions with commas
    columns_string = ", ".join(sql_columns)

    # Build and execute the dynamic CREATE TABLE query
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS raw_purchase_events (
        {columns_string}
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Table 'raw_purchase_events' successfully created.")

# 3. Process and load files using chunks
for csv_file in DATA_DIR.glob("*_sample.csv"):

    print(f"Loading {csv_file.name}")

    # Use chunksize to keep memory usage low
    df_chunks = pd.read_csv(csv_file, chunksize=100_000)

    for chunk in df_chunks:
        # Dynamically build your INSERT statement from the CSV headers
        columns = ", ".join(chunk.columns)
        placeholders = ", ".join(["%s"] * len(chunk.columns))
        query = f"INSERT INTO raw_purchase_events ({columns}) VALUES ({placeholders})"

        # Convert your NaN values to None so MySQL registers them as NULL
        chunk = chunk.astype(object).where(pd.notnull(chunk), None)

        # Convert the DataFrame chunk rows into a list of tuples
        data_tuples = [tuple(x) for x in chunk.to_numpy()]

        # Efficient native bulk insert
        cursor.executemany(query, data_tuples)

        # Commit each chunk to save progress and keep memory free
        conn.commit()

cursor.close()
conn.close()
print("Done!")