#!/usr/bin/node
if (process.argv[2] !== undefined) {
  const argNum = parseInt(process.argv[2]);
  if (!isNaN(argNum)) {
    for (let i = 0; i < argNum; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
