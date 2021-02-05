#built-in libraries
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


#return items from table with size in range
def select_items(table, min_size, max_size):
    fe = Attr('size').between(min_size, max_size)
    response = table.scan(
      FilterExpression=fe
    )
    if (response['Count'] == 0):
        return 'None'
    else:
        items = response['Items']
        return items

def lambda_handler(event, context):
    min_size = int(event['min'])
    max_size = int(event['max'])
    
    #init dynamodb table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    
    items = select_items(table, min_size, max_size)
 
    return {
        "statusCode": 200,
        "body": items
      }