# This script will management the terminal Inputs and Outputs
# Print The instructions and control input options

# Project Imports
import celestrak
import space_track


def initial_print():
    print("")
    print("############################################")
    print("  ___  ____  ____    ___   ___    ___   ___  ")
    print(" / __)( ___)(_  _)  / __) / __)  / __) / __) ")
    print("( (__  )__)  _)(_   \__ \ \__ \ ( (__  \__ \ ")
    print(" \___)(____)(____)  (___/ (___/  \___) (___/ ")
    print("")
    print("############################################")

    print("")
    print("# KEPLERIAN FETCHER")
    print("# This Script Get Space Object TLE's")
    print("")


def help_print():
    print("")
    print("General Options:")
    print("     NoraID                     Type NoradID to get TLE from Celestrak")
    print("     NoraID -st                 Type NoradID -st to get TLE from Space-Track")
    print("     -a, -all                   Get all active objects TLE's from Celestrak ")
    print("     -a -st, -all -st           Get all active objects TLE's from Space-Track")
    print("     exit                       Close Application")
    print("")


# Terminal Input
def get_answer():
    check_answer(input("Type NoradID to get TLE or -h to check other options: ").lower())


# Input Options Detail in help_print
def check_answer(answer):
    if answer == "-h":
        help_print()
        get_answer()
    elif answer == "-a" or answer == "-all":
        celestrak.tle_reader(answer)
    elif answer == "-a -st" or answer == "-all -st":
        space_track.tle_reader(answer)
    elif answer[-3:] == "-st":
        space_track.tle_reader(answer)
    elif "-" in answer:
        print("Unrecognized Command!")
        print("")
        get_answer()
    elif answer.strip() == "exit":
        print("Closing Application")
        print("Bye!")
        exit()
    else:
        celestrak.tle_reader(answer)
