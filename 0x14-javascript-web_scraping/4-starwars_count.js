#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) throw error;

  const result = JSON.parse(body).results;
  console.log(result.reduce((count, movie) => {
    if (movie.characters.find((character) => character.endsWith('/18/'))) {
      count += 1;
    }
    return count;
  }, 0));
});
