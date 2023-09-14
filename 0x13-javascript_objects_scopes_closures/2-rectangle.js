#!/usr/bin/node
// creating rectangle class
module.exports = class Rectangle {
  constructor (w, h) {
    // creating an empty class if w or h <= 0
    if (w > 0 && h > 0 && !isNaN(w) && !isNaN(h)) {
      this.width = w;
      this.height = h;
    }
  }
};
