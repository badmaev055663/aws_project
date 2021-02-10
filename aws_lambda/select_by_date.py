#built-in libraries
import json
import boto3
from boto3.dynamodb.conditions import Attr
from datetime import datetime, date, time, timedelta


#return items from table by date 
def select_items(table, count):
    now  = datetime.now()
    then = now - timedelta(days=count, minutes=now.minute, hours=now.hour)
    now = now.strftime("%Y-%m-%d, %H:%M")
    then = then.strftime("%Y-%m-%d, %H:%M")
    fe = Attr('upload_time').between(then, now)
    response = table.scan(
      FilterExpression=fe
    )
    if (response['Count'] == 0):
        return 'None'
    else:
        items = response['Items']
        return items


def lambda_handler(event, context):
    
    count = int(event['count'])
    
    #init dynamodb table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    
    items = select_items(table, count)
 
    return {
        "statusCode": 200,
        "body": items
      }