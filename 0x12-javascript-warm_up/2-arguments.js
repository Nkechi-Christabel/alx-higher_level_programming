#!/usr/bin/node

const args = process.argv.length;

if (args < 3) {
  console.log('No argument');
} else {
  console.log(args > 3 ? 'Arguments found' : 'Argument found');
}
