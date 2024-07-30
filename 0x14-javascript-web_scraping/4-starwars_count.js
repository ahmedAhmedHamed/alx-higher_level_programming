#!/usr/bin/node
const request_module = require('request');

try {
    let request_url = process.argv[2];
    request_module(request_url, (error, response) => {
        let movies = JSON.parse(response.body)['results'];
        let character_appearance_counter = 0;
        let searched_character = "18";
        movies.forEach(movie => {
            movie['characters'].forEach(character_url => {
                const trimmedUrl = character_url.endsWith('/')
                    ? character_url.slice(0, -1) : character_url;
                const parts = trimmedUrl.split('/');
                const number = parts[parts.length - 1];
                if (number === searched_character)
                    ++character_appearance_counter;
            })
        });
        console.log(character_appearance_counter);
    });
}
catch (e) {
  console.error(e);
}
