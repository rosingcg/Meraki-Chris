
import time
import provision
import reports

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

from vars import apikey, orgid
import ftpadp
import adpcsvsearch
import provision

#start Menu
#Begining Menu to choose between Running Reports and and Provisioning
def print_menu():
	print (bcolors.BOLD + 30 * "-" , "Stewart Telecom Provisioning" , 30 * "-"+ bcolors.ENDC)
	print ("1. Run Reports")
	print ("2. Provision Systems")
	print ("100. Exit")


def test_report_print_menu():
	print (30 * "-" , "Reporting menu" , 30 * "-")
	print ("11. Meraki Inventory Report")
	print ("12. Meraki Marshall Report")
	print ("100. Exit")

def test_report_loop():
	#JL - removed try, reserve try's for external program handling like APIs, for user interaction, we can
	#	  create specific error handling (called data sanitizing) for user input

	#Run a secondary menu to choose between Specefic Reports
	report_loop=True
	while report_loop:
			test_report_print_menu() #turned into a function
			report_choice = input(bcolors.QUESTION + "Please choose your report:  "+ bcolors.ENDC)
			report_choice = int(report_choice)
			if report_choice==11:
			#Choice 11 is for Meraki Inventory Report.  For now, just print the text Inventory Report
			#Once that report is ran, return back to Report Menu
				print(bcolors.RESULT +"######\nInventory should run\n######"+ bcolors.ENDC)
				time.sleep(1)
			
			elif report_choice==12:
			#Choice 12 is for Meraki Marshal Report.  For now, just print the text Marshal Report
			#Once that report is ran, return back to Report Menu
				print(bcolors.RESULT +"######\nMarshal should run\n#####"+ bcolors.ENDC)
				time.sleep(1)

			elif report_choice==100:
				#break loop and return to main menu
				report_loop=False
				break
			#else:
				#input("Press any key to continue...")

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

	#Ask for selection and change it to an Integer for proper choice selection
	#choice is a variable at this point, since it is the main menu, do I call it main_choice?
	choice = input(bcolors.QUESTION + "Please Enter Your Selection: "+ bcolors.ENDC)
	choice=int(choice) #JL - error handling, what if not a int?   throws error, will change this later
	if choice==1: 
		#test_report_loop()
		reports.report_main()
	elif choice==2:
		print(bcolors.RESULT +"######\nProvision SilverPeak or Meraki\n######"+ bcolors.ENDC)
		provision.meraki_provision()
		time.sleep(1)
	elif choice==100:
		main_loop=False
		break

print('All done')


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
	
