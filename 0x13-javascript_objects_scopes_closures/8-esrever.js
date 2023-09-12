#!/usr/bin/node
// reversing using unshift
exports.esrever = function (list) {
  const reversed = [];
  list.forEach(function (element) {
    reversed.unshift(element);
  });
  return reversed;
};
