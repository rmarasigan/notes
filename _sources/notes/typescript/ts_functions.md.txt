# TS – Functions

Functions are the primary means of passing data around in JavaScript. They are the primary blocks of any program. With functions, you can implement/mimic the concepts of object-oriented programming like classes, objects, polymorphism, and abstraction. Functions ensure that the program is maintainable and reusable, and organized into readable blocks. It is a set of statements to perform a specific task. Once defined, functions may be called to access code. This makes the code reusable.

A function declaration tells the compiler about a function's name, return type, and parameters. A function definition provides the actual body of the function.

## Named Functions
A named function is one where you declare and call a function by its given name.

Syntax:
```typescript
function display() {}

display();
```

Functions can also include parameter types and return type.
```typescript
function sum(x: number, y: number) : number
{
   return x + y;
}

sum(1, 2);
```

Output:
```
3
```

In this example, the `sum()` function accepts two parameters with the `number` type. In it, you can only pass numbers into it, not the values of other types. The `: number` after the parentheses indicate the return type. The `sum()` function return a value of the `number` type.

When a function has a return type, the TypeScript compiler checks every `return` statement against the return type to ensure that the return vlalue is compatible with it. If a function does not return a value, you can use the `void` type as the return type. The `void` keyword indicates that the function doesn't return any value.

Example:
```typescript
function print(message: string) : void
{
   console.log(message.toUpperCase());
}
```

## Anonymous Function
An anonymous function is one which is defined as an expression. This expression is stored in a variable. So, the function itself does not have a name. These functions are invoked using the variable name that the function is stored in. An anonymous function is usually not accesible after its initial creation. Variables can be assigned an anonymous function. Such an expression is called a function expression.

Syntax:
```typescript
let anonymous = function() {}

anonymous();
```

An anonymous function can also include parameter types and return type, just as standard functions do.
```typescript
let sum = function(x: number, y: number) : number {
   return x + y;
}

sum(1, 2);
```

Output:
```
3
```

## Optional Parameters
Optional parameters can be used when arguments need not be compulsorily passed for a function's execution. A parameter can be marked optimal by append a question mark to its name. The optional parameter *should be set as the last argument* in a function.

```typescript
function function_name (param_1: data_type, param_2: data_type, param_3?: data_type) {}
```

Example:
```typescript
function user_details(name: string, email: string, mobile?: string)
{
   if (mobile != undefined)
   {
      // code block here
   }
}

user_details("Manson", "mark_manson@gmail.com");
user_details("Paulo", "paulo_cuelho@gmail.com", "12345678923");
```

In the above example, the last parameter `mobile` is marked as optional with a question mark appended at the end. If we do not specify the last parameter then its value will be `undefined`.

## Default Parameters
Like optional parameters, default parameters are also optional. It means that you can omit the default parameters when calling the function. A parameter cannot be declared optional and default at the same time.


Syntax:
```typescript
function function_name (param_1 = default_value1, ...) {}
```

In this syntax, if you don't pass arguments or pass the `undefined` into the function when calling it, the function will take the default initialized values for the omitted parameters.

Example:
```typescript
function calculate (price: number, rate: number = 0.50)
{
   let discount = price * rate;
   console.log(`Discount Amount: ${discount}`);
}

calculate(2000);
calculate(2500, 0.30)
```

Output:
```
Discount Amount: 1000
Discount Amount: 750
```

In the example above, the `calculate` function takes two parameters – price and rate. The default parameter value for rate is set to 0.50. When the program invokes the function, only passing the price parameter, the value of rate is 0.50 as there is no rate parameter being passed so the default value will be used. Again, the same function is invoked but with two arguments. The default value of rate is overwritten and is set to the value explicitly passed.

## Rest Parameters
When the number of parameters that a function will receive is not known or can vary, we can use rest parameters. With TypeScript we can use rest parameters denoted by ellipsis `...`. We can pass zero or more arguments to the rest parameters. The compiler will create an array of arguments with the rest parameter name provided by us.

Rest parameters don’t restrict the number of values that you can pass to a function. However, the values passed must all be of the same type. In other words, rest parameters act as placeholders for multiple arguments of the same type. Any nonrest parameter should come before the rest parameter.

Syntax:
```typescript
function function_name (param_1: data_type, ...param_2: data_type) {}
```

Example:
```typescript
function sum(...numbers: numbers[]): number
{
   let total = 0;
   numbers.forEach((num) => total += num);
   return total;
}

console.log(sum(1, 2, 3));
```

Output:
```
6
```

In this example, the `sum()` function calculates the total amount of numbers passed into it. Since the `numbers` parameter is a rest parameter, you can pass one or more numbers to calcule the total.

## Reference
* [TypeScript Functions](https://www.typescripttutorial.net/typescript-tutorial/typescript-functions/)
* [TypeScript - Functions](https://www.tutorialsteacher.com/typescript/typescript-function)
* [TypeScript - Functions](https://www.tutorialspoint.com/typescript/typescript_functions.htm)
* [TypeScript Rest Parameters](https://www.typescripttutorial.net/typescript-tutorial/typescript-rest-parameters/)
* [Everyday Types - Functions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#functions)
* [TypeScript - Rest Parameters](https://www.tutorialsteacher.com/typescript/rest-parameters)
