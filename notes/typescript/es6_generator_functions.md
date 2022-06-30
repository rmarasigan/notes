# ES 6 – Generator Functions

Generator function objects created with a constructor are parsed when the function is created. That is less efficient than declaring a generator function with a `function*` expression and calling it within your code, because such functions are parsed with the rest of the code. A generator is a function that can stop midway and then continue from where it stopped.

It gives a new way to work with iterators and functions. ES6 Generator is a new type of function that can be paused in the middle or many times in the middle and resumed later. In standard function, control remains with the called function until it returns, but generator function allows the caller function to control the execution of a called function.

Here are some other common definitions of generators:
* Generators are a special class of functions that simplify the task of writing iterators
* A generator is a function that produces a sequence of results instead of a single value

## Normal vs Generator Functions

<img src = "assets/img/normal-vs-generator-function.png" alt = "normal-vs-generator-function" width = "600"/>

The difference between a generator and a regular function is:
* In response to a generator call, its code doesn't run. In its place, it returns a special object called a *Generator Object* to manage the execution
* At any time, the generator function can return (or yield) the control back to the caller
* The generator can return (or yield) multiple values according to the requirement, unlike a regular function

## Syntax
Generator functions have a similar syntax to regular functions. As the only difference is denoted by an asterisk (`*`) after the function keyword.
```javascript
function *functionName() {}
```

* **`yield`**
   * Function execution is suspended and a value is returned to the caller
* **`next()`**
   * `next()` method will resume the execution of the generator function when it receives an argument, replacing the yielded expression where the execution was paused with the argument from the `next()` method.
   * Objects returned:
      * **`value`** – Yielded value.
      * **`done`** – The completed state of a function can be expressed as a boolean value true. Otherwise, it yields false.

## Example
For creating a generator function, we use `function *` syntax instead of just `function`. Inside the body, we don't have a `return` keyword. Instead we have `yield`. It is an operator with which a generator can pause itself. Everytime a generator encounters a `yield`, it returns the value specified after it. Calling a generator function does not execute the body immediately. Instead of returning any value, a generator function *always* returns a generator object. The generator object is an iterator.
```javascript
function *myFunction(i) {
   yield i;
   yield i + 5;
}

var generator = myFunction(10);
console.log(generator);
```

Output:
```
myFunction {<suspended>}
```

In here, we call the `next()` method on the generator object. With this call, the generator begins executing. The generator yields the value as an object and suspends/pauses. Now, it is waiting for the next invocation. For the next `next()` method, the generator wakes up and begin executing where it left.
```javascript
function *myFunction(i) {
   yield i;
   console.log(i + " Just log this");
   yield i + 5;
}

var generator = myFunction(10);
console.log(generator.next());
console.log(generator.next());
```

Output:
```
{value: 10, done: false}
10 Just logged this
{value: 15, done: false}
```

The `next()` method returns an object with a `value` property containing the yielded value and a `done` property which indicates whether the generator has yiedled its last value, as a boolean.

## Reference
* [function*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
* [GeneratorFunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction)
* [Explain the Generator Function in ES6](https://www.geeksforgeeks.org/explain-the-generator-function-in-es6/)
* [Understanding Generators in ES6 JavaScript with Examples](https://codeburst.io/understanding-generators-in-es6-javascript-with-examples-6728834016d5)