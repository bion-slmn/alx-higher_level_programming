#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  const todo = JSON.parse(body);
  const todoComplete = {};
  for (const i in todo) {
    if (todo[i].completed) {
      if (todoComplete[todo[i].userId]) {
        todoComplete[todo[i].userId] += 1;
      } else {
        todoComplete[todo[i].userId] = 1;
      }
    }
  }
  console.log(todoComplete);
});
