#!/usr/bin/node
// This script concatenates the content of two files and writes it to a destination file

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Function to read file and handle errors
const readFile = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
};

// Function to write to the destination file
const writeFile = (destination, data) => {
  fs.writeFile(destination, data, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
};

// Concatenate files and write to destination
Promise.all([readFile(fileA), readFile(fileB)])
  .then((data) => {
    const combinedData = data.join('');
    writeFile(fileC, combinedData);
  })
  .catch((err) => {
    console.error(err);
  });
