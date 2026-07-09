# End_to_end_analytics_engineering_pipeline

The goal of this project was to design and implement an end-to-end analytics engineering pipeline by:

1. Ingesting raw e-commerce purchase data into a MySQL database using automated Python ETL scripts.
2. Building a layered data architecture to improve data quality, manitainability, and scalability.
3. Cleaning, testing, and transforming the data using dbt. 
4. Modeling key business metrics for customer analytics, product performance, and session analytics.
5. Visualizing insights in Tableau Public through interactive dashboards.
6. Orchestrating data workflows with Airflow to automate data ingestion and transformation processes.

The objective is to transform raw e-commerce transaction data into a scalable analytics-ready data model that supports business reporting and decision-making.


### Tech Stack
* Python (Data Ingestion & Processing)
* MySQL (Data Warehouse)
* Docker & Docker Compose (Local Infrastructure)
* dbt (Data Transformation & Testing)
* Apache Airflow (Workflow Orchestration)
* Tableau Public (Data Visualization)


### Data

The original dataset contained 7 months of purchase transactions (~50GB+ raw CSV). For local development purposes, a representative subset was loaded into MySQL.


During exploratory analysis, I observed that some product_id values map to multiple category_code values across months (for example, the same product_id changed from apparel categories in Oct to kitchen categories in Dec).



### High-Level Architecture


### Business Use Cases
