print('\033[92m Creating network with the name of \n \033[0m')
print('Back to normal')


#bcolor class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER + "Header: Color 95,Magenta" + bcolors.ENDC)
print(bcolors.OKBLUE + "OKBLUE: Color 94, Blue" + bcolors.ENDC)
print(bcolors.OKGREEN + "OKGREEN: Color 92, Teal" + bcolors.ENDC)
print(bcolors.WARNING + "WARNING: Color 93, yellow" + bcolors.ENDC)
print(bcolors.FAIL + "FAIL: Color 93, Red" + bcolors.ENDC)
print(bcolors.ENDC + "ENDC: Color 0, White" + bcolors.ENDC)
print(bcolors.BOLD + "BOLD: Color 1, Bold" + bcolors.ENDC)
print(bcolors.UNDERLINE + "Underline: Color 4, Underline, " + bcolors.ENDC)


#Color Class
class colors:
    '''Colors class:
    reset all colors with colors.reset
    two subclasses fg for foreground and bg for background.
    use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'