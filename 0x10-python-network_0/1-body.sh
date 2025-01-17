#!/bin/bash
# This script sends a GET request to the URL and displays the body of the response if status code is 200
curl -s "$1" | grep -Pzo ".*" 
