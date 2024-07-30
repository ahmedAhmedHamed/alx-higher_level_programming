#!/usr/bin/node
const request_module = require('request');


try {
    let request_url = process.argv[2];
    request_module(request_url, (error, response) => {
        let req_json = JSON.parse(response.body);
        let num_tasks_completed_per_user = {};
        req_json.forEach(task_details => {
            let user_id = task_details["userId"];
            let completion_status = task_details["completed"];
            if (completion_status) {
                if (num_tasks_completed_per_user.hasOwnProperty(user_id)) {
                    num_tasks_completed_per_user[user_id]++;
                } else {
                    num_tasks_completed_per_user[user_id] = 1;
                }
            }
        });
        console.log(num_tasks_completed_per_user);
    });
}
catch (e) {
  console.error(e);
}
