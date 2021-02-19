#built-in libraries
import json
import boto3
from boto3.dynamodb.conditions import Key


#return items from table with size in range
def select_items(table, url):
    response = table.query(
      KeyConditionExpression=Key('url').eq(url),
      ProjectionExpression='#filter_type, upload_time, size',
      ExpressionAttributeNames={
        '#filter_type': 'type'
      }
    )
    if (response['Count'] == 0):
        return 'None'
    else:
        items = response['Items']
        return items


def lambda_handler(event, context):
    url = event['url']
   
    #init dynamodb table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    
    items = select_items(table, url)
 
    return {
        "statusCode": 200,
        "body": items
      }