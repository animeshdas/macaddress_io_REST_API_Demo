#!/usr/bin/env bash

##########################################################################
# This is the bootstrapper script to build and run my script in Docker.
# Feel free to change this file to fit your needs.
##########################################################################

# Define directories.
DC=`which docker`
# run image
$DC run -ti check_mac /bin/bash -c "cd /Demo; python check_mac.py"