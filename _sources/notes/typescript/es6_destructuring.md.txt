# ES 6 – Destructuring

The destructuring assignment syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables. It allows you to assign the properties of an array or object to variables using syntax that looks similar to array or object literals. This syntax can be extremely terse, while still exhibiting more clarity than the traditional property access.

The two most used data structures in JavaScript are Object and Array.
* Objects allows us to create a single entity that stores data items by key
* Arrays allow us to gather data items into an ordered list


### Destructuring Arrays
The object and array literal expressions provide an easy way to create ad hoc packages of data.

```javascript
var programming = ['javascript', 'go', 'c++', 'python'];
console.log(programming[0]);
```

Output:
```javascript
javascript
```

The destructuring assignment uses similar syntax, but on the left-hand side of the assignment to define what values to unpack from the sourced variable. Destructuring does not mean *destructive*. It is called *destructuring assignment*  because it destructurizes by copying items into variables. But the array itself is not modified.

This will just assign the `first` and `last` the value to the corresponding item in the array.
```javascript
var [first, last] = ['javascript', 'go', 'c++', 'python'];
console.log(first);
console.log(last);
```

Output:
```javascript
javascript
go
```

To get the last element, we can use commas to ignore some elements. Unwanted elements of the array can also be thrown away via an extra comma:
```javascript
var [first, , , last] = ['javascript', 'go', 'c++', 'python'];
console.log(first);
console.log(last);
```

Output:
```javascript
javascript
python
```

In the code above, the second and third element of the array is skipped (as there are no variables for them), the fourth one is assigned to last. Actually, we can use it with any iterable not only arrays.
```javascript
let [a, b, c] = "abc";
console.log(a);
console.log(b);
console.log(c);
```

Output:
```javascript
a
b
c
```
That works, because internally a destructuring assignment works by iterating over the right value. It's a kind of syntax for calling `for...of` over the value to the right of `=` and assigning the values.

There's a well-known trick for swapping values of two variables using a destructuring assignment.
```javascript
let guest = "John";
let admin = "Manson";

// Swapping the values. Make guest = Manson, admin = John
 [guest, admin] = [admin, guest];

 console.log(guest);
 console.log(admin);
```

Output:
```javascript
Manson
John
```
Here we create a temporary array of two variables and immediately destructure it in swapped order.

### Default Values
If the array is shorter than the list of variables at the left, there'll be no errors. Absent values are considered undefined. But if we want a *default* value to replace the missing one, we can provide it using the `=`.

```javascript
let [name = "Guest", surname = "Anonymous"] = ["John"];
console.log(name);
console.log(surname);
```

Output:
```javascript
John
Anonymous
```

### Object Destructuring

The basic syntax is:
```javascript
let {var1, var2} = {var1: ..., var2: ....}
```

We should have an existing object on the right side, that we want to split into variables. The left side contains an object-like “pattern” for corresponding properties.
```javascript
let options = {
   title: "Menu",
   width: 100,
   height: 200
}

let {title, width, height} = options;

console.log(title);
console.log(width);
console.log(height);
```

Output:
```javascript
Menu
100
200
```

Properties `options.title`, `options.width` and `options.height` are assigned to the corresponding variables. Also, the order does not matter. This works too:
```javascript
let {height, width, title} = { title: "Menu", height: 200, width: 100 }

console.log(title);
console.log(width);
console.log(height);
```

Output:
```javascript
Menu
100
200
```

The pattern on the left side may be more complex and specify the mapping between properties and variables. If we want to assign a property to a variable with another name, for instance, make options.width go into the variable named w, then we can set the variable name using a colon.
```javascript
// { sourceProperty: targetVariable }
let {width: w, height: h, title} = options;

console.log(title);
console.log(width);
console.log(height);
```

Output:
```javascript
Menu
100
200
```

The colon shows “what : goes where”. In the example above the property `width` goes to `w`, property `height` goes to `h`, and `title` is assigned to the same name. The identifier before the colon (`:`) is the property of the object and the identifier after the colon is the variable.

## Reference
* [Destructuring assignment](https://javascript.info/destructuring-assignment)
* [Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
* [ES6 In Depth: Destructuring](https://hacks.mozilla.org/2015/05/es6-in-depth-destructuring/)
* [JavaScript Object Destructuring](https://www.javascripttutorial.net/es6/javascript-object-destructuring/)