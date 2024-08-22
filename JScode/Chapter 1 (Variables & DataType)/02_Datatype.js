/* In JavaScript, a datatype refers to the type of data that can be stored and manipulated within a program. JavaScript has several built-in datatypes, and understanding them is crucial for writing effective code. */


// Number
let age = 25; // integer
let pi = 3.14; // floating-point number

// String
let namea = "John Doe";

// Boolean
let isStudent = true;

// Undefined
let middleName; // No value assigned, so it's undefined

// Null
let car = null; // No value

// Object
let person = {
  firstName: "Jane",
  lastName: "Doe",
  age: 28
};

// Symbol
let uniqueId = Symbol("id");

// BigInt
let bigNumber = 9007199254740991n;

// Output the types
console.log(typeof age); // "number"
console.log(typeof namea); // "string"
console.log(typeof isStudent); // "boolean"
console.log(typeof middleName); // "undefined"
console.log(typeof car); // "object" (null is an exception where typeof returns "object")
console.log(typeof person); // "object"
console.log(typeof uniqueId); // "symbol"
console.log(typeof bigNumber); // "bigint"