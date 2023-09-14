#!/usr/bin/node

// read command line args using process module
const args = require('process').argv;
const number = parseInt(args[2]);

if (!number) {
  console.log('Missing size');
} else {
  for (let x = 0; x < number; x++) {
    let row = '';
    for (let y = 0; y < number; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
