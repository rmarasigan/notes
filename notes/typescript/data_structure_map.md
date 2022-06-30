# ECMA 6 – Data Structure: Maps

The `map` object is a simple key-value pair. Keys and values in a map may be primitive or objects. This data structure enables mapping a key to a value. You can create a `Map` by passing an iterable object whose elements are in the form of key-value, or you can create an empty `Map`, then insert entries.

## Object vs Maps
Object is similar to Map — both let you set keys to values, retrieve those values, delete keys, and detect whether something is stored at a key. *Regular Object* in JavaScript is *dictionary type* of data collection — which means it also follows key-value stored conecpt like Map. Each key in Object — or we normally call it "property" — is also unique and associated with a single value. It also has built-in prototype.

Map is a data collection in which data is stored in a form of pairs, which contains a unique key and value mapped to that key. Because of the uniqueness of each stored key, there is no duplicated pair stored. Map is mainly used for fast searching and looking up data.

They are indeed quite different from each other, mainly in:
* **Key field**
   * Object follows the rule of normal dictionary. The keys must be simple types (either integer or string or symbols)
   * Map can be any data type (an object, an array, etc...)
* **Element Order**
   * In Map order of elements (pairs) is preserved while in Object, it isn't
* **Inheritance**
   * Object is definitely not an instance of Map
   * Map is an instance of Object


## Methods
To create a map object:
```javascript
let person  = new Map();

// set() method adds or updates an element with a
// specified key and value
// Syntax: set(key, value)
person.set('name', 'John');

console.log(person);
```

Output:
```
Map(1) {"name" => "John"}
```

We can have function as a key of any primitive data arrays or symbols as well.
```javascript
person.set(function print()
{
   console.log("hey");
}, "John");
```

Output:
```
Map(1) {ƒ => 'John'}
```

If we added a few things like 3 times with the same key and values, it will get rid of the duplicates.
```javascript
person.set('name', 'John');
person.set('name', 'John');
person.set('name', 'John');

console.log(person);
```

Output:
```
Map(1) {"name" => "John"}
```

But if we change at least one of them, we will get a Map of 2. Basically it will automatically remove the duplicate values and ignore them.
```javascript
person.set('name', 'John');
person.set('name1', 'John1');
person.set('name', 'John');

console.log(person);
```

Output:
```
Map(2) {'name' => 'John', 'name1' => 'John'}
```

To grab the values from a map:
```javascript
// get() method returns a specified element
// from a Map object
// Syntax: get(key)
console.log(person.get('name'));
```

Output:
```
John
```

To check whether the key is available or not:
```javascript

// has() method returns a boolean indicating
// whether an element with the specified key
// exists or not
// Syntax: has(key)
console.log(person.has('name1'));
console.log(person.has('name2'));
```

Output:
```
true
false
```

To get all the keys:
```javascript

// keys() method returns a new iterator object that
// contains the keys for each element in the Map object
// in insertion order
console.log(person.keys());
```

Output:
```
MapIterator {'name', 'name1'}
```

To get all the values:
```javascript

// values() method returns a new iterator object that
// contains the values for each element in the Map
// object in insertion order
console.log(person.values());
```

Output:
```
MapIterator {'John', 'John1'}
```

To iterate on our map object:
```javascript
// forEach() method executes a provided function
// once per each key/value pair in the Map object,
// in insertion order
person.forEach(function (person) {
   console.log(person);
});
```

Output:
```
John
John1
```

Adding a key-value pairs:
```javascript
let john = ['John', '29', 'programmer']
let person = new Map([
   [john],
   [new Date(), 'today']
]);

console.log(person);
```

Output:
```
Map(2) {Array(3) => undefined, Tue Jun 28 2022 21:18:18 GMT+0800 (Philippine Standard Time) => 'today'}
```

## Reference
* [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
* [ES6 - Collections](https://www.tutorialspoint.com/es6/es6_collections.htm)
* [ES6 - Map vs Object](https://medium.com/front-end-weekly/es6-map-vs-object-what-and-when-b80621932373)
* [Simple Introduction to the ES6 Map Data Structure in JavaScript](https://levelup.gitconnected.com/simple-introduction-to-map-in-javascript-6786034f9154)