#!/usr/bin/node
import { argv } from 'node:process';
if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = argv[2]; i > 0; i--) {
    console.log('C is fun');
  }
}
