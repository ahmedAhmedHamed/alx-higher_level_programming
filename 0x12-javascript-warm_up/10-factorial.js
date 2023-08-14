#!/usr/bin/node
import { argv } from 'node:process';

function factorial (n) {
  if (isNaN(n) || n === 1)
    return 1;
  return n * factorial(n-1);
}

console.log(factorial(argv[2]));
