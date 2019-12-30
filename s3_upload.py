import boto3
import hashlib

s3_bucket_name = "BUCKET-NAME"
file_name = "FILE-NAME"

with open(file_name, "rb") as file:
    raw_file = file.read()

    md5_hash = hashlib.md5(raw_file)
    file_hash = md5_hash.hexdigest()

    print("Calculated File Hash:", file_hash)
    
    s3 = boto3.client('s3')
    response = s3.put_object(ACL='bucket-owner-full-control',
                    Body=raw_file, 
                    Bucket=s3_bucket_name,
                    Key=file_name)

    s3_file_hash = response['ETag'].replace('"', '')

    print("S3 Calculated File Hash:", s3_file_hash)
