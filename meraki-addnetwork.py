from meraki import meraki as mer
from vars import apikey, orgid
from pprint import pprint
import json
import requests
import re
import pandas as pd
from tabulate import tabulate

class bcolors:
    QUESTION = '\033[95m'
    ACTION = '\033[94m'
    VARIABLE = '\033[92m'
    RESULT = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'

# Create a network
# https://dashboard.meraki.com/api_docs#create-a-network
#def addnetwork(apikey, orgid, name, nettype, tags, tz, suppressprint=False):

#Vars Verification
def __validip(ip):
    """

    Args:
        ip: IP Address to be tested

    Returns: None, raises ValueError on invalid formating for IP address

    """
    try:
        ip_address(ip)
    except ValueError:
        raise ValueError('Invalid IP Address')



#Local Vars

# while True adpcode = input('What is the sites ADP code? ')

#     while not re.match("^[A-Z][A-Z][0-9][0-9][0-9]", adpcode):
#         print ("Error! Make sure your ADP Code contains 2 letters, then 3 numbers")
#     else:
#         print("ADP Code is "+ adpcode)
print(bcolors.HEADER, "Let's set up your Meraki Network.  You will define the ADP Code and Site Friendly name.  The Network Type, Timezone, and Tags are already configured for you.", bcolors.ENDC)
adpcode = input(bcolors.QUESTION + 'What is the sites ADP code? ' + bcolors.ENDC )
friendlyname = input(bcolors.QUESTION + 'What is the friendly name for the site? ' + bcolors.ENDC )

#limit to 32 characters, only _ allowed
networkname = adpcode+"-"+friendlyname

#API Vars
name = networkname
nettype = "wireless switch"
tz = 'America/Chicago'

#add tags for ADP Code, State, and City.
tags = adpcode + ' APITEST'

#Script for what Organization?

#Prompt for settings

#Search for Site first based on tags and name
print(bcolors.ACTION + 'Creating network with the name of ',bcolors.VARIABLE + name, '.', bcolors.ENDC)

#Confirm and submit


newnetwork = mer.addnetwork(apikey,orgid,networkname,nettype,tags,tz,suppressprint=True) 
pprint(newnetwork) 

# Get your id/name and print.
newnetworkid = newnetwork.get('id')
newnetworkname = newnetwork.get('name')
newnetworkorg = newnetwork.get('organizationId')
newnetworktag = newnetwork.get('tags')
newnetworktz = newnetwork.get('timeZone')
newnetworktype = newnetwork.get('type')

print(bcolors.RESULT, '\nYour new netowrk id is:\t',bcolors.VARIABLE, newnetworkid, bcolors.ENDC)
print(bcolors.RESULT,'It is part of the organizationId with',bcolors.VARIABLE, newnetworkorg, bcolors.ENDC)
print(bcolors.RESULT,'The following tags were assigned to the network',bcolors.VARIABLE, newnetworktag, bcolors.ENDC)
print(bcolors.RESULT,'The network is set to the ',bcolors.VARIABLE, newnetworktz, bcolors.RESULT,'timezone', bcolors.ENDC)
print(bcolors.RESULT,'Network Type is now',bcolors.VARIABLE, newnetworktype, bcolors.ENDC)

# Bind a network to a template.
# https://dashboard.meraki.com/api_docs#bind-a-network-to-a-template
#newnetwork = mer.bindtotemplate(apikey, networkid, templateid, autobind=False, suppressprint=False)

print(bcolors.HEADER, "Now that the network is set up, let's bind it to a template. For now, just use the only template available.  You will need to use the field that starts with L_", bcolors.ENDC)
#List Templates
templatelist = mer.gettemplates(apikey, orgid, suppressprint=False)
pprint(templatelist)

#Choose Template to be Assinged
assignedtemplateid = input(bcolors.QUESTION + 'What is your TemplateID? ' + bcolors.ENDC )

#Notifiy of action taken and take it
print(bcolors.ACTION,'We will now autobind to the Standard Template', bcolors.ENDC)
bindtempate = mer.bindtotemplate(apikey, newnetworkid, assignedtemplateid, autobind=True, suppressprint=False)

#Print result from API
pprint(bcolors.RESULT, bindtempate, bcolors.ENDC)

#Add Swich to the Network
print(bcolors.ACTION,'Now it is time to add a swtich to the network', bcolors.ENDC)
switchsn = input(bcolors.QUESTION, 'What is the Switch Serial Number (QNXX-XXXX-XXXX) (Q2EX-X5WR-SQAU for testing)?', bcolors.ENDC)


# Claim a device into a network
# https://dashboard.meraki.com/api_docs#claim-a-device-into-a-network
#def adddevtonet(apikey, networkid, serial, suppressprint=False):
addswitch = mer.adddevtonet(apikey, networkid, swtichsn, suppressprint=False)
pprint(bcolors.RESULT, addswtich, bcolors.ENDC)


#add AP to the network
print(bcolors.ACTION,'Now it is time to add an Access Point to the network', bcolors.ENDC)
apsn = input(bcolors.QUESTION, 'What is the Switch Serial Number (QNXX-XXXX-XXXX) (Q2KD-3PUQ-K9KX for testing)?', bcolors.ENDC)


# Claim a device into a network
# https://dashboard.meraki.com/api_docs#claim-a-device-into-a-network
#def adddevtonet(apikey, networkid, serial, suppressprint=False):
addswitch = mer.adddevtonet(apikey, networkid, apsn, suppressprint=False)
pprint(bcolors.RESULT, addswtich, bcolors.ENDC)


#Configure Switch and AP

# Update the attributes of a device
# https://dashboard.meraki.com/api_docs#update-the-attributes-of-a-device
#def updatedevice(apikey, networkid, serial, name=None, tags=None, lat=None, lng=None, address=None, move=None, suppressprint=False):

print(bcolors.HEADER,'Now we need to give it a name and Street Address', bcolors.ENDC)
addressstreet = input(bcolors.QUESTION + 'What is the Street Address?  (Do not include Suite number): ' + bcolors.ENDC)
addresscity = input(bcolors.QUESTION + 'What City? : '+ bcolors.ENDC)
addressstate = input(bcolors.QUESTION + 'What State (2 Letters, Capitalized): ' + bcolors.ENDC)
addresszip = input(bcolors.QUESTION +'Zip Code? : '+ bcolors.ENDC)
fulladdress = addressstreet + "\n" + addresscity + ', ' + addressstate + ' ' +addresszip
print(bcolors.ACTION, 'This is the address that will be used:\n', bcolors.VARIABLE fulladdress, bcolors.ENDC)

#Configure Switch
configswitch = mer.updatedevice(apikey, networkid, switchsn, name=newnetworkname+'AS01', lat=None, lng=None, address=fulladdress, move=True, suppressprint=FALSE)

#Configure AP
configap = mer.updatedevice(apikey, networkid, apsn, name=newnetworkname+'AS01', lat=None, lng=None, address=fulladdress, move=True, suppressprint=FALSE)

#Result Printout
print(bcolors.RESULT, configswitch, bcolors.ENDC)
print(bcolors.RESULT, configAP, bcolors.ENDC)

