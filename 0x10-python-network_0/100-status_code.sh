#!/bin/bash
# It sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sI "$1" | head -n 1 | grep -oE '[0-9]{3}'
