#!/bin/bash
# It takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
curl -sLH "X-School-User-Id: 98" "$1"
