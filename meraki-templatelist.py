from meraki import meraki as mer
from vars import apikey, org
from pprint import pprint
import json
import requests
import re
import pandas as pd
from tabulate import tabulate


templatelist = mer.gettemplates(apikey, org, suppressprint=False)
pprint(templatelist)

