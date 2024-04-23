#!/usr/bin/node
const Status = require('request');
const url = process.argv[2];
Status.get(url).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});
