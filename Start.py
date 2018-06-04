from vars import apikey, orgid
import ftpadp
import adpcsvsearch
import provision

#start Menu
#Begining Menu to choose between Running Reports and and Provisioning
def print_menu():
	print (30 * "-" , "Stewart Telecom Provisioning" , 30 * "-")
	print ("1. Run Reports")
	print ("2. Provision Systems")
	print ("100. Exit")
def report_print_menu():
	print (30 * "-" , "Reporting menu" , 30 * "-")
	print ("11. Meraki Organization Inventory Report")
	print ("12. Meraki Marshall Report")
	print ("13. Meraki Client Search in all Networks")
	print ("100. Exit")
def provision_print_menu():
	print (30 * "-" , "Provisioning" , 30 * "-")
	print ("21. Fully Create Meraki Network")
	print ("100. Exit")
def network_lookup_menu():
	print ("1. Update ADP Code List")
	print ("2. Search ADP Codes")
	print ("3. Manual entry")
	print ("0. Return to Meraki Provisioning")

#Start Options Loop: info accuracy is important I have not written error handlers yet
#Loop options to accept Running Reports or Provision Systems
main_loop=True
while main_loop:
	print_menu()
	#Ask for selection(var: main_choice)
	main_choice = int(input("Please Enter Your Selection: "))
	if main_choice==1:
		try:
			#Run a secondary menu to choose between Specefic Reports
			report_loop = True
			while report_loop:
				#run Function to display hte Report Menu
				report_print_menu()
				report_choice = int(input("Please choose your report: "))
				if report_choice == 11:
				#Choice 11 is for Meraki Inventory Report.  For now, just print the text Inventory Report
				#Once that report is ran, return back to Report Menu
					try:
						print("Inventory should run")
						print("Inventory Report complete.  Returning to Reporting menu.")
					except:
						pass
					
				elif report_choice==21:
					#Choice 12 is for Meraki Marshal Report.  For now, just print the text Marshal Report
					#Once that report is ran, return back to Report Menu
					try:
						print("Marshal should run")
						print("Marshal Report complete.  Returning to Reporting menu.")
					except:
						pass
				elif report_choice==100:
						#break loop and return to main menu
						report_loop=False
				else:
					input("Press any key to continue...")
					break

		except:
			pass

	elif main_choice==2:
		try:
			#run provision.py
			#subprocess.Popen("provision.py")
			print("Provision SilverPeak or Meraki")
			provision_loop = True
			while provision_loop:
				#run Function to display the Provision Menu
				provision_print_menu()
				provision_choice = int(input("Please Choose Provisioning Actions: "))
				if provision_choice==21:
					try:
						print("We will now begin creating the Meraki Network, Add devices, Apply templates, etc...")		
						#first, we need to get location information. 
						location_loop = True
						while location_loop:
							network_lookup_menu()
							location_choice = int(input("Please choose site infomration collection method:"))
							if location_choice == 1:
								try:
									ftpadp.getadpcsv()
								except:
									pass
							elif location_choice == 2:
								try:
									adpcsvsearch.adpsearch()
								except:
									pass
							elif location_choice == 3:
								try:
									provision.manual_network_location()
								except:
									pass
							elif location_choice == 0:
								try:
									break
								except:
									pass
							else:
								#invalid entry should repeat the Merkai Provision Menu
								input("Invalid entry.  Press any key to continue...")
					#Continue to Meraki network Provisioning


						print("Provision Meraki Network is now complete.  Returning to Provisioning menu.")
					except:
						pass
				elif provision_choice==100:
					try:
						#break loop and return to main menu
						provision_loop=False
					except:
						pass
				else:
					try:
						input("Press any key to continue...")
						#Do I need a break here?  Should I set the loop to false now?  But i want it to return to asking provisioning menu questions
						provision_loop=False
						break
					except:
						pass
		except:
			pass
	elif main_choice==100:
		break
	else:
		print ("Invalid Selection, please try again")
	
	
