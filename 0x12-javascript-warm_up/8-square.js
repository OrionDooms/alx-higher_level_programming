#!/usr/bin/node
if (process.argv[2] !== undefined) {
  if (isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    let i = 0;
    const num = parseInt(process.argv[2]);
    while (num > i) {
      let j = 1;
      let a = 'X';
      while (num > j) {
        a += 'X';
        ++j;
      }
      ++i;
      console.log(a);
    }
  }
} else {
  console.log('Missing size');
}
