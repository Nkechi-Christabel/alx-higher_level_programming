#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId;
      completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
    }
  });
  console.log('{');
  for (const userId in completedTasksByUser) {
    console.log(`  '${userId}': ${completedTasksByUser[userId]},`);
  }
  console.log('}');
});
