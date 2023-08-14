#!/usr/bin/node
import { argv } from 'node:process';
if (argv[0] && !argv[1]) {
  console.log('Argument found');
} else if (argv[0] && argv[1]) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
