#!/usr/bin/node
const request_module = require('request');

try {
  request_module(process.argv[2], (error, response) => {console.log(response.statusCode)});
}
catch (e) {
  console.error(e);
}
