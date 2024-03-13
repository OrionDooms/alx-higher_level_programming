#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let c = 0;
  while (list.length > i) {
    if (list[i] === searchElement) {
      c += 1;
    }
    ++i;
  }
  return (c);
};
