import boto3
import configparser

CONFIG_FILE = 'aws.config'

class DynamoDB:
    
    def __init__(self):
        self.config = self.load_config()
        self.dynamodb = boto3.resource('dynamodb',
                            aws_access_key_id=self.config['credentials']['aws_access_key_id'],
                            aws_secret_access_key=self.config['credentials']['aws_secret_access_key'],
                            region_name="ap-southeast-1")
        
    def get_dynamodb(cls):
        return cls.dynamodb
    
    def load_config(cls):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        return config