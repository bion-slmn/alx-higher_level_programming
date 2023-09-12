#!/usr/bin/node

const obj = require('./101-data.js').dict;
const list = Object.keys(obj);
const size = Object.keys(obj).length;

const newObj = {};

for (let i = 0; i < size; i++) {
  const value = obj[list[i]];
  if (newObj[value]) {
    newObj[value].push(list[i]);
  } else {
    newObj[value] = [list[i]];
  }
}
console.log(newObj);
