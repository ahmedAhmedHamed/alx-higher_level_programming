#!/usr/bin/node
const request_module = require('request');

try {
    let request_url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];
    request_module(request_url, (error, response) => {
        console.log(JSON.parse(response.body)['title'])
    });
}
catch (e) {
  console.error(e);
}
