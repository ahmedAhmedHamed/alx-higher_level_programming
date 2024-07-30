#!/usr/bin/node
const request_module = require('request');
const fs = require('fs');


let body_to_be_written = undefined;
try {
    let request_url = process.argv[2];
    request_module(request_url, (error, response) => {
        body_to_be_written = response.body;
        fs.writeFileSync(process.argv[3], body_to_be_written, {encoding: 'utf8'});
    });
}
catch (e) {
  console.error(e);
}
