#!/usr/bin/node
import { argv } from 'node:process';
function add(a, b) {
  return a + b;
}

if (!isNaN(argv[2] && !isNaN(argv[3]))) {
  console.log(add(argv[2], argv[3]));
} else {
  console.log('NaN')
}
