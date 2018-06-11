print("Program Booting please wait........")

#importing communication unit
print("Initialing Communication Unit")
import slack_communication as communicator

def communicatorCallback(msg):
	print("Recieved " % msg)

communicator.token = "xoxb-192681167893-e2VjaeDIg9rInQsoKuydywJu"
communicator.initialize(communicatorCallback)
communicator.initiate()

if(communicator.communicationStatus())
	print("Communciation status:Online")
else 
	print ("Communciation status:Offline")

