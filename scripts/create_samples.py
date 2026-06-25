import pandas as pd
from pathlib import Path


DATA_DIR = Path("data")
OUTPUT_DIR = DATA_DIR / "samples"

OUTPUT_DIR.mkdir(exist_ok=True)


# Keep about 1% of rows
SAMPLE_FRAC = 0.01

# Number of rows to process at a time
CHUNK_SIZE = 500_000



for csv_file in DATA_DIR.glob("*.csv"):
    print(f"\nProcessing {csv_file.name}")

    sampled_chunks = []

    df = pd.read_csv(csv_file, chunksize=CHUNK_SIZE)

    for chunk in df:
        sampled_chunk = chunk.sample(
            frac=SAMPLE_FRAC,
            random_state=0
        )

        sampled_chunks.append(sampled_chunk)

    sample_df = pd.concat(sampled_chunks)

    output_file = OUTPUT_DIR / f"{csv_file.stem}_sample.csv"

    sample_df.to_csv(output_file, index=False)

    print(
        f"Saved {len(sample_df):,} rows to "
        f"{output_file.name}"
    )

print("\nDone!")

