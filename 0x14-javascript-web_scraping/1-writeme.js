#!/usr/bin/node
const Write_me = require('fs');
Write_me.writeFile(process.argv[2], process.argv[3], 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
