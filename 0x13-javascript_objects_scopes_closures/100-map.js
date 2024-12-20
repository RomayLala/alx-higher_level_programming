#!/usr/bin/node
// This script imports the list from 100-data.js and computes a new list
const list = require('./100-data').list;

// Use map to create a new list where each element is multiplied by its index
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
