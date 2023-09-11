#!/usr/bin/node
// add the process module
const args = require('process').argv;
let arr = args.slice(2);

if (arr.length <= 1) {
  console.log(0);
} else {
  arr = arr.map(Number);
  arr = arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
