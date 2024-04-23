#!/usr/bin/node

const Readme = require('fs');
Readme.readFile(process.argv[2], 'utf8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
