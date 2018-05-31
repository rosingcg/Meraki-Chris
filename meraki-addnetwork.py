from meraki import meraki as mer
from vars import apikey, org
from pprint import pprint
import json
import requests
import re
import pandas as pd
from tabulate import tabulate
import ftpadp
import time

class bcolors:
    #cyan
    HEADER = '\033[32m'
    #purple
    QUESTION = '\033[35m'
    #lightblue
    ACTION = '\033[34m'
    #blue
    VARIABLE = '\033[94m'
    #yellow
    RESULT = '\033[33m'
    #red
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def explore_next(apikey,apidata,headers,selector="none",column_name="none",justPrint=False):
    #print(len(apidata))
    if '[' in str(apidata): #quick check if there are multiple 'rows' in json, starts with '[{data},{data}]'
        df = pd.DataFrame(apidata)
    else:
        df = pd.DataFrame(apidata, index=[0]) #pandas is weird for JSON w/ only 1 'row' : '{data}'
    df.index.names = ['Selection']
    if df.empty:
        return "empty"    
    try:
        df = df[headers]
    except:
        "Can't set headers, showing all"
    print (tabulate(df, headers='keys',tablefmt="fancy_grid"))

    if not justPrint:
        user_input = input(bcolors.QUESTION + "Select the row number which contains the "+selector +" you wish to configure  :  " + bcolors.ENDC)
        #print("Org ID = "+ str(df.iloc[1]['id']))
        data = str(df.iloc[int(user_input)][column_name])
        return data
    else:
        return "nada"

# Create a network
# https://dashboard.meraki.com/api_docs#create-a-network
#def addnetwork(apikey, orgid, name, nettype, tags, tz, suppressprint=False):


#Local Vars


#Download adp_locations.csv from FTP Server


adpupdate = input(bcolors.QUESTION + 'Do you want to refrest the ADP list? [yes/no]' + bcolors.ENDC)

if adpupdate == 'yes':
    ftpget = ftpadp.getadpcsv()
    
elif adpupdate != 'yes':
    print(bcolors.ACTION, 'ADP file will', bcolors.FAIL, ' NOT ', bcolors.ACTION, 'be downloaded.', bcolors.ENDC)


#Select Orgainization from Defined Function expore_next
apidata = mer.myorgaccess(apikey,suppressprint=True)
# id|name|samlConsumerUrl|samlConsumerUrls
selectedOrg = explore_next(apikey,apidata,['id','name'],"Organization","id")


print(bcolors.HEADER, "Let's set up your Meraki Network.  You will define the ADP Code and Site Friendly name.  The Network Type, Timezone, and Tags are already configured for you.", bcolors.ENDC)
#ADP Code with REGEX Verification
while True:
    adpcode = input(bcolors.QUESTION + 'What is the sites ADP code? ' + bcolors.ENDC)

    while not re.match("^[A-Z][A-Z][0-9][0-9][0-9]", adpcode):
        print (bcolors.FAIL,"Error! Make sure your ADP Code contains 2 letters, then 3 numbers", bcolors.ENDC)
        adpcode = input(bcolors.QUESTION + 'What is the sites ADP code? ' + bcolors.ENDC)
    else:
        print("ADP Code is "+ adpcode)
        break


#Friendly Name with REGEX
while True:
    friendlyname = input(bcolors.QUESTION + 'What is the friendly name for the site? ' + bcolors.ENDC )

    while not re.match("^[A-Za-z_]{0,25}$", friendlyname):
        print (bcolors.FAIL,"Error! Invalid Site Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.",bcolors.ENDC)
        friendlyname = input(bcolors.QUESTION + 'What is the friendly name for the site? '+ bcolors.ENDC )
    else:
        print("ADP Code is "+ friendlyname)
        break

networkname = adpcode+"-"+friendlyname

#API Vars
name = networkname
nettype = "wireless switch"
tz = 'America/Chicago'

#add tags for ADP Code, State, and City.
tags = adpcode + ' APITEST'


#Prompt for settings

#Search for Site first based on tags and name
print(bcolors.ACTION + 'Creating network with the name of ',bcolors.VARIABLE + name, '.', bcolors.ENDC)

#Confirm and submit


newnetwork = mer.addnetwork(apikey,selectedOrg,networkname,nettype,tags,tz,suppressprint=True)

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

