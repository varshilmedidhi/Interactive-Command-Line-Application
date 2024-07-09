######################################################################################################################
#
# Computer Project 3:
#
######################################################################################################################

import csv
from operator import itemgetter

# Titles of the columns in the output
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

FORMAT_DATA = "{:>3d}. " + "{:<45.40s} {:<20.18s} " + "{:>11d} " * 4

# ranking parameters -- listed here for easy manipulation
A=1.5
B=-5
C= 5
D=3

MENU = '''\nOptions:
    a - Search and display songs by an artist
    b - display top 20 songs by peak rank
    c - display top 20 songs by weeks on the charts
    d - display top 50 songs by calculated scores
    q - terminate the program'''


PROMPT = "\n:~Enter one of the listed options ~:"
'Invalid option! Try again'
'\n:~Enter a file name ~:'
'Invalid file name; please try again.'
"\n" + " " * 5 + ("{:<45.40s} {:<20.18s} " + "{:>11.9s} " * 4)
'-' * 120

"\nBillboard Top 100"
":~Please enter the name of the artist ~:"
'\n{:d}% of the top 100 songs are {} songs.'
'None of the top 100 songs are by {}.'
"\nThanks for using this program!\nHave a good day!\n"


# Define your functions here

def main():
    pass  # Replace by your code


# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()