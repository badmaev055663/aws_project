#built-in libraries
import json
import urllib.request
import boto3
from io import BytesIO
from random import choice
from string import ascii_lowercase

# extrenal libraries
from PIL import Image
from PIL import ImageFilter


def lambda_handler(event, context):
    #get image
    url = event['url']
    type = event['type']
    urllib.request.urlretrieve(url, "/tmp/img.jpg")
    
    #process image
    image = Image.open('/tmp/img.jpg')
    if type == 'BLUR':
        processed = image.filter(ImageFilter.BLUR)
    elif type == 'SHARPEN':
        processed = image.filter(ImageFilter.SHARPEN)
    elif type == 'EMBOSS':
        processed = image.filter(ImageFilter.EMBOSS)
   
    processed.save("/tmp/processed.jpg")
    new_file = open("/tmp/processed.jpg", "rb")
    
    #upload image to bucket
    s3 = boto3.client('s3')
    fileobj = BytesIO(new_file.read())
    
    #generate filename
    key = ''.join(choice(ascii_lowercase) for i in range(7))
    file_name = 'images/'+ key + '.jpg'
    s3.upload_fileobj(fileobj, 'aws-project-badmaev', file_name, ExtraArgs={'ACL': 'public-read'})
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    response = table.put_item(
        Item={
            'img_id': key,
            'origin_url': url,
            'type': type
        })
    return {
      "statusCode": 200,
      "body": file_name,
    }