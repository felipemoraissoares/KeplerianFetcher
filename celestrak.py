# Python Script to obtain data of objects in space orbit from http://celestrak.com/
# The information is acquired at http://celestrak.com/NORAD/documentation/gp-data-formats.php
# The Query information and outputs files can be changed in args.py

# Python Imports
import requests

# Project Imports
from args import args_celestrak
from tle_detach import detach


# Function to get TLE from Celestrak
def tle_reader(answer):
    # Input Check and get url from args.py
    if answer == "-a" or answer == "-all":
        url = args_celestrak['url_all']
    else:
        url = args_celestrak['url_noradid'] + answer

    print(f"Get information from: {url}")

    # Request data from Celestrak Website
    data = requests.get(url)
    data_lines = data.text.split('\n')

    aux_list = []
    tle_list = []

    # The information of a TLE is contained every 3 lines, for example:
    # Line 0 = Object Name
    # Line 1 = TLE Line 1
    # Line 2 = TLE Line 2

    # Thus, data will be Separated each 3 lines
    aux = 0
    for line in data_lines:
        line = line.strip()
        if aux < 3:
            aux_list.append(line)
        else:
            tle_list.append(aux_list)
            aux_list = [line]
            aux = 0
        aux += 1

    print(f"Total of {len(tle_list)} objects...")

    # Function to detach TLE lines
    if not tle_list:
        print(f"NoradID: {answer} does not return any data!")
    else:
        detach(tle_list)

    print("Completed session")

