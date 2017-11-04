from meraki import meraki as m
from vars import apikey, org
from pprint import pprint

# Create a network
# https://dashboard.meraki.com/api_docs#create-a-network
#def addnetwork(apikey, orgid, name, nettype, tags, tz, suppressprint=False):

#Local Vars
adpcode = input('What is the sites ADP code? ')

#Build Regex Check ([A-Z][A-Z][0-9][0-9][0-9])
friendlyname = input('What is the friendly name for the site? ')

#limit to 32 characters, only _ allowed
networkname = adpcode+"-"+friendlyname

#API Vars
name = networkname
orgid = org
nettype = "wireless Switch"
tz = 'America/Chicago'

#add tags for ADP Code, State, and City.
tags = adpcode

#Script for what Organization?

#Prompt for settings

#Search for Site first based on tags and name
print('Network with the name of '+name+' created')

#Confirm and submit


#post m.addnetwork(apikey,orgid,name,nettype,tags,tz)