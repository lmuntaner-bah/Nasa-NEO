from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from dotenv import load_dotenv
from loguru import logger
from io import StringIO
import boto3
import os

# Load environment variables
load_dotenv()

def upload_df_to_s3(df, bucket_name, file_name):
    """
    Uploads a DataFrame to an S3 bucket as a CSV file.
    
    Parameters:
    - df: The DataFrame to upload.
    - bucket_name: The name of the S3 bucket.
    - file_name: The name of the file to create in the S3 bucket.
    
    Returns:
    - response: The response from the S3 service.
    """
    try:
        logger.info(f"Writing data to S3 {bucket_name}")
        
        # Convert DataFrame to CSV format without an index
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        
        # Create an S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        
        # Upload the CSV file
        response = s3_client.put_object(
            Bucket=bucket_name,
            Key="interm/" + file_name, # Include the desired path within the bucket as part of the key
            Body=csv_buffer.getvalue()
        )
        
        return response
    except NoCredentialsError:
        logger.error("No AWS credentials found.")
        return "No AWS credentials found."
    except PartialCredentialsError:
        logger.error("Incomplete credentials AWS credentials found.")
        return "Incomplete credentials found."
    except ClientError as e:
        logger.error(f"Client error occurred: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise