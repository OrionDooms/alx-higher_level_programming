#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    while (this.height > i) {
      let a = c;
      for (let j = 1; this.width > j; ++j) {
        a += c;
      }
      ++i;
      console.log(a);
    }
  }
}
module.exports = Square;
