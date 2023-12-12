#!/usr/bin/node
const baseSquare = require('./5-square.js');

module.exports = class Square extends baseSquare {
  charPrint (c = 'X') {
    [...c.repeat(this.height)].forEach(() => console.log(c.repeat(this.width)));
  }
};
