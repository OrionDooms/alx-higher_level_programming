#!/usr/bin/node
const contents = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

contents(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFileSync(filename, body, 'utf-8');
  }
});
