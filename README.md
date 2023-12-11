# Sky Server Time
A kinda simple Python files that use to track Server Reset time for Sky: Children of the Light, supports for Global server, NetEase server and China server

## Setting up - Server side

First download [Python](https://www.python.org/downloads/)

Any version Python will work but the current version support that I use on PC and Linux Server is 3.11

On Windows 10 or Windows 11, you can use this command

```winget install Python.Python.3.11```

On Linux (Ubuntu for now), you can use this command

```sudo apt install python3.11```

Download the release package. Choose if you want the GB.zip, CN.zip or GBCN.zip

Extract the downloaded package to a folder you want to store

After that, run this command to install the required packages to run the server

```pip install -r requirements.txt```

## Setting up - Discord side
A PC is require to do this as creating webhook is PC only

On your Discord server, right click on the channel you want to send and choose "Integrations"

Choose Webhook and create a new Webhook. Once created, rename your Webhook and click 'Copy Webhook URL'

You also need to enable Developer Mode to get the Message ID

Create a ```.env``` file and add this line

```
webhook = 'YOUR WEBHOOK URL'
message_id =
global_hour = 'HOUR WHEN SKY SERVER RESET'
global_minute = 'MINUTES WHEN SKY SERVER RESET'
```

You can check when Sky server reset for you by going to [this website](https://sky-clock.netlify.app/), and check the "Daily Reset" Section, "Next Event" Column. Two digits on the left correspond with hour and two digits on the right correspond with minutes.

It should look like this

```
webhook='https://discord.com/api/webhooks/.../...'
message_id=''
global_hour = '23'
global_minute = '00'
```

If you also play China server, add the following lines

```
china_hour = '18'
china_minute = '00'
```

Depending on your timezone, it maybe different. China server reset at 12 am (UTC+8). Use a time converter website to see when is that time at your local time.

Numbers shown are just for filler, please use the website to see when the server reset.

You can try testing your Webhook to see if it works by running "webhook_test.py" using this command

```python webhook_test.py```

Once run, you should see a message to copy the message ID. Right Click on the message ,choose copy message ID and return to your .env. DO NOT DELETE THE MESSAGE

Paste in your Message ID, it should look like this

```message_id = '654064604650465'```

Now try run this command to see if the time reset message works or not

```python webhook_loop.py```

If it does! Congrats! Your Webhook is working!

## Automations
Setting up so the message updates every reset.

On Windows, use Task Scheduler. Tho I'm used to Scheduling task on Linux and Windows is bit complicated

On Linux (Ubuntu), use crontab with this command

```crontab -e```

If it ask, choose 1

Scroll down and enter the following:

```mm hh * * * /bin/python3 /where/your/webhook_loop.py```

```mm hh * * * /bin/python3 /where/your/webhook_loop_next.py```

MM is Minutes and HH is hour. Depending on your timezone, it may be different

The second line is optional and only use if you also need to see China Reset time.

Use the same time when the server reset to trigger the command on reset time. This will refresh the time message on Discord to the next reset time.

## Optional Setting
In the ```.env``` file, You can set your webhook to show a profile picture

Adding this line will help

```avatar = 'YOUR PFP URL'```

**PLEASE NOTE THAT PROFILE PICTURES HOSTED USING DISCORD CDN WILL NOT WORK DUE TO CHANGES TO DISCORD BACKEND.**  You can use [Tixte](https://tixte.com/) to host your profile images.