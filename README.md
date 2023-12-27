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
```

It should look like this

```
webhook='https://discord.com/api/webhooks/.../...'
message_id=''
```

You can try testing your Webhook to see if it works by running "webhook_test.py" using this command

```python webhook_test.py```

Once run, you should see a message to copy the message ID. Right Click on the message ,choose copy message ID and return to your .env. DO NOT DELETE THE MESSAGE

Paste in your Message ID, it should look like this

```message_id = '654064604650465'```

Now try run this command to see if the time reset message works or not

```python webhook_loop.py```

If it does! Congrats! Your Webhook is working!

## Automations
Version 1.1 recently added ability to always running. But you will need to manually setup the program to start after your PC or Server restart or something.

## Optional Setting
In the ```.env``` file, You can set your webhook to show a profile picture

Adding this line will help

```avatar = 'YOUR PFP URL'```

**PLEASE NOTE THAT PROFILE PICTURES HOSTED USING DISCORD CDN WILL NOT WORK DUE TO CHANGES TO DISCORD BACKEND.**  You can use [Tixte](https://tixte.com/) to host your profile images.