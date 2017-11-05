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

print(bcolors.HEADER,'Now we need to give it a name and Street Address', bcolors.ENDC)
addressstreet = input(bcolors.QUESTION + 'What is the Street Address?  (Do not include Suite number): ' + bcolors.ENDC)
addresscity = input(bcolors.QUESTION + 'What City? : '+ bcolors.ENDC)
addressstate = input(bcolors.QUESTION + 'What State (2 Letters, Capitalized): ' + bcolors.ENDC)
addresszip = input(bcolors.QUESTION +'Zip Code? : '+ bcolors.ENDC)
fulladdress = addressstreet + "\n" + addresscity + ', ' + addressstate + ' ' +addresszip
print(fulladdress)

