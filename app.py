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

filename = "time.txt"
if not os.path.isfile(filename):
   open(filename, "w").close()
   print(f"Cache File '{filename}' was created. Please do not delete this file when the application is running")
   print(f"To interrupt this program, press CTRL + C (CMD + C)")
   print(f'[{log_time}] Running Program')
else:
   print(f"Cache file '{filename}' exists. Reusing file. Please do not delete this file when the application is running")
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
   la_tz = pytz.timezone('America/Los_Angeles')
   la_time = datetime.datetime.now(la_tz)

   cn_tz = pytz.timezone('Asia/Shanghai')
   cn_time = datetime.datetime.now(cn_tz)
   if la_time.hour == 00 and la_time.minute == 00:
      la_tomorrow = la_time + datetime.timedelta(days=1)
      print(f'[{log_time}] Setting Server Time (Sky - Global Server)')
      la_unix = int(la_tomorrow.timestamp())
      with open('time.txt', 'r') as c:
         cn_cache = str(c.read())
      y = requests.patch(url + '/messages/' + message_id, data={
    'username': 'Sky Time',
    'avatar_url': 'avatar',
    'content': 'Global: Server Reset <t:' + str(la_unix) + ':R>\nChina: Server Reset <t:' + 
    cn_cache+ ':R>'})
      c.close
      with open('time.txt', 'w') as f:
         f.write(str(la_unix))
   elif cn_time.hour == 00 and cn_time.minute == 00:
      cn_tomorrow = cn_time + datetime.timedelta(days=1)
      print(f'[{log_time}] Setting Server Time (Sky - NetEase/BiliBili Server)')
      cn_unix = int(cn_tomorrow.timestamp())
      with open('time.txt', 'r') as l:
         la_cache = str(l.read())
         a = requests.patch(url + '/messages/' + message_id, data={
    'username': 'Sky Time',
    'avatar_url': 'avatar',
    'content': 'Global: Server Reset <t:' + la_cache + ':R>\nChina: Server Reset <t:' + 
    str(cn_unix) + ':R>'})
         a.close
         with open('time.txt', 'w') as z:
            z.write(str(cn_unix))
   else: 
      pass

   # Delay execution for 5 minutes
   time.sleep(60)  # 300 seconds = 5 minutes