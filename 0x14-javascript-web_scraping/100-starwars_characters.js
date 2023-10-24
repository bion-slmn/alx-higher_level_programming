#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const actors = JSON.parse(body).characters;

  for (const x in actors) {
    request(actors[x], (err, resp, body_) => {
      if (err) throw error;
      console.log(JSON.parse(body_).name);
    });
  }
});
