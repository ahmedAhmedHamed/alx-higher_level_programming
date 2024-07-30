#!/usr/bin/node
const request_module = require('request');

try {
    let request_url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
    request_module(request_url, (error, response) => {
        let movie = JSON.parse(response.body);
        movie['characters'].forEach(character_url => {
            request_module(character_url, (error, response) => {
                let character_details = JSON.parse(response.body);
                console.log(character_details["name"]);
            });
        })
    });
}
catch (e) {
  console.error(e);
}
