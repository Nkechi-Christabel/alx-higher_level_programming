#!/usr/bin/node

const { argv } = require('node:process');
const argLen = argv.length;

if (argLen < 3)
    console.log('No argument')
else if (argLen === 3)
    console.log('Argument found');
else
    console.log('Arguments found');
   
