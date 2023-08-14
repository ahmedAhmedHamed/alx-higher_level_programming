#!/usr/bin/node
import { argv } from 'node:process';
if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
