# Project CEI SSCS
# Author: Felipe de Morais Soares
# github.com/felipemoraissoares/
# Python project to obtain TLE of objects in space orbit from Celestrak and Space-Track
# The operating instructions will be detailed in the respective scripts
# The TLe's will be detached according to https://celestrak.com/columns/v04n03/ instructions
# This data will be saved in a csv file or MySQL Database according to input option

# Project Imports
from terminal_settings import initial_print, get_answer

if __name__ == '__main__':
    initial_print()
    get_answer()
