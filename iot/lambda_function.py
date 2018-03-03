import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('ses')
source = "from:email"
destination = {
        "ToAddresses": [
            "to:email"
        ]
    }
message =  {
        "Subject": {
            "Data": "Dash Button Puppies"
        },
        "Body": {
            "Text": {
                "Data": "Hi! Remember how we did a scene about Amazon Dash buttons delivering puppies? Here you go! https://gph.is/2liYlbW"
            },
            "Html":{
                "Data": '<p>Remember that sketch about push button puppy delivery? I have done it. This email was sent using an amazon dash button.</p> <p><a href="https://giphy.com/gifs/LyKsWcZiTxSrS">DRONES!!!</a></p><p><a href="https://giphy.com/gifs/sleeping-puppies-pile-zPGJzH8fXsoBW">Puppies!</a></p>'
            }
        }
    }


def lambda_handler(event, context):
    logger.info('Received event: ' + json.dumps(event))
    response = client.send_email(Source=source, Destination=destination, Message=message)
    logger.info('Email sent!')