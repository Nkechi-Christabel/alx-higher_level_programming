#!/usr/bin/node
const Square5 = require('./5-square.js');

module.exports = class Square extends Square5 {
  charPrint (c) {
    [...(c || 'X').repeat(this.height)].forEach((ch) => console.log(ch.repeat(this.width)));
  }
};
