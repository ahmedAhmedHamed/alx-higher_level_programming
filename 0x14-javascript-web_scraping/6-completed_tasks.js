#!/usr/bin/node
const requestModule = require('request');

try {
  const requestUrl = process.argv[2];
  requestModule(requestUrl, (error, response) => {
    if (error) console.error(error);
    const requestJson = JSON.parse(response.body);
    const numTasksCompletedPerUser = {};
    requestJson.forEach(taskDetails => {
      const userId = taskDetails.userId;
      const completionStatus = taskDetails.completed;
      if (completionStatus) {
        if (userId in numTasksCompletedPerUser) {
          numTasksCompletedPerUser[userId]++;
        } else {
          numTasksCompletedPerUser[userId] = 1;
        }
      }
    });
    console.log(numTasksCompletedPerUser);
  });
} catch (e) {
  console.error(e);
}
