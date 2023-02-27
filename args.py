# Argument Configurations to return this values in all code
# The argument could be changed according to your requirements

# Python Imports
import os
from datetime import datetime

now = datetime.now()
now_str = now.strftime("%Y%m%d-%H%M%S")

# Path to save CSV file
output_csv = os.path.join(os.path.dirname(os.path.realpath(__file__)) + "/csv_files/" + now_str + ".csv")

# More Information http://celestrak.com/NORAD/documentation/gp-data-formats.php
# Define params to get information from http://celestrak.com/
args_celestrak = {
    'url_noradid': "http://celestrak.com/NORAD/elements/gp.php?CATNR=",
    'url_all': "http://celestrak.com/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    }

# A different query could be generated in https://www.space-track.org/#/queryBuilder
# Just put the credentials to access https://www.space-track.org in '###' fields site_cred
args_st = {
    'url_login': "https://www.space-track.org/ajaxauth/login",
    'site_cred': {'identity': "###", 'password': "###"},
    'url_noradid_1': "https://www.space-track.org/basicspacedata/query/class/gp/NORAD_CAT_ID/",
    'url_noradid_2': "/orderby/NORAD_CAT_ID%20asc/emptyresult/show",
    'url_all': "https://www.space-track.org/basicspacedata/query/class/gp/orderby/NORAD_CAT_ID%20asc/emptyresult/show",
    }
