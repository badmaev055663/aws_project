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

#find item in table and return if exists
def get_img_item(table, url, type):
    response = table.get_item(
      Key = {
         'url': url,
         'filter': type
      }
    )
    if 'Item' in response:
      return response['Item']
    else:
      return None

#process image 
def process_img(type):
    image = Image.open('/tmp/img.jpg')
    if type == 'BLUR':
      processed = image.filter(ImageFilter.BLUR)
    elif type == 'SHARPEN':
      processed = image.filter(ImageFilter.SHARPEN)
    elif type == 'EMBOSS':
      processed = image.filter(ImageFilter.EMBOSS)
    elif type == 'DETAIL':
      processed = image.filter(ImageFilter.DETAIL)
    elif type == 'SMOOTH':
      processed = image.filter(ImageFilter.SMOOTH)
    processed.save("/tmp/processed.jpg")
  
#upload to s3 bucket
def upload_s3():
    processed_file = open("/tmp/processed.jpg", "rb")
    s3 = boto3.client('s3')
    fileobj = BytesIO(processed_file.read())
    
    key = ''.join(choice(ascii_lowercase) for i in range(7))
    file_name = 'images/'+ key + '.jpg'   #generate filename
    s3.upload_fileobj(fileobj, 'aws-project-badmaev', file_name, ExtraArgs={'ACL': 'public-read'})
    return key
  
def lambda_handler(event, context):
    #url of source and type of filter
    url = event['url']
    type = event['type']
    
    #init dynamodb table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('img_table')
    
    item = get_img_item(table, url, type)
    
    # if such item not found in table, proccess image, upload image to s3, put new item into table
    if (item == None):
      urllib.request.urlretrieve(url, "/tmp/img.jpg") #get source img by url
      process_img(type)
      img_id = upload_s3()
      response = table.put_item(
        Item={
            'url': url,
            'filter': type,
            'img_id': img_id
        })
    # if found immeadiatly get img_id for already existing image in s3 bucket
    else:
      img_id = item['img_id']

    return {
        "statusCode": 200,
        "body": 'images/' + img_id + '.jpg'
      }