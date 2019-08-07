#!/usr/bin/env python3

# imports
import requests 
import argparse
import sys

# gettting api url as argument  
parser = argparse.ArgumentParser(description='Getting API URL')
parser.add_argument('url', type=str, help='API URL for listing services')
args = parser.parse_args()

# getting api payload
try:
    r = requests.get(args.url, timeout=30)
    data = r.text.split("<br />")
    print("The following services are NOT OK:\n")
# searching for non "OK" Services
    for line in data:
        if len(line) and " OK" not in line:
            service=line.split(":")
            print("The Service {} is{}".format(service[0], service[1]))
except Exception as e:
    print("Error while fetching API data.\nError message: {}".format(e))
    sys.exit(1)
