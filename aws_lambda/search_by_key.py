#built-in libraries
import json
import boto3
from boto3.dynamodb.conditions import Key


#return items from table with size in range
def select_items(table, key, body):
    if (key == 'url'):
        fe = Key('url').eq(body)
    else:
        fe = Key('type').eq(body)
    response = table.scan(
      FilterExpression=fe
    )
    if (response['Count'] == 0):
        return 'None'
    else:
        items = response['Items']
        return items

def lambda_handler(event, context):
    key = event['key']
    body = event['body']
    #init dynamodb table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    
    items = select_items(table, key, body)
 
    return {
        "statusCode": 200,
        "body": items
      }