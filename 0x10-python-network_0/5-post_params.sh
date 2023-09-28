#!/bin/bash
# posting with variable in the body
curl -s -X POST -d "email=test@gmail.com&message=I will always be here for PLD" "$1"
