adpcode = input('What is the sites ADP code? ')
siteaddressstreet = input('What is address (Number and street)? ')
siteaddresscity = input('What City? ')
siteaddressstate = input('What is the State? ')
siteaddresszipcode = input('What is the Zip Code? ')
friendlyname = input('What is the friendly name for the site? ')
networkname = adpcode+"-"+friendlyname
print('\033[1;31mRed like Radish\033[1;m')
#print ("Thanks for your input, here is your site information:", 'red')
print(siteaddressstreet)
print(siteaddresscity+", "+siteaddressstate+"  "+siteaddresszipcode)
print(networkname)