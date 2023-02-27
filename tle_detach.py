# This Script detaches TLE's from celestrak.py and space_track.py
# The instructions in https://celestrak.com/columns/v04n03/ were followed to separate the Lines positions

# Python Imports
import pandas as pd

# Project Import
from args import output_csv
from database import to_database


# Function to detach TLE, received a List of TLE's
def detach(tle_list):
    tle_list_detach = []
    for item in tle_list:
        objname = item[0].strip()
        line1 = item[1].strip()
        line2 = item[2].strip()

        # Detach Line1
        noradid = line1[2:7]
        classification = line1[7]
        designator = line1[9:17]
        epoch_year = line1[18:20]
        epoch_day = line1[20:32]
        fstder = line1[33:43]
        sndder = line1[44:52]
        bdrag = line1[53:61]
        eltype = line1[62]
        elset = line1[64:68]

        # Detach Line2
        inclination = line2[8:16]
        ascend_mode = line2[17:25]
        eccentricity = line2[26:33]
        perigee = line2[34:42]
        mean_anomaly = line2[43:51]
        mean_motion = line2[52:63]
        revolution = line2[63:68]

        tle_line = (objname, line1, line2, noradid, classification, designator,
                    epoch_year, epoch_day, fstder, sndder, bdrag, eltype, elset,
                    inclination, ascend_mode, eccentricity, perigee, mean_anomaly,
                    mean_motion, revolution)

        tle_list_detach.append(tle_line)
    # end for

    # Create a pandas dataframe to export csv
    df_tle = pd.DataFrame(tle_list_detach, columns=['ObjectName', 'Line1', 'Line2', 'NoradID', 'Classification',
                                                    'Designator', 'EpochYear', 'EpochDay', 'FstMeanDer',
                                                    'SndMeanDer', 'BDrag', 'ElSetTyme', 'ElementNumber',
                                                    'Inclination', 'RightAscension', 'Eccentricity', 'Perigee',
                                                    'MeanAnomaly', 'MeanMotion', 'Revolution'])

    # Change output in args.py
    try:
        df_tle.to_csv(output_csv)
        print(f"Information Saved in {output_csv}")
    except Exception as error:
        print(error)

    # If it needs, uncomment this section to save information in database
    # Function to save data in MySQL is in database.py
    '''
    try: 
        to_database(df_tle)
    except Exception as error:
        print(error)
    '''
