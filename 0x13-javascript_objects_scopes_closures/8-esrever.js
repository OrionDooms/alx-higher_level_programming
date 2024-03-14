#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let array = 0;
  let j = list.length - 1;
  while (i < j) {
    array = list[i];
    list[i] = list[j];
    list[j] = array;
    ++i;
    j--;
  }
  return (list);
};
