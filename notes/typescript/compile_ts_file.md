# How to compile a TypeScript file?

### app.ts
```typescript
let hello: string = "Hello everybody. Welcome to TypeScript Course";
```

On the terminal, run the following command and this will create a JavaScript file from TypeScript automatically with the same name.
```bash
dev@dev:~$ tsc ./file_name.ts
```

This is the JavaScript file from TypeScript:
##### app.js
```javascript
var hello = "Hello everybody. Welcome to TypeScript Course";
```

To compile the file automatically, you can run the following command:
```bash
dev@dev:~$ tsc -w ./file_name.ts
[2:53:01 PM] Starting compilation in watch mode...

[2:53:02 PM] Found 0 errors. Watching for file changes
```

If there's some changes made on the file it will automatically compiled. It will be looking for the changes from the `.ts` file and will compile that into `.js` file.

##### app.ts
```typescript
let hello: string = "Hello everybody. Welcome to TypeScript Course";
let name: string = "_undefine";
```

##### app.js
```javascript
var hello = "Hello everybody. Welcome to TypeScript Course";
var name = "_undefine";
```

To specify the language used for the compiled output, you can create a `tsconfig.json` file. It is a file that corresponds to the configuration of the TypeScript compiler (tsc).
```json
{
   "compilerOptions": {
      "target": "ES5"
   }
}
```

Having the `tsconfig.json` file and running a command of `tsc -w`, it will watch for every single file available in your application. Once you created a new file, it will automatically compile your TypeScript file into JavaScript.
```bash
dev@dev:~$ tsc -w
[3:11:00 PM] Starting compilation in watch mode...
```

If you change the version of the target on your `tsconfig.json`, it will also automatically update the JavaScript file into the target version you set.
```json
{
   "compilerOptions": {
      "target": "ES6"
   }
}
```

As you can see, it automatically update the JavaScript file to the latest version. Instead of using `var` keyword, now it uses the `let` keyword.
##### app.js
```javascript
let hello = "Hello everybody. Welcome to TypeScript Course";
let name = "_undefine";
```

## Reference
* [TypeScript](https://www.typescriptlang.org/)
* [What is tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)