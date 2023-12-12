#!/usr/bin/node
const baseSquare = require('./5-square.js');

module.exports = class Square extends baseSquare {
  charPrint (c) {
    [...(c || 'X').repeat(this.width)].forEach((ch) => console.log(ch.repeat(this.height)));
  }
};
