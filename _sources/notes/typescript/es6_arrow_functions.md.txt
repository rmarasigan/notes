# ES 6 – Arrow Functions

An arrow function expression is a compact alternative to a traditional function expression, but is limited and can't be used in all situations. There are differences between arrow functions and traditional functions, as well as some limitations:

* Arrow functions don't have their own bindings to `this`. `arguments` or `super` and should not be used as `methods`
* Arrow functions don't have access to the `new.target` keyword
* Arrow functions aren't suitable for `call`, `apply` and `bind` methods, which generally rely on establishing a scope
* Arrow functions cannot be used as constructors
* Arrow functions cannot use yield, within its body

Arrow functions are **anonymous functions** (the functions without a name and not bound with an identifier). They don't return any value and can declare without the function keyword. The context within the arrow functions is lexically or statically defined. They are also called as **Lambda Functions** in different languages.

## Syntax
One param. With simple expression return is not needed:
```javascript
parameter => expression
```

Multiple params require parentheses. With simple expression return is not needed:
```javascript
(parameter1, parameterN) => expression
```

Multiline statements require body braces and return:
```javascript
parameter => {
   let a = 1;
   return a + param;
}
```

There are three parts to an Arrow Function or Lambda Function:
* Parameters
   * Any function may optionally have the parameters
* Fat arrow notation / Lambda notation
   * It is the notation for the *arrow (=>)*
* Statements
   * It represents the instruction set of the function

```javascript
const functionName = (arg1, arg2, ....) => {
   // code block here
}
```

## Examples
First, let us create a function expression
```javascript
var person = function (person) {
   console.log(person);
};

person('John');
```

Output:
```
John
```

The function expression can be written with arrow syntax and it will be lot less code.
```javascript
var person = (person) => {
   console.log(person);
};

person('John');
```

Output:
```
John
```

To make it more short:
```javascript
var person = (person) => console.log(person);
console.log(person);
```

Output:
```
John
```

If only one parameter is defined, we don't really have to have a code block. Also, we don't even need the parentheses around our parameter and it will still give you the same result.
```javascript
var person = person => console.log(person);
console.log(person);
```

Output:
```
John
```

How about create a function without any parameter? So this is how you can define a function without any parameter.
```javascript
var x = () => { console.log('Arrow function works') };
a();
```

Output:
```
Arrow function works
```

## This Scope
`this` always references the owner of the function it is in, for this case — since it is now out of scope — the window/global object. When it is inside of an object’s method — the function’s owner is the object. Thus the ‘this’ keyword is bound to the object. Yet when it is inside of a function, either stand alone or within another method, it will always refer to the window/global object.

```javascript
var person = {
   name: 'John',
   hobbies: ['programming', 'fishing', 'video games'],
   printHobbies: function () {
      // This is used to access the person's objects
      // to reference inside the forEach function
      // of hobbies
      var _this = this;

      this.hobbies.forEach(function (hobby) {
         // Since we are inside the forEach function
         // we cannot access the `this` keyword that
         // points to the person object.
         var msg = _this.name + " likes " + hobby;
         console.log(msg);
      })
   }
}

person.printHobbies();
```

Output:
```
John likes programming
John likes fishing
John likes video games
```

There is another way to make it work without using the `_this` variable and will still give us the same exact result. Use `bind` to attach the ‘this’ keyword that refers to the method to the method’s inner function.
```javascript
var person = {
   name: 'John',
   hobbies: ['programming', 'fishing', 'video games'],
   printHobbies: function () {
      this.hobbies.forEach(function (hobby) {
         var msg = this.name + " likes " + hobby;
         console.log(msg);
      }.bind(this))
   }
}

person.printHobbies();
```

Output:
```
John likes programming
John likes fishing
John likes video games
```

And now introducing Arrow functions. Dealing with `this` issue has never been easier and more straightforward. In ES6, arrow functions use lexical scoping — `this` refers to it’s current surrounding scope and no further. Thus the inner function knew to bind to the inner function only, and not to the object’s method or the object itself.
```javascript
var person = {
   name: 'John',
   hobbies: ['programming', 'fishing', 'video games'],
   printHobbies() {
      this.hobbies.forEach((hobby) => {
         var msg = this.name + " likes " + hobby;
         console.log(msg);
      });
   }
}

person.printHobbies();
```

Output:
```
John likes programming
John likes fishing
John likes video games
```

## Reference
* [ES6 Arrow Function](https://www.javatpoint.com/es6-arrow-function)
* [Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
* [Learn ES6 The Dope Way Part II: Arrow functions and the ‘this’ keyword](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)