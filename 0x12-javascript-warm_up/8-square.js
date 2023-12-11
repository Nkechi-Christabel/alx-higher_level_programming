#!/usr/bin/node

const arg = parseInt(process.argv[2]);
const arr = Array.from({ length: arg }, () => 'X');

arg ? arr.forEach(ch => console.log(ch.repeat(arg))) : console.log('Missing size');
