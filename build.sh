#!/usr/bin/env bash

##########################################################################
# This is the bootstrapper script to build and run my script in Docker.
# Feel free to change this file to fit your needs.
##########################################################################

# Define directories.
SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
API_KEY_INSTALLER=$SCRIPT_DIR/assets/install_apikey.sh
DC=`which docker`

echo "Do you wish to install macaddress.io API Key?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) (exec "$API_KEY_INSTALLER"); break;;
        No  ) cat /dev/null > macaddress_io.apikey; break;;
    esac
done

echo "Shall I start building the Docker image?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) $DC build -t check_mac .; echo "Thanks and goodbye!"; rm -rf macaddress_io.apikey; break;;
        No  ) echo "Thanks and goodbye!"; rm -rf macaddress_io.apikey; break;;
    esac
done


