#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    [...(c || 'X').repeat(this.height)].forEach((ch) => console.log(ch.repeat(this.width)));
  }
};
