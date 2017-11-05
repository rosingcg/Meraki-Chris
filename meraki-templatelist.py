from meraki import meraki as mer
from vars import apikey, orgid
from pprint import pprint
import json
import requests
import re
import pandas as pd
from tabulate import tabulate


templatelist = mer.gettemplates(apikey, orgid, suppressprint=False)
pprint(templatelist)

