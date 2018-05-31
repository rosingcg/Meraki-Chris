from meraki import meraki as m
from vars import ftpusername, ftppassword
from pprint import pprint
import ftplib
import pandas as pd

class bcolors:
    QUESTION = '\033[95m'
    ACTION = '\033[94m'
    VARIABLE = '\033[92m'
    RESULT = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[33m'

#define ADP FTP of CSV File
def getadpcsv():
    filename = "adp_locations.csv"
    ftp = ftplib.FTP("199.253.17.27")
    ftp.login(ftpusername,ftppassword)
    ftp.cwd("/")
    print(bcolors.VARIABLE, filename, bcolors.ACTION, 'will be downloaded.', bcolors.ENDC)
    try:
        ftp.retrbinary('RETR %s' % filename, open(filename, 'wb').write)
        print(bcolors.VARIABLE, filename, bcolors.RESULT, 'was downloaded successfully.', bcolors.ENDC)
        return filename
    except:
        print(bcolors.FAIL, 'Error', bcolors.ENDC)
        return 'Error'
    

