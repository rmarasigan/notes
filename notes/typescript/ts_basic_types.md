# TypeScript – Basic Types

## Types
The Type System checks the validity of the supplied values, before they are stored or manipulated by the program. This ensures the code behaves as expected.

### Built-in Types

#### Primitives: `string`, `number` and `boolean`
* `string`
   * Represents string values
   * It is used to represent a sequence of characters
* `number`
   * Double precision 64-bit floating point values
   * It is used to represent both Integer as well as Floating-Point numbers
   * These numbers can be Decimal (base 10), Hexadecimal (base 16) or Octal (base 8)
   ```typescript
   let first: number = 123;         // number 
   let second: number = 0x37CF;     // hexadecimal
   let third: number = 0o377 ;      // octal
   let fourth: number = 0b111001;   // binary
   ```
* `boolean`
   * For the two vales `true` and `false`
   * The upper case `Boolean` is an object type whereas lower case `boolean` is a primitive type.

### Arrays
An array is a collection of values of the same data type. It is a user defined type. Arrays can contain elements of any data type, numbers, strings, or even objects. An array is a type of data structure that stores the elements of similar data type and consider it as an object too. We can store only a fixed set of elements and can’t expand its size, once its size is declared.

Basic syntax:
```typescript
// Declaration
let array_name: Array<string>;

// Initialization
array_name = ["value_1", "value_2", ..., "value_n"];
```

There are two ways to declare an array:
1. Using square brackets.
   ```typescript
   let array_name: string[] = ["value_1", "value_2", ..., "value_n"];
   ```
2. Using a generic array type, `Array<Type>`
   ```typescript
   let array_name: Array<string> = ["value_1", "value_2", ..., "value_n"];
   ```

An array in TypeScript can contain elements of different data types using a generic array type syntax.
```typescript
let array_name: Array<string | number> = ["value_1", value_2, ..., "value_n"];

let array_name: (string | number)[] = ["value_1", value_2, ..., "value_n"];
```

We can also prevent arrays from being changed by using the `readonly` keyword.
```typescript
let names: readonly string[] = ["Manson"];
```

#### Array object
An array can also be created using the Array object. The Array constructor can be passed.
* A numeric value that represents the size of the array
* A list of comma separated values

```typescript
// Declaring an array with its size
var array_name: number[] = new Array(4);

// Declaring an array with comma separated values
var array_name: string[] = new Array("Mary", "Tom", "Manson", "Paulo");
```

### `any`
It is the super type of all types in TypeScript. It denotes a dynamic type. Using the `any` type is equivalent to opting out of type checking for a variable.

Basic syntax:
```typescript
let something: any = "Hello World";
something = 27;
something = true;
```

None of the following lines of code will throw compiler errors. Using `any` disables all further type checking, and you can access any properties of it (which will turn be of type `any`).

### `void`
`void` is used where there is no data. It is generally used on function return-types. The `void` type can't hold any data – it can only be `undefined` (or `null` if the `strictNullChecks` compiler option is off).  It can be inferred, but we can explicitly define it on functions if we prefer. Use the `void` type as the return type of functions that do not return any value.

Basic syntax:
```typescript
function log(message): void
{
   console.log(message);
}
```

It is a good practice to add the `void` type as the return type of a function or a method that doesn’t return any value. By doing this, you can gain the following benefits:
* Improve clarity of the code: you do not have to read the whole function body to see if it returns anything.
* Ensure type-safe: you will never assign the function with the void return type to a variable.

### Tuples
A *tuple* is another sort of `Array` type that knows exactly how many elements it contains, and exactly which types it contains at specific positions. The order of values in a tuple is important. If you change the order of values, you'll get an error. For this reason, it's a good practice to use tuples with data that is related to each other in a specific order.

Basic syntax:
```typescript
let variable_name: [number, string] = [1, "value_1"];

// Declaration
let user: [number, string, number, string, boolean];

// Initialization
user = [1, "Manson", 27, "Admin", true];

// Declaring and initializing an array of tuple
let employee: [number, string][];
employee = [[1, "Manson"], [2, "Paulo"], [3, "Olivia"]];
```

Tuples types have `readonly` variants, and can be specified by sticking a `readonly` modifier in fron of them – just like with array shorthand syntax.
```typescript
let tuple_name: readonly [number, string];
```

#### Optional Tuple Elements
A tuple can have optional elements specified using the question mark (`?`) postfix. Optional tuple elements can only come at the end, and also affect the type of `length`.

Basic syntax:
```typescript
let tuple_name: [number, string, number, boolean?];
tuple_name = [1, "Manson", 27];
```

### `enum`
An enum is a group of named constant values. Enum stands for enumerated type. Enum allows us to declare a set of named constants like a collection fo related values that cna be numeric or string values.

There are three types of enums:
* Numeric enum
* String enum
* Heterogeneous enum

#### Numeric enum
They are number-based enums.

Example:
```typescript
enum PrintMedia {
   Newspaper,
   Newsletter,
   Magazine,
   Book
}
```

Enums are always assigned numeric values when they are stored. The first value always takes the numeric value of 0, while the other values in the enum are incremented by 1. We also have the option to initialize the first numeric value ourselves.

#### String enum
They are similar to numeric enums, except that the enum values are initialized with string values rather than numeric values. The benefits of using string enums is that string enums offer better readability.

Example:
```typescript
enum PrintMedia {
   Newspaper = "NEWSPAPER",
   Newsletter = "NEWSLETTER",
   Magazine = "MAGAZINE",
   Book = "BOOK"
}

// To access the string enum
PrintMedia.NewsPaper;
```

The difference between numeric and string enums is that numeric enum values are auto-incremented, while string enum values need to be individually initialized. String enums allow you to give a meaningful and readable value when your code runs, independent of the name of the enum member itself.

#### Heterogeneous enum
Heterogeneous enum are enums that contain both string and numeric values.

```typescript
enum Status {
   Active = "ACTIVE",
   Deactivate = 1,
   Pending
}
```

## Reference
* [Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
* [TypeScript - Types](https://www.tutorialspoint.com/typescript/typescript_types.htm)
* [TypeScript void Type](https://www.typescripttutorial.net/typescript-tutorial/typescript-void-type/)
* [Data types in TypeScript](https://www.geeksforgeeks.org/data-types-in-typescript/)
* [TypeScript Data Type - Enum](https://www.tutorialsteacher.com/typescript/typescript-enum)
* [Understanding and using the void type](https://learntypescript.dev/03/l3-void)