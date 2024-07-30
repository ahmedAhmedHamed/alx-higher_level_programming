#!/usr/bin/node
const requestModule = require('request');
const fs = require('fs');

let bodyToBeWritten;
try {
  const requestUrl = process.argv[2];
  requestModule(requestUrl, (error, response) => {
    bodyToBeWritten = response.body;
    if (error) console.error(error);
    fs.writeFileSync(process.argv[3], bodyToBeWritten, { encoding: 'utf8' });
  });
} catch (e) {
  console.error(e);
}
