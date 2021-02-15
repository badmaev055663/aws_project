#built-in libraries
import json
import boto3

#find item in table and return if exists
def get_img_item(table, url, type):
    response = table.get_item(
      Key = {
         'url': url,
         'type': type
      },
      ProjectionExpression='img_id'
    )
    if 'Item' in response:
      return response['Item']
    else:
      return None

#delete record from table
def delete_from_table(table, url, type):
    response = table.delete_item(
      Key = {
         'url': url,
         'type': type
      },
      ReturnValues='NONE'
    )
    
def delete_from_bucket(file):
    s3 = boto3.client('s3')
    response = s3.delete_object(
        Bucket='img-process-project',
        Key=file
    )
  
    
def lambda_handler(event, context):
    #url of source and type of filter
    url = event['url']
    type = event['type']
    
    #init dynamodb table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    
    item = get_img_item(table, url, type)
    body = "no"
    if (item != None):
        delete_from_table(table, url, type);
        file = 'images/' + item['img_id'] + '.jpg'
        delete_from_bucket(file)
        body = "yes"
  
    return {
        "statusCode": 200,
        "body": body
      }