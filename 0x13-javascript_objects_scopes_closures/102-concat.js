#!/usr/bin/node

const fs = require('fs');
const [src1, src2, dest] = process.argv.slice(2);

function callback (err, data) {
  if (err) throw err;

  fs.appendFile(dest, data, function (err) {
    if (err) throw err;
  });
}

fs.readFile(src1, 'utf8', callback);

fs.readFile(src2, 'utf8', callback);
