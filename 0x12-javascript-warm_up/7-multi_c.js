#!/usr/bin/node
if (process.argv[2] !== undefined) {
  const arg = process.argv[2];
  const times = process.argv[3] || 1;
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences”');
}
