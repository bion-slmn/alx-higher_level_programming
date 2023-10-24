#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const userId = 18;

request(url, (error, response, body) => {
  if (error) throw error;
  const jResp = JSON.parse(body);
  const userUrl = jResp.results[0].characters[0].replace(/\d+/, userId);

  request(userUrl, (error, response, body) => {
    if (error) throw error;
    const resp = JSON.parse(body);
    console.log(resp.films.length);
  });
});
