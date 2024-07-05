from psycopg2 import OperationalError
from sqlalchemy import create_engine
from models import NeoJobParams
from dotenv import load_dotenv
from loguru import logger
import pandas as pd
import psycopg2
import time
import os

# Load environment variables from .env file
load_dotenv()

def build_query(params: NeoJobParams, db_table: str):
    """
    Build and return a SQL query string based on the given parameters and database table.
    
    Args:
        params (NeoJobParams): An instance of the NeoJobParams class containing the parameters for the query.
        db_table (str): The name of the database table to query.
    
    Returns:
        str: The SQL query string.
    """
    return f"""
    SELECT
        id,
        name AS {params.alias_name},
        name_limited AS {params.alias_limited_name},
        absolute_magnitude_h,
        is_potentially_hazardous_asteroid,
        is_sentry_object,
        kilometers_estimated_diameter_min,
        kilometers_estimated_diameter_max,
        perihelion_distance,
        aphelion_distance,
        first_observation_date AS {params.alias_first_date},
        last_observation_date AS {params.alias_last_date},
        orbit_class_description
    FROM
        {db_table}
    WHERE
        is_potentially_hazardous_asteroid = {params.haz_asteroid};
    """

def get_mssql_conn():
    """
    Creates a SQL Server database engine.
    
    Returns:
    Engine
    """
    try:
        # Get environment variables
        db_server = os.getenv('DB_SERVER')
        db_name = os.getenv('DB_NAME')
        
        # Create SQLAlchemy engine with Windows Authentication for localhost
        connection_string = f"mssql+pyodbc://{db_server}/{db_name}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
        engine = create_engine(connection_string)
        
        conn = engine.connect()
        
        return conn
    except Exception as e:
        print(f'Creating SQL engine failed: {e}')

def get_postgres_conn():
    connection = None
    
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dbname=os.getenv("DB_NAME")
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    
    return connection

def get_query_result(query_str, conn):
    try:
        # Start measuring time
        start_time = time.time()
        
        # Execute query and fetch results
        logger.info(f'Running query: {query_str}')
        df = pd.read_sql_query(query_str, conn)
        
        # Log time taken for query execution and data loading
        elapsed_time = time.time() - start_time
        logger.info(f'Query executed and data loaded in {elapsed_time:.2f} seconds')
        
        return df
    except Exception as e:
        logger.error(f'Error running query: {e}')
        raise