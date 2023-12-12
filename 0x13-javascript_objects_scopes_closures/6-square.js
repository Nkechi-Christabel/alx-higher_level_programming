#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c === undefined ? this.print() : [...c.repeat(this.height)].forEach(() => console.log(c.repeat(this.width)));
  }
};
