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
nettype = "wireless switch"
tz = 'America/Chicago'

#add tags for ADP Code, State, and City.
tags = adpcode

#Script for what Organization?

#Prompt for settings

#Search for Site first based on tags and name
print('Creating network with the name of '+name+)

#Confirm and submit


result = m.addnetwork(apikey,orgid,networkname,nettype,tags,tz,suppressprint=True) 
pprint(result) 

#import results to varibles
def addnetwork_results(parameter1,parameter2):
	#do something with parameters
	print(parameter1)
	print(str(parameter2))


# Bind a network to a template.
# https://dashboard.meraki.com/api_docs#bind-a-network-to-a-template
result = m.bindtotemplate(apikey, networkid, templateid, autobind=False, suppressprint=False):
pprint(result) 