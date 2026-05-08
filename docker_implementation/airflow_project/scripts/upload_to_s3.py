import boto3

s3 = boto3.client(
    's3',
    #aws_access_key_id='your key id',
    #aws_secret_access_key='your secret access',
    #region_name='your region'#
)

file_name = "/opt/airflow/data/processed/cleaned_api_data.csv"
bucket_name = #"usaid-data-pipeline-bucket"
object_name = #"cleaned_api_data.csv"

s3.upload_file(file_name, bucket_name, object_name)

print("File uploaded successfully!")
