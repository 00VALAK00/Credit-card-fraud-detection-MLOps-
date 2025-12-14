from storage.base_storage import BaseStorageService
from utils.env_loader import load_environment
from minio import Minio
import os 
import pickle
from typing_extensions import Literal
import logging


class MinioStorageService(BaseStorageService):

    def __init__(self):
        super().__init__()
        load_environment() # load the environments
        self.bucket = os.environ.get("BUCKET_NAME")
        self.endpoint = os.environ.get("MINIO_ENDPOINT")
        self.access_key = os.environ.get("MINIO_SECRET_ACCESS_KEY_ID")
        self.secret_key = os.environ.get("MINIO_SECRET_ACCESS_KEY_PASSWORD")

        self.client = Minio(
            endpoint= self.endpoint,
            access_key= self.access_key,
            secret_key=self.secret_key,
            secure=False
        )

    def save_artifact(self, artifact, artifact_name):
        return self.client.fput_object(bucket_name=self.bucket,
                                    object_name=f"model/{artifact_name}", 
                                    file_path=pickle.dumps(artifact))


    def retrieve_artifact(self, artifact_name):
        if artifact_name not in self.client.list_objects(bucket_name=self.bucket,recursive=True):
            logging.error(f"Artifact {artifact_name} is not within the specified bucket {self.bucket}")

        else:    
            object = self.client.fget_object(bucket_name=self.bucket,
                                       object_name=artifact_name,
                                       file_path=f"model/")
            return pickle.loads(object)
        
    def clear_storage(self, option: Literal["data","model"]):
        objects = self.client.list_objects(bucket_name=self.bucket, prefix=f"{option}/", recursive=True)
        for obj in objects:
            logging.info(f"Object {obj.object_name} has been successfuly deleted")
            self.client.remove_object(self.bucket, obj.object_name)

