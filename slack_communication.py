import re
import time
import json
from slackclient import SlackClient
import sys, os

#Messaging Channel
channel = "channel"
token = ""

def communicationStatus():
	if slack_client.rtm_connect():
		return True
	
	return False

def initialize():
    #token = "xoxb-192681167893-e2VjaeDIg9rInQsoKuydywJu"
    print("token%s" % (token))
    slack_client = SlackClient(token)
    user_list = slack_client.api_call("users.list")  
    for user in user_list.get('members'):  
		if user.get('name') == "house":
	        	print("user id: %s" % user.get('id'))6
			slack_user_id = user.get('id')
			break
    if slack_client.rtm_connect():  
		print("Connected!")
		while True:
			for message in slack_client.rtm_read():
				if 'text' in message:
					print("message read as:%s" % message['text'])

				if 'text' in message and message['text'].startswith("<@%s>" % slack_user_id):
					channel = message['channel']
					print("Message received: %s" % (json.dumps(message, indent=2)))
					if re.match('(hello)', message['text'], re.IGNORECASE):
						slack_client.api_call(
                                            "chat.postMessage",
                                            channel=message['channel'],
                                            text="Hi Lajith",
                                            as_user=True)
						time.sleep(1)
					else:
						if 'text' in message and re.match('(hello)', message['text'], re.IGNORECASE):
							channel = message['channel']
							print("Messaging channel: %s" % channel)
							slack_client.api_call(
                                                "chat.postMessage",
                                                channel="D5PBHLH70",
                                                text="Hi Lajith hiii",
                                                as_user=True)
							time.sleep(1)
						else:
							if 'text' in message and re.match('(shutdown)',message['text'], re.IGNORECASE):
								print ("SHUTDOWN REQUEST")
								slack_client.api_call(
												    "chat.postMessage",
                                                    channel="D5PBHLH70",
                                                    text="SHUTDOWN INITIATED. GOOD BYE",
                                                    as_user=True)
								time.sleep(1)
								raise Exception('Shutdown request from lajith')



