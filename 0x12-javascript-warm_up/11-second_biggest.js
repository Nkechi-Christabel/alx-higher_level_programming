#!/usr/bin/node

const args = process.argv.slice(2);
console.log(args.length > 1 ? args.sort((a, b) => b - a)[1] : 0);
