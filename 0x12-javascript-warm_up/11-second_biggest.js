#!/usr/bin/node
import { argv } from 'node:process';

if (!argv[2]) { console.log(0); } else if (argv[2] && !argv[3]) { console.log(1); } else {
  let biggest = 2;
  let secondBiggest = 2;
  for (let i = 2; i < argv.length; i++) {
    if (argv[biggest] < argv[i]) {
      secondBiggest = biggest;
      biggest = i;
    } else if (argv[secondBiggest] < argv[i]) {
      secondBiggest = i;
    }
  }
  console.log(argv[secondBiggest]);
}
