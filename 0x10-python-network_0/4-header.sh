#!/bin/bash
# sends a get to the url using the header specified
curl -s "$1" -X GET -H "X-School-User-Id: 98"
