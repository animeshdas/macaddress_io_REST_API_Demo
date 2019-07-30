#!/usr/bin/env python

# Script: check_mac.py
# Name: DEMO REST API CLIENT
# Description: 	Simple REST client to query macaddress.io API
#              	services to query for the company associated 
# 			   	with the given mac address. 
# Version: 0.1
# License: MIT 
# GitHub: 
# Mode of operation: CLI
# Tested on: CentOS Linux 7.4 with python v2.x
# Author: Animesh Das 
# Email: jobs4ani@gmail.com
##########################################
# Release History: 
#   30-Jul-2019 - First initial release.
##########################################

# importing the requests library 
import sys
import requests
import json

# api-endpoint 
URL = "https://api.macaddress.io/v1"

# Read Macaddress.io API Key
with open('macaddress_io.apikey', 'r') as f:
    API_KEY = f.read().strip()

# Output Type
output="json"


# Set timeout in seconds
timeout=3

# Show banner & 
# Inform the user of the macaddress format we are gonna accept. This is just to save time
# to avoid writing additional validation code for macaddress format validation. 
print """
------------------------------------------------
              - MACADDRESS.IO -
          DEMO REST API CLIENT v0.1
------------------------------------------------
This small little script is to demonstrate a
simple REST client to query macaddress.io API. 
Please register with macaddress.io to get your
own API KEY. It needs to be added in API_KEY. 

No validation or checks has been performed due 
time constraint. Please use the script at your 
own risk.

Author: Animesh Das 
Email: jobs4ani@gmail.com
Version: 0.1
License: MIT
------------------------------------------------
NOTE: This script currently support macaddress
in six groups of two separated by colons (:), 
for example 44:38:39:ff:ef:57
~~
"""

# Ask macaddress from user
macaddress = raw_input("Please enter the macaddress to query : ")

PARAMS = {'apiKey':API_KEY, 'output':output, 'search':macaddress}



def chk_res_code(argument):
    switcher = {
        400: "Invalid parameters.",
        401: "Access restricted. Enter the correct API key.",
        402: "Access restricted. Check the credits balance.",
        422: "Invalid MAC or OUI address was received. Check https://macaddress.io/faq/what-is-the-structure-of-a-mac-address",
        429: "Too many requests. Try your call again later.",
        500: "Internal server error. Try your call again or contact us."
    }
    return switcher.get(argument, "Unknown error occured!")


# Handle request connection and exceptions
try:
	# Sending in GET request and save the response as response object 
    r = requests.get(url = URL, params = PARAMS, timeout=(timeout, timeout + 25)) 
except requests.exceptions.Timeout:
    print "Network timed out to reach the server."
    sys.exit(1)
except requests.exceptions.TooManyRedirects:
    print "Bad URL : " + URL + ". Received redirects."
    sys.exit(1)
except requests.exceptions.ConnectionError:
	print "Connection Error. Please check your network connection."
	sys.exit(1)
except requests.exceptions.RequestException as e:
    # Some unknown error. Print the error and exit.
    print e
    sys.exit(1)

# Check response code and in case of non 200, display appropiate text error of macaddress.io response codes.  
if r.status_code != 200:
    print (chk_res_code(r.status_code)); sys.exit(1)

# Handle json data parsing exceptions.
try:
	# extracting data in json format 
    data = r.json()
    company=data['vendorDetails']['companyName'] # Retreive companyName
    print "The company associated with MAC address " + macaddress + " is : " + company # Print details.
except ValueError:  # includes simplejson.decoder.JSONDecodeError
    print "Invalid JSON data received! Decoding of JSON has failed" # Throw JSON error.
except Exception as e:
    print "An exceptions has occured while parsing the JSON data, following is the details:\n %s" % str(e)