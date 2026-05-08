import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id='AKIA3TF4LH5RLW4FPUIT',
    aws_secret_access_key='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',
    region_name='eu-north-1'
)

file_name = "/opt/airflow/data/processed/cleaned_api_data.csv"
bucket_name = "usaid-data-pipeline-bucket"
object_name = "cleaned_api_data.csv"

s3.upload_file(file_name, bucket_name, object_name)

print("File uploaded successfully!")