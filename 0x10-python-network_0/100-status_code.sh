#!/bin/bash
# this script displays the size of the body of the response
curl -w "%{http_code}" -so /dev/null "$1"
