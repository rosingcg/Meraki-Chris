from meraki import meraki
from pprint import pprint
from vars import apikey

#apidata is a variable we are created to return apidata
meraki_orgaccess = meraki.myorgaccess(apikey,suppressprint="true")
#print(meraki_orgaccess)
pprint(meraki_orgaccess)
