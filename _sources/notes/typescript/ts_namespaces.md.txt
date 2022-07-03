# TS – Namespaces

A namespace is a way that is used for **logical grouping** of functionalities. It allows us to organize our code in a much cleaner way. A namespace can include interfaces, classes, functions, and variables to support a group of related functionalities. A namespace can *span* in multiple files and allow to *concatenate* each file using `--outfile` as they were all defined in one place.

A namespace can be cerated using the `namespace` keyword followed by the namespace name. All the interfaces, classes, etc., can be defined in the curly brackets `{}`. It is also known as **internal modules**.

Syntax:
```typescript
// Declaring a namespace
namespace namespace_name
{
   export interface interface_name {}
   export class class_name {}
}

// Accessing the namespace
namespace_name.class_name;
namespace_name.function_name;
```

If the namespace is in separate file, then it must be referenced by using **triple-slash** (`///`).
```typescript
/// <reference path = "namespace_file_name.ts" />
```

Example:
Namespace file: **`kvp.ts`**
```typescript
namespace KeyValuePair
{
   interface KeyValuePair <T, U>
   {
      Process(key: T, value: U): void;
   
   }

   export class KVP <T, U> implements KeyValuePair <T, U>
   {
      Process(key: T, value: U): void
      {
         console.log(`Key: ${key} Value: ${value}`);
      }
   }
}
```

Main file: **`script.ts`**
```typescript
/// <reference path = "kvp.ts" />

let user = new KeyValuePair.KVP;
user.Process("98182018", 'Mark Manson');
```

In order to use namespace components at other places, first we need to include the namespace using the **triple-slash** (`///`) syntax. After including the namespace file using the `reference` tag we can access all the functionalities using the namespace.

Open the terminal and go to the location where you stored your project. Use the following `--outfile` command to generate a single `.js` file for a single namespace or multiple namespaces. The `script_output.js` is a name and path of the JavaScript file and the `script.ts` is a namespace file name and path.
```bash
dev@dev:~$ tsc --outfile script.ts script_output.js
```

Compile and execute the code.
```bash
dev@dev:~$ tsc --target es6 script.ts --outfile script_output.js
dev@dev:~$ node ./script_output.js
Key: 98182018 Value: Mark Manson
```

The above command will generate the `script_output.js`.
```javascript
var KeyValuePair;
(function (KeyValuePair) {
    var KVP = /** @class */ (function () {
        function KVP() {
        }
        KVP.prototype.Process = function (key, value) {
            console.log("Key: ".concat(key, " Value: ").concat(value));
        };
        return KVP;
    }());
    KeyValuePair.KVP = KVP;
})(KeyValuePair || (KeyValuePair = {}));
// import { KeyValuePair as kvp } from './kvp';
/// <reference path = "kvp.ts" />
var user = new KeyValuePair.KVP;
user.Process("98182018", 'Mark Manson');
```

## Namespace vs. Module

### Namespace
* Must use the `namespace` keyword and the `export` keyword to expose namespace components
* Used for logical grouping of functionalities with local scoping
* To use it, it must be included using **triple-slash** (`///`) reference syntax
* Compiled using the `--outfile` command
* Must export functions and classes to be able to access it outside the namespace
* Namespaces cannot declare their dependencies
* No need of module loader. Include the `.js` file of a namespace using the `<script>` tag in the HTML page

### Module
* Uses the `export` keyword to expose module functionalities
* Used to organize the code in separate files and not pollute the global scope
* Must import it first in order to use it elsewhere
* Compiled using the `--module` command
* All the exports in a module are accessible outside the module
* Modules can declare their dependencies
* Must include the module loader API which was specified at the time of compilation e.g. CommonJS, require.js, etc.

## Reference
* [TypeScript - Namespaces](https://www.tutorialsteacher.com/typescript/typescript-namespace)
* [Difference between Namespaces and Modules](https://www.javatpoint.com/difference-between-namespaces-and-modules)