#!/usr/bin/node
const rectangle = require('./4-rectangle.js');
class Square extends rectangle {
  size;
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
