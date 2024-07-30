#!/usr/bin/node
const requestModule = require('request');

try {
  const requestUrl = process.argv[2];
  requestModule(requestUrl, (error, response) => {
    if (error) console.error(error);
    const movies = JSON.parse(response.body).results;
    let characterAppearanceCounter = 0;
    const searchedCharacter = '18';
    movies.forEach(movie => {
      movie.characters.forEach(characterUrl => {
        const trimmedUrl = characterUrl.endsWith('/')
          ? characterUrl.slice(0, -1)
          : characterUrl;
        const parts = trimmedUrl.split('/');
        const number = parts[parts.length - 1];
        if (number === searchedCharacter) { ++characterAppearanceCounter; }
      });
    });
    console.log(characterAppearanceCounter);
  });
} catch (e) {
  console.error(e);
}
