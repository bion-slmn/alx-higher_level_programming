#!/usr/bin/node
const SquareParent = require('./5-square');

module.exports = class Square extends SquareParent {
  charPrint (c) {
    if (c) {
      const row = c.repeat(this.width);
      for (let i = 0; i < this.width; i++) {
        console.log(row);
      }
    } else {
      super.print();
    }
  }
};
