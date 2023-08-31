#!/bin/bash
# shows the length of the body using the content-length header
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