print(bcolors.HEADER, "\nNow that the network is set up, let's bind it to a template. Select the template you wish to use.", bcolors.ENDC)
#List Templates
templatelist = mer.gettemplates(apikey, selectedOrg, suppressprint=True)

selectedTemplate = explore_next(apikey,templatelist,['id','name'],"Template","id")


#Choose Template to be Assinged
#assignedtemplateid = input(bcolors.QUESTION + 'What is your TemplateID? ' + bcolors.ENDC)

while True:
    apidata = mer.getnetworkdetail(apikey,newnetworkid,suppressprint=True)
    result = explore_next(apikey,apidata,['name','id','tags','timeZone','type'],justPrint=True)
    if result != "empty":
        break
    print("Initializing Network: adding 5 seconds")
    time.sleep(5)



print(bcolors.ACTION,'We will now autobind to the Standard Template', bcolors.ENDC)

#Notifiy of action taken and take it
print(bcolors.ACTION,'We will now autobind to the Standard Template', bcolors.ENDC)
bindtempate = mer.bindtotemplate(apikey, newnetworkid, selectedTemplate, autobind=False, suppressprint=False)

#Print result from API
print(bcolors.RESULT, bindtempate, bcolors.ENDC)

#Add Swich to the Network, Verify Serialnumber with Regex
print(bcolors.ACTION,'Now it is time to add a swtich to the network', bcolors.ENDC)

while True:
    switchsn = input(bcolors.QUESTION + 'What is the Switch Serial Number (QNXX-XXXX-XXXX) (Q2EX-X5WR-SQAU for testing)? ' + bcolors.ENDC)

    while not re.match("[Q][2][A-Z0-9][A-Z0-9]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]", switchsn):
        print (bcolors.FAIL,"Invalid Format for Serial Number.  Please try again.",bcolors.FAIL)
        switchsn = input(bcolors.QUESTION + 'What is the Switch Serial Number (QNXX-XXXX-XXXX) (Q2EX-X5WR-SQAU for testing)? ' + bcolors.ENDC)
    else:
        print("Switch Serial number is "+ switchsn)
        break

# Claim a device into a network
# https://dashboard.meraki.com/api_docs#claim-a-device-into-a-network
#def adddevtonet(apikey, networkid, serial, suppressprint=False):
addswitch = mer.adddevtonet(apikey, newnetworkid, switchsn, suppressprint=False)
print(bcolors.RESULT, addswitch, bcolors.ENDC)


#Add AP to the network, Verify Serial number with Regex
print(bcolors.ACTION,'Now it is time to add an Access Point to the network', bcolors.ENDC)
while True:
    apsn = input(bcolors.QUESTION + ' What is the Access Point Serial Number (QNXX-XXXX-XXXX) (Q2KD-3PUQ-K9KX for testing)? ' + bcolors.ENDC)

    while not re.match("[Q][2][A-Z0-9][A-Z0-9]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]", apsn):
        print ("Error! Make sure your ADP Code contains 2 letters, then 3 numbers")
        switchsn = input(bcolors.QUESTION + ' What is the Access Point Serial Number (QNXX-XXXX-XXXX) (Q2KD-3PUQ-K9KXfor testing)? ' + bcolors.ENDC)
    else:
        print("Access Point Serial number is "+ apsn)
        break

# Claim a device into a network
# https://dashboard.meraki.com/api_docs#claim-a-device-into-a-network
#def adddevtonet(apikey, networkid, serial, suppressprint=False):
addap = mer.adddevtonet(apikey, newnetworkid, apsn, suppressprint=False)
print(bcolors.RESULT, addap, bcolors.ENDC)


#Configure Switch and AP

# Update the attributes of a device
# https://dashboard.meraki.com/api_docs#update-the-attributes-of-a-device
#def updatedevice(apikey, networkid, serial, name=None, tags=None, lat=None, lng=None, address=None, move=None, suppressprint=False):

print(bcolors.HEADER,'Now we need to give it a name and Street Address', bcolors.ENDC)

addressstreet = input(bcolors.QUESTION + 'What is the Street Address?  (Do not include Suite number): ' + bcolors.ENDC)


