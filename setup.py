#install bcolors
#pip install bcolors
#install meraki
#pip install meraki
#install tabulate
#pip install tabulate
#install pandas
#pip install pandas
#update pip
#python -m pip install --upgrade pip

"""#!/usr/bin/env python
https://stackoverflow.com/questions/6457794/pip-install-r-continue-past-installs-that-fail
pipreqs.py: run ``pip install`` iteratively over a requirements file.

def main(argv):
    try:
        filename = argv.pop(0)
    except IndexError:
        print("usage: pipreqs.py REQ_FILE [PIP_ARGS]")
    else:
        import pip
        retcode = 0
        with open(filename, 'r') as f:
            for line in f:
                pipcode = pip.main(['install', line.strip()] + argv)
                retcode = retcode or pipcode
        return retcode
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))
    """