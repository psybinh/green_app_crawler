import boto3
import configparser

CONFIG_FILE = 'aws.config'

class S3Uploader:
    
    def __init__(self):
        self.config = self.load_config()
        s3 = boto3.resource('s3', 
                    aws_access_key_id=self.config['credentials']['aws_access_key_id'], 
                    aws_secret_access_key=self.config['credentials']['aws_secret_access_key'])
        self.green_app_bucket = s3.Bucket('green-app-crawler')
    
    def load_config(cls):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        return config
    
    def upload(cls, file_url, filename):
        cls.green_app_bucket.upload_file(file_url, Key=filename)