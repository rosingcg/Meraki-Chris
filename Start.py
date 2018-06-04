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

	
