#!/usr/bin/node
const requestModule = require('request');

async function main () {
  try {
    const requestUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
    await requestModule(requestUrl, async (error, response) => {
      if (error) console.error(error);
      const movie = JSON.parse(response.body);
      for (const characterUrl of movie.characters) {
        await requestModule(characterUrl, (error, response) => {
          if (error) console.error(error);
          const characterDetails = JSON.parse(response.body);
          console.log(characterDetails.name);
        });
        setTimeout(() => {}, 200);
      }
    });
  } catch (e) {
    console.error(e);
  }
}

main();
