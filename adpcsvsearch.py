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


def adpsearch():
    #Dataframes for panda to read CSV
    df = pd.read_csv(adp_locations.csv)

    adpcodesearch = input('What ADP Code are you searching on? ')
    #you can then get whatever cell value you are looking for.  Many ways of doing this :
    #value_you_want_cell_A2 = df.iloc[0][1] # where the cell value you know is in the first row , second column
    #value_you_want = df.loc[0]['Location Code'] #notice the change from iloc to loc, return the value of row 0 under the column locatoin code
    adpstreet = df.loc[df['Location Code']==adpcodesearch]['Street'] #searches whole CSV and finds row that
                                            # contains the sitecode_value inside the sitecode column, AND returns the ip address
                                            # column value of that row
    print('The Street addresss for ',adpcodesearch,'is ',adpstreet)    
    adpresults = df[df['Location Code']==adpcodesearch]
    print(adpresults)
    fulladdress = adpresults.iloc[0][3] + ', ' + adpresults.iloc[0][4] + ', ' + adpresults.iloc[0][5] + ' ' + adpresults.iloc[0][6]
    print(fulladdress)
    fulladdressv2 = adpresults.iloc[0]['Street'] + ', ' + adpresults.iloc[0]['City'] + ', ' + adpresults.iloc[0]['State'] + ' ' + adpresults.iloc[0]['Zip']
    print(fulladdressv2)
