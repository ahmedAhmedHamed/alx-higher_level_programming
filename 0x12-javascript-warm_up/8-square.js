#!/usr/bin/node
import { argv } from 'node:process';

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let line = ''
  for (let i = 0; i < argv[2]; i++) {
    line += 'X'
  }
  for (let j = 0; j < argv[2]; j++) {
    console.log(line);
  }
}
