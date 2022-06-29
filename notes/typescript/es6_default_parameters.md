# ES 6 – Default Parameters in Functions and Object Literals

## Default Function Parameters
Allow named parameters to be initialized with default values if no value or `undefined` is passed.

### Syntax
```javascript
function functionName(parameter1 = defaultValue1, ..., parameterN = defaultValueN) {
   // code block here
}
```
### Examples
For example, we have this function `add` without a default value.
```javascript
function add(x, y)
{
   return x + y;
}

add();
```

Basically we are not passing any value to the function `add()`. So it will give you a result of `NaN` which means *not a number*.

Output:
```javascript
NaN
```

Adding a default value but we're not passing any value to the `add()` function will give you a result of 10. But if you pass in a value, the default values will be ignored as long as there is value passed to the function.
```javascript
function add(x = 5, y = 5)
{
   return x + y;
}

add();
add(2, 3);
```

Output:
```javascript
10
5
```

But what if we did not pass the second parameter value? Since there is a default value for the 2nd parameter, it will return a value of 7.
```javascript
add(2)
```

Output:
```javascript
7
```

### Arguments vs. Parameters
Parameters are what you specify in the function declaration whereas arguments are what you pass into the function.
```javascript
function add(x, y)
{
   return x + y;
}

add(100, 200);
```

The `x` and `y` are the parameters of the `add()` function, and the values passed to the `add()` function `100` and `200` are the arguments.

## Object Literal Enhancement
Object literal enhancement is used to group variables from the global scope and form them into javascript objects. It is the process of restructuring or putting back together.


When defining object methods, it is no longer necessary to use the **`function`** keyword. Object literal enhancement allows us to pull global variables into objects and reduces typing by making the function keyword unnecessary.

#### Old Syntax
```javascript
var person = {
   name: function() {
      return 'John';
   },
   age: function() {
      return 29
   }
}

console.log(person.name());
```

Output:
```javascript
John
```

#### New Syntax
In ES6, we don't really have to type in a `function` keyword.
```javascript
var person = {
   name() {
      return 'John';
   },
   age() {
      return 29
   }
}

console.log(person.name());
```

Output:
```javascript
John
```

### Computed Properties
Computed property names allow us to write an expression wrapped in square brackets (`[]`) instead of the regular property name. Whatever the expression evaluates to will become the property name. The square brackets allow you to use the string literals and variables as the property names.

```javascript
var name = "make"
const laptop = {
   [name]: "Apple"
}

console.log(laptop.make);
```

Output:
```javascript
Apple
```

The value of `name` was computed to `make` and this was used as the name of the property. In ES6, the computed property name is a part of the object literal syntax, and it uses the square bracket notation. When a property name is placed inside the square brackets, the JavaScript engine evaluates it as a string. It means that you can use an expression as a property name.

```javascript
let prefix = 'machine';
let machine = {
    [prefix + ' name']: 'server',
    [prefix + ' hours']: 10000
};

console.log(machine['machine name']);
console.log(machine['machine hours']);
```

Output:
```javascript
server
10000
```

## Reference
* [Default Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
* [JavaScript Default Parameters](https://www.javascripttutorial.net/es6/javascript-default-parameters/)
* [Enhanced Object Literals in ES6](https://dev.to/sarah_chima/enhanced-object-literals-in-es6-a9d)
* [Object Literal Syntax Extensions in ES6](https://www.javascripttutorial.net/es6/object-literal-extensions/)
* [JavaScript (ES6) | Object Literal Enhancement](https://www.geeksforgeeks.org/javascriptes6-object-literal-enhancement/)