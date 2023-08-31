#!/bin/bash
# sends a delete response to the url in the first argument
curl -s "$1" -X DELETE
