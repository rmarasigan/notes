# Introduction

## What is TypeScript?
It is a superset of JavaScript programming language that has the concept of static typing to the core feature of JavaScript. This is a big deal because JavaScript is and always has been a dynamic language. TypeScript does not run directly on the browser as JavaScript run, we have to compile the TypeScript file to the JavaScript then it will work as usual.

### Dynamic vs. Static
DYNAMIC                            | STATIC                                 |
---------------------------------- | -------------------------------------- |
Types                              | Types                                  |
[Duck Typing](#duck-typing)        | [Static Typing](#static-typing)        |
Forgiving                          | Rigid                                  |
Great for web browser object modal | Promotes stability and maintainability |

### Example
#### Duck Typing
```javascript
{
   name: "duck",
   quack: function() {}

   function sayQuack(target)
   {
      target.quack();
   }
}
```

#### Static Typing
```typescript
class Duck
{
   public string name;
   public void quack(){}
}
```

## Linux Installation

1. Install Node.js

   If you install Node.js, NPM will be automatically installed.

   #### Install the latest version
   ```bash
   dev@dev:~$ sudo apt update
   dev@dev:~$ sudo apt install nodejs
   dev@dev:~$ node -v
   v10.19.0
   ```

   #### Install specific version
   ```bash
   dev@dev:~$ sudo apt update
   dev@dev:~$ curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
   dev@dev:~$ sudo apt-get install -y nodejs
   v10.19.0
   ```

   #### Remove Node.js and NPM
   ```bash
   dev@dev:~$ sudo npm cache clean -f
   dev@dev:~$ sudo apt-get remove nodejs
   dev@dev:~$ sudo apt-get remove npm
   ```

   Go to `/etc/apt/sources.list.d` and remove any node list if you have. Then do an update
   ```bash
   dev@dev:~$ sudo apt-get update
   ```

   Check for any .npm or .node folder in your home folder and delete those. This will give you the location
   ```bash
   dev@dev:~$ which node
   /usr/bin/node
   ```

   #### Install NPM
   ```bash
   dev@dev:~$ sudo apt install npm
   ```

2. Install TypeScript
   ```bash
   dev@dev:~$ sudo npm install -g typescript
   dev@dev:~$ tsc
   Version 4.6.3
   tsc: The TypeScript Compiler - Version 4.6.3
   ```

## Reference
* [Node.js](https://nodejs.org/en/)
* [TypeScript](https://www.typescriptlang.org/)
* [What is tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)
* [TypeScript Documentation](https://www.typescriptlang.org/docs/)