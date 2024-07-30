#!/usr/bin/node
const requestModule = require('request');

try {
  requestModule(process.argv[2], (response) => { console.log(response.statusCode); });
} catch (e) {
  console.error(e);
}
