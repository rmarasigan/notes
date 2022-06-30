# ES 6 – Promises

A `Promise` is an object that is used as a placeholder for the eventual results of a deferred (and possibly asynchronous) computation. Simply, a promise is a container for a future value. Like if you order any food from any site to deliver it to your place that order record will be the promise and the food will be the value of that promise. So the order details are the container of the food you ordered.

It is an object representing the eventual completion or failure of an asynchronous operation. Essentially, a promise is a returned object to which you attach callbacks, instead of passing callbacks into a function. A promise has 2 possible outcomes: it will either be kept when the time comes, or it won’t.

A `Promise` is in one of these states:
* *pending*
   * Initial state, neither fulfilled nor rejected
* *fulfilled*
   * Meaning that the operation was completed succssfully
* *rejected*
   * Meaning that the operation failed

<img src = "assets/img/promises.png" alt = "promises" width = "700"/>

For example, when we request data from the server by using a Promise, it will be in pending mode until we receive our data.

This is a simple demo of `Promise` with `resolve` and `then()`:
```javascript
// Promise.resolve returns a Promise that is resolved
// Syntax: Promise.resolve(value);
let promise = Promise.resolve('Resolved issue');

// then() returns a Promise. It takes up to two arguments:
// callback functions for the success and failure cases of
// the Promise
// Syntax: p.then(onFulfilled[, onRejected]);
promise.then(() => {
   console.log("Promise fulfilled");
});
```

Output:
```
Promise fulfilled
```

## Creating and using a `Promise`
Firstly, we use a constructor to create a `Promise` object. It takes two parameters, one for success (*resolve*) and one for fail (*reject*). Finally, there will be a condition that if the condition is met, the `Promise` will be resolved, otherwise it will be rejected. If the `Promise` gets resolved (sucess case), then something will happen next (depends on what we dot with the successful `Promise`). The `then()` method is called after the `Promise` is resolved. Then we can decide what to do with the resolved `Promise`. However, the `then()` method is only for resolved `Promise`. So if the `Promise` gets rejected, we need to use the `catch()` method.

```javascript
let promise = new Promise((resolve, reject) => {
   let finished = true;
   
   // Checks if condition is met
   if (finished)
   {
      resolve();
   }

   else
   {
      reject();
   }
});

promise.then(() => {
   console.log("Finished Work");
}).catch(() => {
   console.log("Didn't finished work");
});
```

Output:
```
Finished Work
```

## Creating and using a `Promise` in getting data
First, XMLHttpRequest is a built-in browser object that allows to make HTTP requests in JavaScript. We create the request and initialize it. The `xhr.open` configures the request and does not open the connection but the network activity only starts with the call of `xhr.send`.

The XMLHttpRequest object is a developers dream, because you can:
* Update a web page without reloading the page
* Request data from a server - after the page has been loaded
* Receive data from a server - after the page has loaded
* Send data to a server - in the backgroun

```javascript
function getData(method, url)
{
  return new Promise((resolve, reject) => {
    // Include the module in your project and use as the browser-based XHR object
    // This is a node-XMLHttpRequest
    let XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

    //  Create XMLHTTPRequest
    let xhr = new XMLHttpRequest();
    //  Initialize it
    xhr.open(method, url);

    xhr.onload = function () {
      if (this.status >= 200 && this.status < 300)
      {
        resolve(xhr.responseText);
      }
      else
      {
        reject({
           // HTTP Status code
           status: this.status,
           // HTTP status message
           statusText: this.statusText
        });
      }
    }

    xhr.onerror = function () {
      reject({
        status: this.status,
        statusText: this.statusText
      });
    }

    // Opens the connection and sends the request to server
    xhr.send();
  });
}

function printData(data)
{
   console.log(JSON.parse(data));
}

getData('GET', 'https://jsonplaceholder.typicode.com/users/')
  .then((data) => {
    console.log(data);
    console.log('Promise Resolved');
  });
```

