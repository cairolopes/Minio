import logging
import sys
from minioConn import MinioSDK

minio = MinioSDK()
minio.mk_bucket(minio.minioClient(), "buckerest")
