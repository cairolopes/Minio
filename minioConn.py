import logging
import sys

from minio import Minio 
from minio.error import S3Error

class MinioSDK:
    
    def __init__ (self):

        self.HOST = 'localhost:9000'
        self.access_key = 'admin'
        self.secret_key = 'password'
        self.region = 'br-northeast'


    def minioClient(self):
        return Minio(
            self.HOST,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False,
            region=self.region
        )

    def mk_bucket(self, client, bucket_name: str):

        # Make new_bucket if not exist.
        found = client.bucket_exists(bucket_name)

        if not found:
            try:
                client.make_bucket(bucket_name)
            except S3Error as exc:
                print("".join(['ERROR OCCURRED.', str(exc)]))
        else:
            print('Bucket {} already exists'.format(bucket_name))