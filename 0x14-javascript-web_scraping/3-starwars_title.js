#!/usr/bin/node
const requestModule = require('request');

try {
  const requestUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  requestModule(requestUrl, (error, response) => {
    console.log(JSON.parse(response.body).title);
    if (error) console.error(error);
  });
} catch (e) {
  console.error(e);
}
