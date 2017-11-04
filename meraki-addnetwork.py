from meraki import meraki as m
from vars import apikey, org
from pprint import pprint
import json

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
adpcode = input('What is the sites ADP code? ')

#Build Regex Check ([A-Z][A-Z][0-9][0-9][0-9])
friendlyname = input('What is the friendly name for the site? ')

#limit to 32 characters, only _ allowed
networkname = adpcode+"-"+friendlyname

#API Vars
name = networkname
orgid = org
nettype = "wireless switch"
tz = 'America/Chicago'

#add tags for ADP Code, State, and City.
tags = adpcode

#Script for what Organization?

#Prompt for settings

#Search for Site first based on tags and name
print('Creating network with the name of '+name)

#Confirm and submit


result = m.addnetwork(apikey,orgid,networkname,nettype,tags,tz,suppressprint=True) 
pprint(result) 

#import results to varibles
the_dict = json.loads(result)


# Bind a network to a template.
# https://dashboard.meraki.com/api_docs#bind-a-network-to-a-template
#result = m.bindtotemplate(apikey, networkid, templateid, autobind=False, suppressprint=False):
pprint(id) 


# Claim a device into a network
# https://dashboard.meraki.com/api_docs#claim-a-device-into-a-network
#def adddevtonet(apikey, networkid, serial, suppressprint=False):

