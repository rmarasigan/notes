# ECMA 6 – Spread Operator

## Spread syntax
Spread syntax (`...`) allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected, or an object expression to be expanded in placecs where zero or more key-value pairs (for object literals) are expected.

It is mostly used in the variable array where there is more thant 1 values are expected. It allows us the privilege to obtain a list of parameters from an array.

**Syntax**
```javascript
const odd = [1, 3, 5];
const combined = [2, 4, 6, ...odd];

console.log(combined);     // [2, 4, 6, 1, 3, 5]
```

The spread operator allows you to spread out elements of an iterable object such as an array, map, or set. In the example, the three dots (`...`) located in front of the `odd` array is the spread operator. The spread operator (`...`) unpacks the elements of the `odd` array.

### Spread Operator vs Rest Parameter

The *rest parameter* packs the elements into and array. It allows you to represent an indefinite number of arguments as an array. See the following syntax:
```javascript
function fn(a, b, ...args) {}
```

It also allows you to create dynamic function through the function constructor.
```javascript
var showNumbers = new Function('...numbers', 'console.log(numbers)');
showNumbers(1, 2, 3);      // [1, 2, 3]
```

In this example, `args` is in array. You could use the `for...of` loop to iterate over its elements and sum them up.
```javascript
function sum (...args)
{
   let total = 0;
   for (const a of args)
   {
      total += a;
   }

   return total;
}

sum(1, 2, 3);               // 6
```

It must appear at the end of the argument list. However, the spread operator can be anywhere. The spread operator unpacks the elements of an iterable object. Keep in mind that you cannot use the `use strict` directive inside any function containing a rest parameter, default parameter, or destructuring parameter.

A *spread operator* is effective only when used within array literals, function calls, or initialized properties objects. It helps us expand an iterable such as an array where multiple arguments are needed, it also helps to expand the object expressions.
```javascript
var var_name = [...iterable]; 
```

## Reference
* [JavaScript | Spread Operator](https://www.geeksforgeeks.org/javascript-spread-operator/)
* [Introduction to JavaScript Rest Parameters](https://www.javascripttutorial.net/es6/javascript-rest-parameters/)
* [Introduction to the JavaScript Spread Operator](https://www.javascripttutorial.net/es6/javascript-spread/)