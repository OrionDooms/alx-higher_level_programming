#!/usr/bin/node
const StarWar = require('request');
const url = process.argv[2];
let count = 0;

StarWar.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body);
    films.results.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  }
});
