#!/usr/bin/node

const args = require('process').argv;
const number = parseInt(args[2]);

if (!number) {
  console.log(1);
} else {
  function fact (x) {
    if (x === 1) {
      return 1;
    }
    return (x * fact(x - 1));
  }
  console.log(fact(number));
}
