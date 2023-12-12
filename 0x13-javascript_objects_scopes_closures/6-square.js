#!/usr/bin/node
const baseSquare = require('./5-square.js');

module.exports = class Square extends baseSquare {
  charPrint (c) {
    [...(c || 'X').repeat(this.height)].forEach((ch) => console.log(ch.repeat(this.width)));
  }
};
