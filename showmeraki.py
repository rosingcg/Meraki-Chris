!/usr/bin/env python3

#------------------------------------------------------------------------------------
	# apikeys is a .py file that is in the same directory as this script. setup is meraki="your api key"
import requests
import apikeys
from pprint import pprint

#key=apikeys.meraki
key="b0854ab8f1ef3b9ec0450f793b3086f0fbf93c94"
url="https://dashboard.meraki.com/api/v0/"

main=input("What main function API are you calling? ")
net=input("For what organization or network? " )
info=input("What information are you looking for? ")
dev=input("For a specific serial number/device? ")

headers = {
    'X-Cisco-Meraki-API-Key': key,
    'Content-Type': 'application/json',
}

r=requests.get(url + main + '/' + net + '/' + info, headers=headers)
if r.status_code == requests.codes.ok:
	r.json()
	pprint (r.json())
else:
	print("Something is not right, that pages does not exist. Check your rights and syntax")