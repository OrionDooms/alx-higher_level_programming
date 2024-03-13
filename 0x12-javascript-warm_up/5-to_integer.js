#!/usr/bin/node
if (process.argv[2] !== undefined) {
  if (isNaN(process.argv[2])) {
    console.log('Not a number');
  } else {
    const num = parseInt(process.argv[2]);
    console.log('My number:', num);
  }
} else {
  console.log('Not a number');
}
