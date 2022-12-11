import requests
import sys

SUBLIST = open("wordlist.txt").read()
directories = SUBLIST.splitlines()

for dir in directories:
    dir_enum = f"https://{sys.argv[1]}/{dir}.html"
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("Valid directory : ", dir_enum)