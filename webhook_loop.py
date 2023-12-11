import requests
import time
import datetime

url = 'https://discord.com/api/webhooks/1183675444671807568/sJJdaC0ilRhZaPjLHA9ZNpex5bI8l30YD95px3HF_0p61XdN33QHwiv1zUkRorcoCi4y'
ts = time.time

today = datetime.date.today()
# Get tomorrow's date
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

# Set the time you want to send the message
hour = 14
minute = 00

# Combine the date and time
tomorrow_at_specific_time = datetime.datetime.combine(tomorrow, datetime.time(hour, minute))

# Convert to Unix timestamp
unix_timestamp = int(tomorrow_at_specific_time.timestamp())

# Set the time you want to send the message
hour1 = 23
minute1 = 00

# Combine the date and time
tomorrow_at_specific_time_china = datetime.datetime.combine(today, datetime.time(hour1, minute1))

# Convert to Unix timestamp
unix_timestamp2 = int(tomorrow_at_specific_time_china.timestamp())

y = requests.patch(url + '/messages/1183693061759455372', data={
    'username': 'Sky Time',
    'avatar_url': 'https://studiobutter-private.tixte.co/r/sky_light.png',
    'content': 'Global: Server Reset <t:' + str(unix_timestamp) + ':R>\nChina: Server Reset <t:' + 
    str(unix_timestamp2) + ':R>'})
