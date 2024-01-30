#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';
let count = 0;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;

  films.forEach(film => {
    film.characters.forEach(ch => {
      if (ch.includes(characterId)) count++;
    });
  });
  console.log(count);
});
