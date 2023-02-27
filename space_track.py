# Python Script to obtain data of objects in space orbit from www.space-track.org
# The information is acquired from a set query made at https://www.space-track.org/#/queryBuilder
# The results are the latest TLE's, in Json format
# The site credentials, query information and outputs files can be changed in args.py

# Python Imports
from datetime import time
import requests
import json

# Project Imports
from args import args_st
from tle_detach import detach


# Class to Raise Exception when Request error
class MyError(Exception):
    def __init___(self, args):
        Exception.__init__(self, f"my exception was raised with arguments {args}")
        self.args = args


# Function to get TLE from Space-Track
def tle_reader(answer):
    with requests.Session() as session:

        # Space-Track needs site credentials to access information
        resp = session.post(args_st['url_login'], data=args_st['site_cred'])
        if resp.status_code != 200:
            raise MyError(resp, "POST fail on login")

        # Input Check and get url from args.py
        if answer == "-a -st" or answer == "-all -st":
            url = args_st['url_all']
            resp = session.get(args_st['url_all'])
        else:
            url = args_st['url_noradid_1'] + answer + args_st['url_noradid_2']
            resp = session.get(args_st['url_noradid_1'] + answer + args_st['url_noradid_2'])

        print(f"Get information from: {url}")

        if resp.status_code != 200:
            print(resp)
            raise MyError(resp, "GET fail on request for Starlink satellites")

        # Use the json package to break the json formatted response text into a list of dictionaries
        api_data = json.loads(resp.text)
        print(f"Total of {len(api_data)} objects...")

        tle_list = []

        # Json Information bring TLE already in separated fields
        # Although this script get TLE lines and separates fields with its own function

        maxs = 1  # Use to snoozing download when necessary
        for element in api_data:
            # save each object in a list
            tle_list.append([element['OBJECT_NAME'], element['TLE_LINE1'], element['TLE_LINE2']])

            """
            # In case the amount of data is too large, due to the rate limit reasons
            # There is a possibility of the user receiving some blockage due to the amount of data
            # If necessary, uncomment this section to snoozing download 
            maxs += 1
            if maxs > 200:
                print("Snoozing for 60 secs for rate limit reasons (max 20/min and 200/hr)...")
                time.sleep(60)
                maxs = 1
            """

        # Function to detach TLE lines
        if not tle_list:
            print(f"NoradID: {answer} does not return any data!")
        else:
            detach(tle_list)

        print("Completed session")
        session.close()
