#!/usr/bin/node
const request_module = require('request');

async function main() {
    try {
        let request_url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
        await request_module(request_url, async (error, response) => {
            let movie = JSON.parse(response.body);
            for (const character_url of movie['characters']) {
                await request_module(character_url, (error, response) => {
                    let character_details = JSON.parse(response.body);
                    console.log(character_details["name"]);
                });
            }
        });
    }
    catch (e) {
        console.error(e);
    }
}


main();
