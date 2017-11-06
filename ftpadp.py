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

filename = "adp_locations.csv"
ftp = ftplib.FTP("199.253.17.27")
ftp.login(ftpusername,ftppassword)
ftp.cwd("/")
print(bcolors.VARIABLE, filename, bcolors.ACTION, 'will be downloaded.', bcolors.ENDC)
try:
    ftp.retrbinary('RETR %s' % filename, open(filename, 'wb').write)
    print(bcolors.VARIABLE, filename, bcolors.RESULT, 'was downloaded successfully.', bcolors.ENDC)
except:
    print(bcolors.FAIL, "Error", bcolors.ENDC)
    

df = pd.read_csv(filename)

#you can then get whatever cell value you are looking for.  Many ways of doing this :
value_you_want = df.iloc[0][1] # where the cell value you know is in the first row , second column
value_you_want = df.loc[0]['column name'] #notice the change from iloc to loc
value_you_want = df.loc[df['sitecode column']=='sitecode_value']['ip address column'] #searches whole CSV and finds row that
                                          # contains the sitecode_value inside the sitecode column, AND returns the ip address
                                          # column value of that row
