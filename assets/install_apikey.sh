#/usr/bin/env bash
# Ask for API Key.
echo -n "Please enter you macaddress.io API Key : "
read answer
echo $answer > macaddress_io.apikey
echo "macaddress.io API Key has been installed."
