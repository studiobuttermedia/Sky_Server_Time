import signal
import sys
import requests
import time
import datetime
import pytz

from dotenv import load_dotenv
import os

server_now = datetime.datetime.now()
log_time = server_now.strftime("%Y-%m-%d %H:%M:%S")


print(f"To interrupt this program, press CTRL + C (CMD + C)")
print(f'[{log_time}] Running Program')

load_dotenv()

url = os.getenv('webhook')
message_id = os.getenv('message_id')
avatar = os.getenv('avatar')

def handle_interrupt(signal, frame):
   print(f"[{log_time}] Exiting Program")
   sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

while True:
   # Perform the desired operations here
   tz = pytz.timezone('America/Los_Angeles')
   current_time = datetime.datetime.now(tz)

   if current_time.hour == 00 and current_time.minute == 00:
      tomorrow = current_time + datetime.timedelta(days=1)
      print(f'[{log_time}] Setting Server Time')
      unix = int(tomorrow.timestamp())
      y = requests.patch(url + '/messages/' + message_id, data={
    'username': 'Sky Time',
    'avatar_url': 'avatar',
    'content': 'Server Reset <t:' + str(unix) + ':R>'})
      pass

   # Delay execution for 5 minutes
   time.sleep(60)  # 300 seconds = 5 minutes