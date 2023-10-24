#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
    if (err) throw err;
  });
});
