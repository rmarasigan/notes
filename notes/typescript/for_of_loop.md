#  ES 6 – "for-of" Loop

`for...of` iterates over an iterable object such as:
* Built-in `Array`, `String`, `Map`, `Set`, ...
* Array-like objects such as `arguments` or `NodeList`
* User-defined objects that implement the iterator protocol

## Syntax
```javascript
for (variable of iterable) {
   statement
}
```

* **`variable`**
   * It may be declared with `const`, `let` or `var`
   * On each iteration a value of different property is assigned to variable
* **`iterable`**
   * Object whose iterable properties are iterated

## Examples of `for...of`

### Iterate over a String:
```javascript
let programming = 'javascript';

for (let x of programming) {
   console.log(x);
}
```

Output:
```
j
a
v
a
s
c
r
i
p
t
```

So it is iterating over a string and we can use the `for...of` loop for iterating an arays as well.

### Iterate over Array
```javascript
let programming = ['javascript', 'go', 'python', 'c++'];

for (let x of programming) {
   console.log(x);
}
```

Output:
```
javascript
go
python
c++
```

The `let x` is a variable which holds the current iterable value. It is a variable placeholder and store the first value into the x and do whatever we want inside the function and go grab the second one and store that into the next until it finishes the loop.

To access the index of the array elements inside  the loop, you can use the `for...of` statement with the `entries()` method of the array. The `array.entries` method returns a pair of `[index, element]` in each iteration.
```javascript
let programming = ['javascript', 'go', 'python', 'c++'];

for (let [index, language] of programming.entries()) {
   console.log(`${language} is at index ${index}`);
}
```

Output:
```
javascript is at index 0
go is at index 1
python is at index 2
c++ is at index 3
```

### Iterate over a Map object
```javascript
let programming = new Map();

programming.set('HTML', 'HypertText Markup Language');
programming.set('Scripting', 'JavaScript is so cool');
programming.set('CSS', 'StyleSheet');

for (let x of programming) {
   console.log(x);
}
```

Output:
```
(2) ['HTML', 'HypertText Markup Language']
(2) ['Scripting', 'JavaScript is so cool']
(2) ['CSS', 'StyleSheet']
```

To iterate Map keys:
```javascript
for (let x of programming.keys()) {
   console.log(x);
}
```

Output:
```
HTML
Scripting
CSS
```

## Reference
* [for...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
* [JavaScript for…of Loop](https://www.javascripttutorial.net/es6/javascript-for-of/)