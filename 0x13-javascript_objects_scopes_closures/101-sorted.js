#!/usr/bin/node

const { dict } = require('./101-data');

const userIdsByOccurrence = {};
for (const occurrence in dict) {
  const id = dict[occurrence];
  const previousValue = userIdsByOccurrence[id] ?? [];
  userIdsByOccurrence[id] = [...previousValue, occurrence];
}
console.log(userIdsByOccurrence);
