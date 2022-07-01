# TS – Advance Types

## Union
A union type is a type formed from two or more other types, representing values that may be any one of those types. We refer to each of these types as the union's members. The union type allows you to combine multiple types into one type. It describes a value that can be one of several types, not just two.

Syntax:
```typescript
let union_name: (type_1 | type_2 | type_3 ... | type_n);
```

Example:
```typescript
let union_name: string | number;

union_name = 1;
union_name = 'Hello';
```

## Type Guards
Type Guards allows you to narrow down the type of a variable within a conditional block. It is some expression that performs a *runtime check* that guarantees the type in some scope. This ensures that the variable is the type you're expecting at the moment your code is executed.

### `typeof`
`typeof` operator can give very basic information about the type of values we have at runtime. In TypeScript, checking against the value returned by `typeof` is a type guard. Because TypeScript encodes how `typeof` operates on different values, it knows about some of its quirks in JavaScript.

Syntax:
```typescript
typeof operand
typeof(operand)
```

* *operand*: an expression represnting the object or primitive whose type is to be returned

Example:
```typescript
function sum(arg1: string | number, arg: string | number) string | number
{
   if (typeof arg1 === "string")
   {
      return arg1 + arg 2;
   }

   if (typeof arg1 === "number" && typeof arg2 === "number")
   {
      return arg1 + arg2;
   }

   return arg1 + arg2;
}
```

In the example above, we have a function named `sum` that takes two arguments that can be either a string or a number. Inside the function, we've got two conditional statements. The first one checks if the `arg1` is a type of a string and the second one checks if both  is a type of a number. So the two conditional statements are both *type guard*.

### `instanceof`
Similar to the `typeof` operator, TypeScript is also aware of the usage of the `instanceof` operator. It tests to see if the prototype property of a constructor appears anywhere in the prototype chain of an object. The `instanceof` operator tests the presence of `constructor.prototype` in object's prototype chain. This usually means object was constructed with constructor.

Syntax:
```typescript
object instanceof constructor
```

* *object*: object to test
* *constructor*: constructor to test against

## Type Aliases
Type aliases create a new name for a type. They are sometimes similar to interfaces, but can name primitives, unions, tuples, and any other types that you'd otherwise have to write by hand. Aliasing doesn’t actually create a new type – it creates a new name to refer to that type. 

Syntax:
```typescript
// New type is created
type type_alias = number | string | boolean;

// Variable is declared of the new type created
let variable_name: type_alias;
```

Example:
```typescript
// New type is created
type typeStringNumber = string | number;

function sum(arg1: typeStringNumber, arg2: typeStringNumber)
{
   return arg1.toString() + arg2.toString();
}
```

## `null`
It is used when an object does not have any value. Then value `null` represents te intentional absence of any object value. It represents nothing or no value. `null` means we know that the variable does not have any value. TypeScript does not set the value of a variable to `null`. We neeed to do set it explicitly.

### `strictNullChecks` *off*
Values that might be `null` or `undefined` can still be accessed normally, and the values `null` and `undefined` can be assigned to a property of any type.

### `strictNullChecks` *on*
When a value is `null` or `undefined`, you will need to test for those values before using methods or properties on that value.

### Non Nullable
To make variables of other data types *nullable*, we need to explicitly specify it. We can make use of the union type, which allows us to construct a type that is a union of two or more types.

```typescript
let var_name: number | null | string;
```

## `undefined`
Denotes value given to uninitialized variable. It means the value is not assigned or we do not know its value. `undefined` is a primitive value and is treated as falsy for boolean operations. It is a primitive value used when a variable has not been assigned a value.

Example:
```typescript
let var_name: number;
console.log(var_name);
```

Output:
```
undefined
```

The following example declares the variable of type number but we have not given it any initial value. By default, it gets the value of `undefined`.

## Reference
* [Union Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)
* [TypeScript - Union](https://www.tutorialsteacher.com/typescript/typescript-union)
* [Null in TypeScript](https://www.tektutorialshub.com/typescript/null-in-typescript/)
* [TypeScript union Type](https://www.typescripttutorial.net/typescript-tutorial/typescript-union-type/)
* [TypeScript Type Guards](https://www.typescripttutorial.net/typescript-tutorial/typescript-type-guards/)
* [Undefined in TypeScript](https://www.tektutorialshub.com/typescript/typescript-undefined/)
* [What are type aliases and how to create it in Typescript ?](https://www.geeksforgeeks.org/what-are-type-aliases-and-how-to-create-it-in-typescript/)