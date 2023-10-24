#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, response, body) => {
  if (error) throw error;
  const jResp = JSON.parse(body);
  console.log(jResp.title);
});
