#built-in libraries
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime, date, time, timedelta


#return items from table by url 
def select_items(table, count):
    now  = datetime.now()
    then = now - timedelta(days=count, minutes=now.minute, hours=now.hour)
    now = now.strftime("%Y-%m-%d, %H:%M")
    then = then.strftime("%Y-%m-%d, %H:%M")
    fe = Attr('upload_time').between(then, now)
    response = table.scan(
      FilterExpression=fe
    )
    items = response['Items']
    return items


def lambda_handler(event, context):
    
    count = int(event['count'])
    
    #init dynamodb table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    
    items = select_items(table, count)
    for item in items:
        print(item)
    

    return {
        "statusCode": 200,
        "body": items
      }