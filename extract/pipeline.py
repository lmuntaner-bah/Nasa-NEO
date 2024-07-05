from sql_query import get_postgres_conn, get_query_result, build_query
from models import NeoJobParams, NeoDF, validate_dataframe
from aws_s3 import upload_df_to_s3

def main(params: NeoJobParams):
    db_table = "public.near_earth_objects"
    
    df = get_query_result(
        query_str=build_query(params, db_table), 
        conn=get_postgres_conn()
    )
    print(df.head(15))
    
    validation_result = validate_dataframe(df, NeoDF)
    
    if validation_result:
        print("DataFrame validations passed. Uploaded to S3...")
        upload_df_to_s3(df, params.bucket_name, params.file_name)
    else:
        print("DataFrame validation failed.")


if __name__ == '__main__':
    main(NeoJobParams())