#!/usr/bin/node
// Define the object
const myObject = {
  type: 'object',
  value: 12
};

// Print the initial state of the object
console.log(myObject);

/*
 * Adding a new method `incr` to the object
 * The `incr` method increments the `value` property of the object by 1
 */
myObject.incr = function () {
  this.value++;
};

// Call the `incr` method and print the object after each call
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
