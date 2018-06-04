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
        break
    
    #friendlyname = input('What is the friendly name for the site? ')    
    while True:
        friendlyname = input(bcolors.QUESTION + 'What is the friendly name for the site? ' + bcolors.ENDC )

    while not re.match("^[A-Za-z_]{0,25}$", friendlyname):
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
        friendlyname = input(bcolors.QUESTION + 'What is address (Number and street)? '+ bcolors.ENDC )
    else:
        print("Site address is:  "+ siteaddressstate)
        break
    
    #Site Address: City
    while True:
        siteaddresscity = input(bcolors.QUESTION + 'What City? ' + bcolors.ENDC )
    
    while not re.match("^[A-Za-z_]{0,25}$", siteaddresscity):
        print (bcolors.FAIL,"Error! Invalid Site Name.  Can only contain Uppercase, Lowercase, and underscores.  It also can't be longer than 25 characters.",bcolors.ENDC)
        friendlyname = input(bcolors.QUESTION + 'What City?  '+ bcolors.ENDC )
    else:
        print("Site city is:  "+ siteaddresscity)
        break

    
    siteaddressstate = input('What is the State? ')
    siteaddresszipcode = input('What is the Zip Code? ')
   

    networkname = adpcode+"-"+friendlyname
    print('\033[1;31mRed like Radish\033[1;m')
    #print ("Thanks for your input, here is your site information:", 'red')
    print(siteaddressstreet)
    print(siteaddresscity+", "+siteaddressstate+"  "+siteaddresszipcode)
    print(networkname)