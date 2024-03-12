#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (this.height > i) {
      let a = 'X';
      for (let j = 1; this.width > j; ++j) {
        a += 'X';
      }
      ++i;
      console.log(a);
    }
  }
}

module.exports = Rectangle;
