#!/usr/bin/node
import { argv } from 'node:process';

if (!argv[2])
  console.log(0);
else if (argv[2] && !argv[3])
  console.log(1)
else {
  let smallest = 2
  let secondSmallest = 2
  for (let i = 2; i < argv.length -1; i++) {
    if (argv[smallest] < argv[i]) {
      secondSmallest = smallest;
      smallest = i;
    }
  }
  console.log(argv[secondSmallest]);
}
