# ECMA 6

ECMAScript 6 or JavaScript ES6 is the newer version of JavaScript that was introduced in 2015. It defineds the standard for the JavaScript implementation. It introduces several new features such as, block-scoped variables, new loop for iterating over arrays and objects, template literals, and many other enhancements to make JavaScript programming easier and more fun.

## History
```
└─── [ 1995 ] JavaScript Created
└─── [ 1997 ] ECMAScript 1
└─── [ 1998 ] ECMAScript 2
└─── [ 1999 ] ECMAScript 3
└─── [ 2008 ] ECMAScript 4
└─── [ 2009 ] ECMAScript 5
└──⌍
│  └─[ 2011 ] ECMAScript 5.1
└─── [ 2015 ] ECMAScript 6
```

## `const` keyword
You define a variable with a `const` keyword when you don't want its value to be changed, so that would be a constant. Constants are read-only, you cannot reassign new values to them.

```javascript
const PI = 3.14;
console.log(PI); // 3.14

PI = 10; // error
```

Another example of use case of `const` keyword:
```javascript
const name = 'John';

function createName(firstName, lastName)
{
   const name = firstName + " " + lastName;
   console.log(name);
}

console.log(name);                  // John
createName('Robert', 'White');      // Robert White
console.log(name);                  // John
createName('Andrew', 'Garfield');   // Andrew Garfield
console.log(name);                  // John
```
As you can see, it did not change because we are using the `const` keyword on the left side of the name defined in `createName`, and is not trying to access the `name` variable on a global scope.

The `const` keyword can be used with arrays and objects. It does not stop us to modify a complicated object. For example, arrays and objects, but will stop us to assign the `days` array to a new array. You can modify the existing object or an array and add values, remove values and do a lot of things. But you cannot assign that constant array or object to a new array or a new object literal.
```javascript
// Array
const days = ["Monday"];
console.log(days);      // ["Monday"]

days.push('Tuesday');
console.log(days);      // ["Monday", "Tuesday"]

days = ["Friday"];      // Uncaught TypeError

// Object
const person = {
   first_name: 'Robert'
};
console.log(person);    // {first_name: 'Robert'}

person.last_name = "White";
console.log(person);    // {first_name: 'Robert', last_name: 'White'}
```

## `let` keyword

### Scope of variables
When you declare a variable outside of any function or outside any code block it is called a **global variable** because it is available to any other code in the current document. Declaring a variable outside a function or a block outside a function leads to it being globally scoped. When you declare a variable within a function or a block, it is called a **local variable** because it is only available within that function or block.

Local scope variables are divided into:
* **Function scoped variables**
   - The variable defined within a funcion will not be accessible from outside the function.

* **Block scoped variables**
   - The variable defined within a block will not be accessible from outside the block. A block can reside inside a function, and a block scoped variable will not be available outside the block even if the block is inside a function.

#### `var` block scoped
```javascript
if (true)
{
   var x = 10;
}

console.log(x);   // 10
```

#### `let` block scoped
```javascript
if (true)
{
   let x = 10;
}

console.log(x);   // x is not defined
```

Variables declared with `let` keyword are block-scoped (`{}`) and they are not hoisted. Block scoping simply means that a new scope is created between a pair of curly brackets i.e. `{}`. Therefore, if you declare a variable with the `let` keyword inside a loop, it does not exist outside of the loop.

## Reference
* [Variables in JavaScript](https://www.section.io/engineering-education/variables-in-javascript/)
* [JavaScript ES6 Features](https://www.tutorialrepublic.com/javascript-tutorial/javascript-es6-features.php)