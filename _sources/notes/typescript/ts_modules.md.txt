# TS – Modules

A module is a way to create a group of related variables, functions, classes, and interfaces, etc. It executes in the **local scope**, not in the global scope. In other words, the variables, functions, classes, and interfaces declared in a module cannot be accessible outside the module directly. We can create a module by using the **`export`** keyword and can use in other modules by using the **`import`** keyword.

Modules import another module by using a **module loader**. At runtime, the module loader is responsible for locating and executing all dependencies of a module before executing it. The most common modules loaders which are used in JavaScript are the CommonJS module loader for Node.js and require.js for Web applications. In TypeScript, files containing a top-level export or import are considered modules.

<img src = "assets/img/namespaces-vs-modules.png" alt = "namespaces-vs-modules" width = "600"/>

There are three main things to consider when writing module-based code in TypeScript:
* Syntax
* Module Resolution
* Module Output Target

## `export`
A module can be defined in a separate `.ts` file which can contain functions, variables, interfaces and classes. Use the prefix `export` with all the definitions you want to include in a module and want to access from other modules.

Syntax:
```typescript
export class class_name {}
export let variable_name : data_type = value;

// You can export it like this
export { class_name }
export { class_name as alias_name }
```

## `import`
A module can be used in another module using an `import` statement.

Syntax:
```typescript
import { export_name } from "file_path_without_extension";
import { export_name as alias_name } from "file_path_without_extension";
```

### Creating a module

#### `kvp.ts`
Create a new module called `kvp.ts` and declares an interface called `KeyValuePair` and a class called `KVP`.
```typescript
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
```

In this module, we place the `export` keyword before the `class` keyword to expose it to other modules. In other words, if you do not use the `export` keyword, the `KVP` class is private in the `kvp.ts` module, therefore, it cannot be used by other modules. Other way to export a declaration from a module is to use the `export` statement. TypeScript also allows you to rename declarations for module consumers.

```typescript
class KVP <T, U> implements KeyValuePair <T, U>
{
   Process(key: T, value: U): void
   {
      console.log(`Key: ${key} Value: ${value}`);
   }
}

// You can export it like this:
export { KVP };

// Or you can rename the declaration:
export { KVP as KeyValuePair };
```

#### `script.ts`
To consume a module, you use the `import` statement. Crete a new module called `script.ts` that uses the `kvp.ts` module.

```typescript
import { KeyValuePair } from './kvp';

let user = new KeyValuePair;
user.Process("98182018", 'Mark Manson');
```

When importing a module, you can rename it.
```typescript
import { KeyValuePair as kvp } from './kvp';
```

Output:
```
Key: 98182018 Value: Mark Manson
```

## Reference
* [TypeScript Modules](https://www.typescripttutorial.net/typescript-tutorial/typescript-modules/)
* [TypeScript - Modules](https://www.tutorialsteacher.com/typescript/typescript-module)
* [Difference between Namespaces and Modules](https://www.javatpoint.com/difference-between-namespaces-and-modules)