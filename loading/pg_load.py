from psycopg2 import OperationalError
from loguru import logger

def upload_df_to_postgres(conn, table_df_pairs):
    """
    Uploads a DataFrame to a PostgreSQL table using psycopg2.
    
    Parameters:
    - conn: database connection object
    - table_df_pairs: list of tuples where each tuple contains the table name and the DataFrame to upload
    
    Returns:
    None
    """
    
    try:
        for table_name, df in table_df_pairs:
            with conn.cursor() as cursor:
                values = [tuple(row) for row in df.to_numpy()]
                
                columns = ','.join(list(df.columns))
                
                placeholders = ','.join(['%s'] * len(df.columns))
                
                sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                
                cursor.executemany(sql_query, values)
            
            conn.commit()
            logger.info(f"Data uploaded to {table_name} in PostgreSQL.")
    except OperationalError as e:
        logger.error(f"Error uploading data to PostgreSQL: {e}")
    finally:
        conn.close()