#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const actors = JSON.parse(body).characters;

  actors.reduce((promiseChain, actorUrl) => {
    return promiseChain.then(() => {
      return new Promise((resolve, reject) => {
        request(actorUrl, (err, resp, body_) => {
          if (err) reject(err);
          else {
            console.log(JSON.parse(body_).name);
            resolve();
          }
        });
      });
    });
  }, Promise.resolve());
});
