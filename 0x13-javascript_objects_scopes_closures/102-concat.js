#!/usr/bin/node

const fs = require('fs');
const args = require('process').argv;

let content = '';
fs.readFile(args[2], 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  content += data;

  fs.readFile(args[3], 'utf-8', function (err, data) {
    if (err) {
      console.error(err);
      return;
    }
    content += data;

    fs.writeFile(args[4], content, function (err) {
      if (err) {
        console.error(err);
      }
    });
  });
});
