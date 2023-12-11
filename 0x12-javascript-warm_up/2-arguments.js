#!/usr/bin/node

const argLen = process.argv.length;

if (argLen < 3) {
  console.log('No argument');
} else {
  console.log(argLen > 3 ? 'Arguments found' : 'Argument found');
}
