#!/usr/bin/node

exports.converter = function (base) {
  return function (element) {
    return element.toString(base);
  };
};
