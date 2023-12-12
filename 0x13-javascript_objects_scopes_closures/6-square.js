#!/usr/bin/node
const Square5 = require('./5-square.js');

module.exports = class Square extends Square5 {
  charPrint(c) {
    const charactersArray = [...(c || 'X').repeat(this.height)];
    charactersArray.forEach((ch) => console.log(ch.repeat(this.width)));
  }
};

