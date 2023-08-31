#!/bin/bash
# sends a post the passed url using two variables.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
