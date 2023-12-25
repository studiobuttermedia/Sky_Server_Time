import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('webhook')
message_id = os.getenv('message_id')
avatar = os.getenv('avatar')


today = datetime.date.today()
# Get tomorrow's date
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

# Set the time you want to send the message
hour = int(os.getenv('global_hour'))
minute = int(os.getenv('global_minute'))

# Combine the date and time
tomorrow_at_specific_time = datetime.datetime.combine(tomorrow, datetime.time(hour, minute))

# Convert to Unix timestamp
unix_timestamp = int(tomorrow_at_specific_time.timestamp())

# Set the time you want to send the message
hour1 = int(os.getenv('china_hour'))
minute1 = int(os.getenv('china_minute'))

# Combine the date and time
tomorrow_at_specific_time_china = datetime.datetime.combine(today, datetime.time(hour1, minute1))

# Convert to Unix timestamp
unix_timestamp2 = int(tomorrow_at_specific_time_china.timestamp())

y = requests.patch(url + '/messages/' + message_id, data={
    'username': 'Sky Time',
    'avatar_url': 'avatar',
    'content': 'Global: Server Reset <t:' + str(unix_timestamp) + ':R>\nChina: Server Reset <t:' + 
    str(unix_timestamp2) + ':R>\nThis message was manually trigger due to a bug with V2. It has been fixed and V2 will be release soon'})
