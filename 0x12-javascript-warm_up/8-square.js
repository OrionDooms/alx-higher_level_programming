#!/usr/bin/node
if (process.argv[2] !== undefined) {
  let i = 0;
  const num = parseInt(process.argv[2]);
  while (num > i) {
    let a = 'X';
    for (let j = 1; num > j; ++j) {
      a += 'X';
    }
    ++i;
    console.log(a);
  }
}
