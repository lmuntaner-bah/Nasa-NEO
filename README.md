# Neo Pipeline Project

## Overview

This project is designed to process Near Earth Objects (NEO) data, leveraging a pipeline that extracts data, transforms it, and loads it into a PostgreSQL database. It also includes functionality for uploading processed data to AWS S3.

## Structure

The project is organized into several key directories:

- `data/`: Contains raw data files and temporary processed data.
- `database/scripts/`: SQL scripts for creating tables in MSSQL and PostgreSQL.
- `extract/`: Python modules for data extraction and initial processing.
- `loading/`: Python modules for loading data into PostgreSQL and downloading from S3.
- `notebooks/`: Jupyter notebooks for testing connections, exploratory data analysis (EDA), and more.

## Key Components

- **Data Extraction and Processing**: Implemented in the `extract` directory, it includes modules like [`aws_s3.py`](extract/aws_s3.py) for AWS S3 interactions, [`models.py`](extract/models.py) for data models, [`pipeline.py`](extract/pipeline.py) for orchestrating the extraction and processing pipeline, and [`sql_query.py`](extract/sql_query.py) for database interactions.

    * There is a AWS lambda function that will execute once the data is loaded into the interm bucket. This lambda function will transform the dates into the correct formate and handle some NaN values in the short_name column.

- **Data Loading**: Located in the `loading` directory, it features scripts like [`load_pipeline.py`](loading/load_pipeline.py) for the main loading pipeline, [`pg_load.py`](loading/pg_load.py) for loading data into PostgreSQL, and [`s3_download.py`](loading/s3_download.py) for downloading data from S3.

- **Database Scripts**: SQL scripts for database setup are found in `database/scripts/`, including [`create_tables_MSSQL.sql`](database/scripts/create_tables_MSSQL.sql) and [`create_tables_postgres.sql`](database/scripts/create_tables_postgres.sql).

- **Jupyter Notebooks**: For testing and EDA, notebooks are available under the `notebooks/` directory, including connection tests for MSSQL and PostgreSQL, an EDA notebook, and more.

## Setup and Usage

1. **Environment Setup**: Ensure Python 3.11.9 is installed along with required packages listed in the project dependencies (not provided here).

2. **Database Setup**: Run the SQL scripts in `database/scripts/` to set up your database tables in either MSSQL or PostgreSQL.

3. **Data Processing and Loading**:
   - Run the pipeline script in [`extract/pipeline.py`](extract/pipeline.py) to extract and process the data.
   - Use the loading script in [`loading/load_pipeline.py`](loading/load_pipeline.py) to load the processed data into the database and/or upload to AWS S3.

4. **Exploratory Data Analysis (EDA)**: Explore the `notebooks/` directory for Jupyter notebooks that can be used for EDA and testing various components of the project.

## Configuration

- Configure your database and AWS credentials in a `.env` file (refer to the provided `.gitignore` for exclusion rules).