Output:
```
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  .......
  {
    "id": 10,
    "name": "Clementina DuBuque",
    "username": "Moriah.Stanton",
    "email": "Rey.Padberg@karina.biz",
    "address": {
      "street": "Kattie Turnpike",
      "suite": "Suite 198",
      "city": "Lebsackbury",
      "zipcode": "31428-2261",
      "geo": {
        "lat": "-38.2386",
        "lng": "57.2232"
      }
    },
    "phone": "024-648-3804",
    "website": "ambrose.net",
    "company": {
      "name": "Hoeger LLC",
      "catchPhrase": "Centralized empowering task-force",
      "bs": "target end-to-end models"
    }
  }
]
Promise Resolved
```

Instead of having a callback inside the `then()`, we can make it a little bit modular.
```javascript
function printData(data)
{
   console.log(JSON.parse(data));
}

getData('GET', 'https://jsonplaceholder.typicode.com/users/').then(printData);
```

Output:
```
(10) [{...}, {...}, {...}, {...}, {...}, ...]
   0: (8) {id: 1, name: "Leanne Graham", usern...}
   1: (8) {id: 2, name: "Ervin Howell", userna...}
   2: (8) {id: 3, name: "Clementine Bauch", us...}
   3: (8) {id: 4, name: "Patricia Lebsack", us...}
   4: (8) {id: 5, name: "Chelsey Dietrich", us...}
   5: (8) {id: 6, name: "Mrs. Dennis Schulist"...}
   6: (8) {id: 7, name: "Kurtis Weissnat", use...}
   7: (8) {id: 8, name: "Nicholas Runolfsdotti...}
   8: (8) {id: 9, name: "Glenna Reichert", use...}
   9: (8) {id: 10, name: "Clementina DuBuque",...}
```

### Loading data with `fetch()`
The `fetch()` method is available in the global scope that instructs the web browsers to send a request to a URL. It requires only one parameter which is the URL of the resource that you want to fetch. It also uses a `Promise` so you can then use the `then()` and `catch()` methods to handle it.

Basic Fetch API:
```javascript
// Get all users
fetch('https://jsonplaceholder.typicode.com/users/').then(console.log);
```

Output:
```
Promise {<pending>}
Response {type: 'cors', url: 'https://jsonplaceholder.typicode.com/users/', redirected: false, status: 200, ok: true, …}
```

But how can we return the data as JSON? To get the actual data, you call one of the methods of the response object like `text()` or `json()`. These methods resolve into the actual data.
```javascript
// Get all users
fetch('https://jsonplaceholder.typicode.com/users/').then(response => response.json()).then(console.log);
```

Output
```
(10) [{…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}]
   0: (8) {id: 1, name: "Leanne Graham", usern...}
   1: (8) {id: 2, name: "Ervin Howell", userna...}
   2: (8) {id: 3, name: "Clementine Bauch", us...}
   3: (8) {id: 4, name: "Patricia Lebsack", us...}
   4: (8) {id: 5, name: "Chelsey Dietrich", us...}
   5: (8) {id: 6, name: "Mrs. Dennis Schulist"...}
   6: (8) {id: 7, name: "Kurtis Weissnat", use...}
   7: (8) {id: 8, name: "Nicholas Runolfsdotti...}
   8: (8) {id: 9, name: "Glenna Reichert", use...}
   9: (8) {id: 10, name: "Clementina DuBuque",...}
```

## Reference
* [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
* [Using Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
* [ES6 | Promises](https://www.geeksforgeeks.org/es6-promises/)
* [XMLHTTPRequest](https://javascript.info/xmlhttprequest)
* [JavaScript Fetch API](https://www.javascripttutorial.net/javascript-fetch-api/)
* [A Simple Guide to ES6 Promises](https://codeburst.io/a-simple-guide-to-es6-promises-d71bacd2e13a)
* [JavaScript Promise Tutorial: Resolve, Reject, and Chaining in JS and ES6](https://www.freecodecamp.org/news/javascript-es6-promises-for-beginners-resolve-reject-and-chaining-explained/)
* [A practical ES6 guide on how to perform HTTP requests using the Fetch API](https://www.freecodecamp.org/news/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547/)