#start Menu
def print_menu():
	print (30 * "-" , "Telecom Reports Menu" , 30 * "-")
	print ("1. Meraki Air Marshal Report")
	print ("2. Meraki Inventory Report")
	print ("3. TBD 3")
	print ("4. TBD 4")
	print ("5. TBD 5")
	print ("6. TBD 6")
	print ("7. TBD 7")
	#print ("8. Assign a Device to a Network")
	print ("100. Exit")


#Start Options Loop: info accuracy is important I have not written error handlers yet
def report_main():
	loop=True
	while loop:
		print_menu()
		choice = input("Please Enter Your Selection: ")
		choice=int(choice)
		if choice==1:
			try:
				pass
				#run marshal.py
			except:
				pass

		elif choice==2:
			try:
				pass
				#run Meraki-Inv.py
			except:
				pass



		elif choice==3:
			print ("Retrieving Orginization Network Information")
			dataset = MerakiAPI.getnetworklist(apikey, orgid)
			for row in dataset:
				vlans = MerakiAPI.getvlans(apikey, row['id'])
				try:
					print('VLAN Details for Network ID {0}'.format(str(row['id'])))
					for vlanrow in vlans:
						vlaninfo = MerakiAPI.getvlandetail(apikey, row['id'], vlanrow['id'])
						print(vlaninfo, end='\n')
				except:
					pass
		elif choice==4:
			print('Getting Device Inventory for Network ID - {0}'.format(netid))
			print("-----------------------------------------------------------")
			dataset = MerakiAPI.getnetworkdevices(apikey, netid)
			for row in dataset:
				try:
					pprint.pprint(dataset)
					print("-----------------------------------")
					#print (row, end='\n')
					
				except:
					pass

			option = input("Would you like to export to a file? (y/n)")
			option=str.lower(option)
			if option=="y":
				orig_stdout = sys.stdout
				f = open('Device_Inventory.txt', 'w')
				sys.stdout = f
				pprint.pprint (dataset)
				sys.stdout = orig_stdout
				f.close()
				print ("Your File is Ready!")
				input("Press any key to continue...")

			



			
			

		elif choice==5:
			print('Getting Network Detail for ORG ID - {0}'.format(netid))
			print("-----------------------------------------------------------")
			dataset = MerakiAPI.getnetworkdetail(apikey, netid)
			#for row in dataset:
			#	try:
			#		print("---------------------------------------------------")
			#		print (row)
			#	except:
			#		pass
			len(dataset)
			pprint.pprint(dataset)

		elif choice==6:
			newnet = input("Please enter the value for the new wireless network: ")
			newnet = str(newnet)
			nettype = input("Please enter the network type (Wireless, Switch, Security Appliance)")
			nettype = str(nettype)
			tags = input("Please enter an initial tag for this network")
			tags = str(tags)
			tz = str("EST")
			netinput = MerakiAPI.addnetwork(apikey, orgid, newnet, nettype, tags, tz)
			print("Wireless Network {0}, has been added to ORG ID: {1}".format(str(newnet), str(orgid)))
			pprint.pprint(netinput)

		elif choice==7:
			netinput = MerakiAPI.getnetworktrafficstats(apikey, netid)
			print ("creating output file")
			orig_stdout = sys.stdout
			f = open('traffic_stats.txt', 'w')
			sys.stdout = f
			pprint.pprint (netinput)
			sys.stdout = orig_stdout
			f.close()
			print ("Your File is Ready!")
			input("Press any key to continue...")



		elif choice==100:
			loop=False
			break
		else:
			input("Press any key to continue...")
