from kfp.dsl import component, Input, Output, Dataset
import boto3 


import pandas as pd 




def preprocess(

):
    from src.utils.env_loader import  load_environment
    import boto3
    from botocore.client import Config
    import os
    import pandas as pd
    load_environment()

    s3_uri = os.environ.get("RAW_DATA_PATH")
    print(s3_uri)
    df = pd.read_csv(
        s3_uri,
        storage_options={
            "key": os.getenv("MINIO_SECRET_ACCESS_KEY_ID"),
            "secret": os.getenv("MINIO_SECRET_ACCESS_KEY_PASSWORD"),
            "client_kwargs": {
                "endpoint_url": os.getenv("MINIO_ENDPOINT")  # works for MinIO, ignored for AWS
            }
        }
)

    print(df.describe())


if __name__ =="__main__":
    preprocess()



     
    