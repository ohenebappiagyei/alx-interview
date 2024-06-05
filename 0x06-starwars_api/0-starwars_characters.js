#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`

if (!movieId) {
    console.error('Please provide a Movie ID');
    process.exit(1);
}

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
        return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach(characterUrl => {
        request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
                console.error(charError);
                return;
            }
            if (charResponse.statusCode !== 200) {
                console.error(`Failed to fetch character data. Status code: ${charResponse.statusCode}`);
                return;
            }

            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
        });
    });
});