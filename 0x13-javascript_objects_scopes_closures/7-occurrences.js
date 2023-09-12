#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(function (element) {
    if (searchElement === element) {
      counter += 1;
    }
  });
  return counter;
};
