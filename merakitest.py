from meraki import meraki as m
from pprint import pprint

#meraki API Key
apikey = "b0854ab8f1ef3b9ec0450f793b3086f0fbf93c94"

#apidata is a variable we are created to return apidata
#apidata = m.myorgaccess(apikey,suppressprint="true")
#print(apidata)
#pprint(apidata)

adpcode = input('What is the sites ADP code? ')
#siteaddressstreet = input('What is address (Number and street)? ')
#siteaddresscity = input('What City? ')
#siteaddressstate = input('What is the State? ')
#siteaddresszipcode = input('What is the Zip Code? ')
friendlyname = input('What is the friendly name for the site? ')
#networkname = adpcode+friendlyname
networkname = adpcode+"-"+friendlyname
#print(adpcode)
#print(siteaddressstreet)
#print(siteaddresscity,siteaddressstate)
print(networkname)