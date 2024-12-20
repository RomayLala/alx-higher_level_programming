#!/usr/bin/node
// This script takes a dictionary of occurrences by user ID and computes a dictionary of user IDs by occurrence

const { dict } = require('./101-data.js'); // Importing the original dictionary

const occurrencesDict = {}; // New dictionary to store user IDs by occurrence

// Loop through the original dictionary to invert its structure
for (const userId in dict) {
  const occurrences = dict[userId]; // Get the number of occurrences

  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = []; // If not present, initialize an empty array
  }

  occurrencesDict[occurrences].push(userId); // Add user ID to the corresponding occurrence list
}

// Print the new dictionary
console.log(occurrencesDict);
