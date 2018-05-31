from functions import functions

#start Menu
#Begining Menu to choose between Running Reports and and Provisioning
def print_menu():
	print (30 * "-" , "Stewart Telecom Provisioning" , 30 * "-")
	print ("1. Run Reports")
	print ("2. Provision Systems")
	print ("100. Exit")


#Start Options Loop: info accuracy is important I have not written error handlers yet
#Loop options to accept Running Reports or Provision Systems
main_loop=True
while main_loop:
	print_menu()
	#Ask for selection and change it to an Integer for proper choice selection
	#choice is a variable at this point, since it is the main menu, do I call it main_choice?
	choice = input(functions.bcolors.QUESTION + "Please Enter Your Selection: "+ functions.bcolors.ENDC)
	choice = int(choice)
	if choice==1:
		try:
			#Run a secondary menu to choose between Specefic Reports
			def report_print_menu():
				print (30 * "-" , "Reporting menu" , 30 * "-")
				print ("11. Meraki Organization Inventory Report")
				print ("12. Meraki Marshall Report")
				print ("13. Meraki Client Search in all Networks")
				print ("100. Exit")
			report_loop = True
			while report_loop:
					report_print_menu
					report_choice = input("Please choose your report")
					report_choice = int(report_choice)
					if report_choice==11
					#Choice 11 is for Meraki Inventory Report.  For now, just print the text Inventory Report
					#Once that report is ran, return back to Report Menu
						try:
							print("Inventory should run")
						except:
							pass
					
					if report_choice==12
					#Choice 12 is for Meraki Marshal Report.  For now, just print the text Marshal Report
					#Once that report is ran, return back to Report Menu
						try:
							print("Marshal should run")
						except:
							pass
					elif report_choice==100:
						#break loop and return to main menu
						report_loop=False
						break
							else:
							input("Press any key to continue...")


			except:
				pass

	elif choice==2:
		try:
			#run provision.py
			#subprocess.Popen("provision.py")
			print("Provision SilverPeak or Meraki")
		except:
			pass

	
