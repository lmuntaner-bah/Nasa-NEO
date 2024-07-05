from s3_download import download_csv_from_s3
from pg_load import upload_df_to_postgres
from dotenv import load_dotenv
from loguru import logger
import pandas as pd
import sys
import os

try:
    load_dotenv()
    project_path = os.getenv('PROJECT_PATH')
    
    if project_path not in sys.path:
        sys.path.append(project_path)
    
    from sql_query import get_postgres_conn
    from models import NeoJobParams
    
    logger.info('Imports successful')
except Exception as e:
    logger.error(f'Unexpected error in imports: {e}')


def main(params: NeoJobParams):
    download_csv_from_s3(params.bucket_name, params.file_name, params.local_dir)
    
    conn = get_postgres_conn()
    
    df = pd.read_csv(f'../data/temp_processed/{params.file_name}')
    
    table_df_pairs = [
        ("public.neo_dashboard", df)
    ]
    
    upload_df_to_postgres(conn, table_df_pairs)

if __name__ == '__main__':
    main(NeoJobParams())