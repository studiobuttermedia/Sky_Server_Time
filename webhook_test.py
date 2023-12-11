# This is a Test File to see if your webhook working

import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('webhook')
message_id = os.getenv('message_id')
avatar = os.getenv('avatar')

y = requests.post(url , data={
    'username': 'Sky Time',
    'avatar_url': avatar,
    'content': 'Congrats! You just send a webhook message. Now right click on this message and copy the Message ID to continue'})
