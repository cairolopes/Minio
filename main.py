import logging
import sys
import os
from minioConn import MinioSDK

minio = MinioSDK()
bucket = "kaggle"
directory = "data/transaction_dataset.csv"
file_name = "transaction_dataset.csv"

# minio.mk_bucket(minio.minioClient(), "buckerest")

minio.put_thing(
    minio.minioClient(),
    bucket,
    file_name,
    directory
)

