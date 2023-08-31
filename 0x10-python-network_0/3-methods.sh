#!/bin/bash
# displays all http methods available from the url in $1
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
