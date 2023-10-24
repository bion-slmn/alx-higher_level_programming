#!/usr/bin/node

// this script reads and prints the content of a file.
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', function (err, data) {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
