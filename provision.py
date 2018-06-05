
import ftpadp
import adpcsvsearch

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


def meraki_provision():
    print ("Meraki Yay!")
    print (bcolors.BOLD + 30 * "-" , "Meraki Device Configuration" , 30 * "-"+ bcolors.ENDC)
    
    #Ask for the Template to be used.  Prod, Dev, None
    print ("What Template are you going to use?")
    print ("1. Production Template")
    print ("2. Development Template")
    print ("3. Development Template")
    print ("100. Exit")
    templatetouse = int(input("Please select template option: "))


    # Ask how many switches
    numberofswitches = int(input("How many switches will you configure? ")

    #Ask how many Access Points
    numberofaps = int(input("How many access points will you configure? ")

    #create loop based number of switches
    #This logic needs to be adjusted, but not sure now.  We are if you have 2 switches, the first one will be primary, the second one will be a secondary. 
    #This is important becuase they get bound to different profile
    while numberofswitches >=1 True:
        primaryswitchsn = input(bcolors.QUESTION + "What is the Serial number of the primary switch? (QNXX-XXXX-XXXX) (Q2KD-3PUQ-K9KX for testing)"+ bcolors.ENDC)
        
    while not re.match("[Q][2][A-Z0-9][A-Z0-9]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]", primaryswitchsn):
        print ("Error! Make sure your serial number is in the correct format")
        primaryswitchsn = input(bcolors.QUESTION + "What is the Serial number of the primary switch? (QNXX-XXXX-XXXX) (Q2KD-3PUQ-K9KX for testing)" + bcolors.ENDC)
    else:
        numberofswitches = numberofswitches - 1
        #how do I go back to ask about the secondary switch?

    #create loopbased on number of APs

    #Ask for the serial number of the primary switch

    #Determine if it is a 48 port or 24 port switch

    #Ask for the serial number of the secondary switches

    #Determine if it is a 48 port or 24 port switch

    #Ask for the serial numbers of the APs

    #Print list of Switches by name, serial number, which is primary, which is secondary, what profile is bind to the switch

    #Print list of Access Points

    #Print Address to be associated with this

    #Confirm all information.  If not, present a list of items to modify.

    #apply settings to Meraki

    #End script






def silverpeak_provision():
    print("Silverpeak ...")

def manual_site_information():
    #ADP Code with REGEX Verification

print ("Provisioning Menu")
def provision_meraki():
    input("We will begin the proccess of provisioning a Meraki network for the first time.  Press any key to continue...")
    print("Please standby while we download the latest ADP list...")
    ftpadp.getadpcsv()
    adpcsvsearch.adpsearch

def manual_network_location():
    #adpcode = input('What is the sites ADP code? ')

    while True:
        adpcode = input(bcolors.QUESTION + 'What is the sites ADP code? ' + bcolors.ENDC)

    while not re.match("^[A-Z][A-Z][0-9][0-9][0-9]", adpcode):
        print (bcolors.FAIL,"Error! Make sure your ADP Code contains 2 letters, then 3 numbers", bcolors.ENDC)
        adpcode = input(bcolors.QUESTION + 'What is the sites ADP code? ' + bcolors.ENDC)
    else:
        print("ADP Code is "+ adpcode)


    #Friendly Name with REGEX

        break
    
    #friendlyname = input('What is the friendly name for the site? ')    

    while True:
        friendlyname = input(bcolors.QUESTION + 'What is the friendly name for the site? ' + bcolors.ENDC )

    while not re.match("^[A-Za-z_]{0,25}$", friendlyname):

        print (bcolors.FAIL,"Error! Invalid Friendly Site Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.",bcolors.ENDC)
        friendlyname = input(bcolors.QUESTION + 'What is the friendly name for the site? '+ bcolors.ENDC )
    else:
        print("ADP Code is "+ friendlyname)

    #Address
    while True:
        siteaddress = input(bcolors.QUESTION + 'What is the Street number and address? ' + bcolors.ENDC)
    
    #Need to modify Regex to include a space
    while not re.match("^[A-Za-z_]{0,35}$", siteaddress):
        print (bcolors.FAIL,"Error! Invalid Address.  Can only contain Uppercase, Lowercase, and underscores.",bcolors.ENDC)
        siteaddress = input(bcolors.QUESTION + 'What is the Street number and address? '+ bcolors.ENDC )
    else:
        print("Site Address is " + siteaddress)
    
    #City
    while True:
        addresscity = input(bcolors.QUESTION + 'What City? ' + bcolors.ENDC )

    while not re.match("^[A-Za-z_]{0,25}$", addresscity):
        print (bcolors.FAIL,"Error! Invalid City Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.", bcolors.ENDC)
        addresscity = input(bcolors.QUESTION + 'What City? ' + bcolors.ENDC )
    else:

    #State
    while True:
        addressstate = input(bcolors.QUESTION + 'What State (2 Letters, Capitalized): ' + bcolors.ENDC)

    while not re.match("[A-Z]{2}", addressstate):
        print (bcolors.FAIL,"Invalid Format",bcolors.ENDC)
        addressstate = input(bcolors.QUESTION + 'What State (2 Letters, Capitalized): ' + bcolors.ENDC)
    else:

    #Zip Code
    while True:
        addresszip = input(bcolors.QUESTION + 'Zip Code? ' + bcolors.ENDC)

    while not re.match("[0-9]{5}", addresszip):
        print (bcolors.FAIL,"Invalid Format, Zip code should contain only 5 numbers",bcolors.ENDC)
        addresszip = input(bcolors.QUESTION + 'Zip Code? ' + bcolors.ENDC)
    else:
    
    #Print Details from questions
    print("The Meraki network name is: " + adpcode + "-" + friendlyname)
    print("The site address is: ")
    print(siteaddress)
    print(addresscity + "\," + addressstate + "  " + addresszip)
    #If the information is correct, end defination.  If it is not, repeat questions
    #Repeat Questions needs to be built out with if statements
    addresscorrect = input("Is this information correct?")



=======
        print (bcolors.FAIL,"Error! Invalid Site Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.",bcolors.ENDC)
        friendlyname = input(bcolors.QUESTION + 'What is the friendly name for the site? '+ bcolors.ENDC )
    else:
        print("ADP Code is "+ friendlyname)
        break
    
    #Site Address input    
    while True:
        siteaddressstate = input(bcolors.QUESTION + 'What is address (Number and street)? ' + bcolors.ENDC )
    
    while not re.match("^[A-Za-z_]{0,25}$", siteaddressstate):
        print (bcolors.FAIL,"Error! Invalid Site Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.",bcolors.ENDC)
        siteaddressstate = input(bcolors.QUESTION + 'What is address (Number and street)? '+ bcolors.ENDC )
    else:
        print("Site address is:  "+ siteaddressstate)
        break
    
    #Site Address: City
    while True:
        siteaddresscity = input(bcolors.QUESTION + 'What City? ' + bcolors.ENDC )
    
    while not re.match("^[A-Za-z_]{0,25}$", siteaddresscity):
        print (bcolors.FAIL,"Error! Invalid Site Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.",bcolors.ENDC)
        siteaddresscity = input(bcolors.QUESTION + 'What City?  '+ bcolors.ENDC )
    else:
        print("Site city is:  "+ siteaddresscity)
        break

    
    #siteaddressstate = input('What is the State? ')
    while True:
        siteaddressstate = input(bcolors.QUESTION + 'What City? ' + bcolors.ENDC )
    
    while not re.match("^[A-Za-z_]{0,25}$", siteaddressstate):
        print (bcolors.FAIL,"Error! Invalid Site Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.",bcolors.ENDC)
        siteaddressstate = input(bcolors.QUESTION + 'What City?  '+ bcolors.ENDC )
    else:
        print("Site city is:  "+ siteaddressstate)
        break
        
    siteaddresszipcode = input('What is the Zip Code? ')
   

    networkname = adpcode+"-"+friendlyname
    print('\033[1;31mRed like Radish\033[1;m')
    #print ("Thanks for your input, here is your site information:", 'red')
    print(siteaddressstreet)
    print(siteaddresscity+", "+siteaddressstate+"  "+siteaddresszipcode)
    print(networkname)

