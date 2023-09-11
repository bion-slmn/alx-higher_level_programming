#!/usr/bin/node

const args = require('process').argv;

const first = parseInt(args[2]);
const second = parseInt(args[3]);

function add (a, b) {
  return a + b;
}

console.log(add(first, second));
