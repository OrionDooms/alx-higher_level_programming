#!/usr/bin/node
if (process.argv[3] !== undefined) {
  const num1 = Number(process.argv[2]);
  const num2 = Number(process.argv[3]);
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}

function add (a, b) {
  return (a + b);
}