while True:
    addresscity = input(bcolors.QUESTION + 'What City? ' + bcolors.ENDC )

    while not re.match("^[A-Za-z_]{0,25}$", addresscity):
        print (bcolors.FAIL,"Error! Invalid City Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.", bcolors.ENDC)
        addresscity = input(bcolors.QUESTION + 'What City? ' + bcolors.ENDC )
    else:
        break

while True:
    addressstate = input(bcolors.QUESTION + 'What State (2 Letters, Capitalized): ' + bcolors.ENDC)

    while not re.match("[A-Z]{2}", addressstate):
        print (bcolors.FAIL,"Invalid Format",bcolors.ENDC)
        switchsn = input(bcolors.QUESTION + 'What State (2 Letters, Capitalized): ' + bcolors.ENDC)
    else:
        break


while True:
    addresszip = input(bcolors.QUESTION + 'Zip Code? ' + bcolors.ENDC)

    while not re.match("[0-9]{5}", addresszip):
        print (bcolors.FAIL,"Invalid Format, Zip code should contain only 5 numbers",bcolors.ENDC)
        addresszip = input(bcolors.QUESTION + 'Zip Code? ' + bcolors.ENDC)
    else:
        break

fulladdress = addressstreet + ', ' + addresscity + ', ' + addressstate + ' ' +addresszip
print(bcolors.ACTION,'This is the address that will be used:\n', bcolors.VARIABLE, fulladdress, bcolors.ENDC,sep='')

#Configure Switch
configswitch = mer.updatedevice(apikey, newnetworkid, switchsn, name=newnetworkname+'-AS01', lat=None, lng=None, address=fulladdress, move=True, suppressprint=False)
# Get your id/name and print.
newswitchlanIp = configswitch.get('lanIp')
newswitchserial = configswitch.get('serial')
newswitchmac = configswitch.get('mac')
newswitchlat = configswitch.get('lat')
newswitchlng = configswitch.get('lng')
newswitchaddress = configswitch.get('address')
newswitchname = configswitch.get('name')
newswitchmodel = configswitch.get('model')
newswitchnetworkid = configswitch.get('networkId')

#Configure AP
configap = mer.updatedevice(apikey, newnetworkid, apsn, name=newnetworkname+'-AP01', lat=None, lng=None, address=fulladdress, move=True, suppressprint=False)

newaplanIp = configap.get('lanIp')
newapserial = configap.get('serial')
newapmac = configap.get('mac')
newaplat = configap.get('lat')
newaplng = configap.get('lng')
newapaddress = configap.get('address')
newapname = configap.get('name')
newapmodel = configap.get('model')
newapnetworkid = configap.get('networkId')

#Result Printout

print(bcolors.HEADER,'Information about the switch added\n' )
print(bcolors.RESULT,'The switch added is a ',bcolors.VARIABLE, newswitchmodel, bcolors.ENDC)
print(bcolors.RESULT,'Switch LAN IP address is:\t',bcolors.VARIABLE, newswitchlanIp, bcolors.ENDC)
print(bcolors.RESULT,'The serial number is ',bcolors.VARIABLE, newswitchserial, bcolors.RESULT, ' with a MAC address of ',bcolors.VARIABLE,newswitchmac,bcolors.ENDC)
print(bcolors.RESULT,'Its location Lat/Long is ',bcolors.VARIABLE, newswitchlat, bcolors.RESULT,' and ',bcolors.VARIABLE, newswitchlng, bcolors.ENDC)
print(bcolors.RESULT,'The sites address is\n',bcolors.VARIABLE, newswitchaddress, bcolors.ENDC)


print(bcolors.HEADER,'Information about the access point added\n' )
print(bcolors.RESULT,'The access point added is a ',bcolors.VARIABLE, newapmodel, bcolors.ENDC)
print(bcolors.RESULT,'Access point LAN IP address is:\t',bcolors.VARIABLE, newaplanIp, bcolors.ENDC)
print(bcolors.RESULT,'The serial number is ',bcolors.VARIABLE, newapserial, bcolors.RESULT, ' with a MAC address of ',bcolors.VARIABLE,newapmac,bcolors.ENDC)
print(bcolors.RESULT,'Its location Lat/Long is ',bcolors.VARIABLE, newaplat, bcolors.RESULT,' and ',bcolors.VARIABLE, newaplng, bcolors.ENDC)
print(bcolors.RESULT,'The sites address is\n',bcolors.VARIABLE, newapaddress, bcolors.ENDC)


