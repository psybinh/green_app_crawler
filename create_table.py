import boto3
from dynamo_lib import DynamoDB

if __name__ == '__main__':
    dynamodb = DynamoDB().get_dynamodb()
    dynamodb.create_table(TableName= 'green_app_data', 
                          KeySchema= [
                              {
                                  'AttributeName': 'hashed_id',
                                  'KeyType': 'HASH'
                              },
                          ], 
                          AttributeDefinitions = [
                              {
                                  'AttributeName': 'hashed_id',
                                  'AttributeType': 'S'
                              }
                          ], 
                          BillingMode='PROVISIONED',
                          ProvisionedThroughput={
                              'ReadCapacityUnits': 10,
                              'WriteCapacityUnits': 10
                          }
                         )