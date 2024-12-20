#!/usr/bin/node
// This function increments a number and calls another function with the new value

exports.addMeMaybe = function (number, theFunction) {
  const newValue = number + 1; // Increment the number
  theFunction(newValue); // Call the provided function with the incremented value
};

