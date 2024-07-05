from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from dotenv import load_dotenv
from loguru import logger
import boto3
import os

load_dotenv()

def download_csv_from_s3(bucket_name, file_name, local_dir):
    """
    Downloads a CSV file from an S3 bucket to a local directory.
    
    Parameters:
    - bucket_name: The name of the S3 bucket.
    - file_name: The name of the file to download from the S3 bucket.
    - local_dir: The local directory to save the downloaded file.
    
    Returns:
    - str: A message indicating the result of the download operation.
    """
    try:
        logger.info(f"Downloading {file_name} from S3 bucket {bucket_name} to {local_dir}")
        
        # Create an S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        
        # Ensure the local directory exists
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        
        # Define the local file path
        local_file_path = os.path.join(local_dir, file_name)
        
        # Download the file
        s3_client.download_file(bucket_name, "processed/" + file_name, local_file_path)
        
        logger.info(f"File downloaded successfully: {local_file_path}")
        return f"File downloaded successfully: {local_file_path}"
    except NoCredentialsError:
        logger.error("No AWS credentials found.")
        return "No AWS credentials found."
    except PartialCredentialsError:
        logger.error("Incomplete AWS credentials found.")
        return "Incomplete credentials found."
    except ClientError as e:
        logger.error(f"Client error occurred: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise