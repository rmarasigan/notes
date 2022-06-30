# ECMA 6 – Data Structure: Set

`Set` objects are collections of values. You can iterate through the elements of a set in insertion order. A value in the `Set` may only occur once; it is unique in the Set's collection. The Set constructuor also accepts an optional iterable object. If you pass an iterable object to the Set constructor, all the elements of the iterable object will be added to the new set.

Set in ES6 are ordered: elements of the set can be iterated in the insertion order. Set can store any types of values whether primitive or objects.


To create a new empty set:
```javascript
let setObject = new Set();
```

Create a new Set from an Array:
```javascript
let number = [1, 2, 3, 4, 4, 5, 6, 1, 2, 7];
let numberSet = new Set(number);
console.log(numberSet);
```

Output:
```
Set(7) {1, 2, 3, 4, 5, 6, 7}
```

To add a new element with specified value to the set.
```javascript
let names = new Set();

// add() method appends a new element with a specified
// value to the end of a Set object.
names.add("John");
names.add("Doe");
names.add("John");

console.log(names);
```

Output:
```
Set(2) {'John', 'Doe'}
```

To check if the value is in the set:
```javascript
// has() method returns a boolean indicating whether an
// element with the specified value exists in a Set object
// or not.
console.log(names.has("John"));   // true
console.log(names.has("Marta"));  // false
```

Output:
```
true
false
```

To remove it from the set:
```javascript
names.add("John");
names.add("Doe");
names.add("Marta");
console.log(names);

// delete() method removes a specified value from a
// Set object, if it is in the set.
names.delete('John');
console.log(names);
```

Output:
```
Set(3) {'John', 'Doe', 'Marta'}
Set(2) {'John', 'Doe'}
```

To remove/delete all elements in the set:
```javascript
// clear() method removes all elements from a Set
// object.
names.clear();
console.log(names);
```

Output:
```
Set(0) {}
```

To iterate on our set object:
```javascript
// forEach() method executes a provided function once
// for each value in the Set object, in insertion order.
names.forEach(function (e) {
   console.log(e);
});
```

Output:
```
John
Doe
Marta
```

To get the size of our set object:
```javascript
names.size
```

Output:
```
3
```

## Reference
* [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
* [Sets in JavaScript](https://www.geeksforgeeks.org/sets-in-javascript/)
* [The Beginner’s Guide to JavaScript Set Type in ES6](https://www.javascripttutorial.net/es6/javascript-set/)