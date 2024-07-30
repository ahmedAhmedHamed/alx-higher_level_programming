#!/usr/bin/node
const requestModule = require('request');

try {
  requestModule(process.argv[2], (error, response) => {
    console.log('code: ', response.statusCode);
    if (error) console.error(error);
  });
} catch (e) {
  console.error(e);
}
