import json
import bs4 as bs
from botocore.vendored import requests

def lambda_handler(event, context):
        r = requests.get('https://serverless.com/')
        data = r.content
        soup = bs.BeautifulSoup(data,'lxml')
        s = soup.find('title')
        return {
            "statusCode": 200,
            "body": json.dumps(title.text)
        }
