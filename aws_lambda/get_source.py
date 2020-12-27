#built-in libraries
import json
import boto3


def lambda_handler(event, context):
    #get image
    img_id = event['image_id']
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    pr_expr = "origin_url"
    response = table.get_item(
      ProjectionExpression= pr_expr,
      Key={
        "img_id": img_id
      })
       
    return {
      "statusCode": 200,
      "body": response["Item"]["origin_url"]
    }