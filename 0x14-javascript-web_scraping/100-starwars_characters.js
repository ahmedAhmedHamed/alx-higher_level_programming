#!/usr/bin/node
const requestModule = require('request');

try {
  const requestUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  requestModule(requestUrl, (error, response) => {
    if (error) console.error(error);
    const movie = JSON.parse(response.body);
    movie.characters.forEach(characterUrl => {
      requestModule(characterUrl, (error, response) => {
        if (error) console.error(error);
        const characterDetails = JSON.parse(response.body);
        console.log(characterDetails.name);
      });
    });
  });
} catch (e) {
  console.error(e);
}
