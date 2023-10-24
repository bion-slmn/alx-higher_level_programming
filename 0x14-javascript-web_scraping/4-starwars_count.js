#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  const jResp = JSON.parse(body);
  const userUrl = jResp.results[0].characters[0].replace(/\d+/, 18);

  request(userUrl, (error, response, body) => {
    if (error) throw error;
    const resp = JSON.parse(body);
    console.log(resp.films.length);
  });
});
