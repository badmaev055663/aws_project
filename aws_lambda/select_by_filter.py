#built-in libraries
import json
import boto3
from boto3.dynamodb.conditions import Attr

#return items from table by date 
def select_items(table, type):
    response = table.scan(
      FilterExpression= Attr('type').eq(type),
      ProjectionExpression='#src_url, upload_time, size',
      ExpressionAttributeNames={
        '#src_url': 'url'
      }
    )
    if (response['Count'] == 0):
        return 'None'
    else:
        items = response['Items']
        return items


def lambda_handler(event, context):
    
    filter = event['type']
    
    #init dynamodb table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    
    items = select_items(table, filter)
 
    return {
        "statusCode": 200,
        "body": items
      }