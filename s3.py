import boto3

s3 = boto3.client('s3')
bucket_name = 'my-web-app-hero-bucket'

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
)

print(f"S3 Bucket created: {bucket_name}")

