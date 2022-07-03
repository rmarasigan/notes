# TS – Generics

TypeScript Generics is a tool which provides a way to create **reusable** components. It creates a component that can work with **variety of data types** rather than a single data type. It allows users to consume these components and use their own types. Generics ensures that the program is flexible as well as scalable in the long term. Generics provides type safety without compromising the performance, or productivity.

Generics offer a way to create reusable components. Generics provide a way to make components work with any data type and not restrict to one data type. So, components can be called or used with a variety of data types. Generics use a special kind of type variable `<T>` that denotes **types**. The generic collections contain similar types of objects. The generic types specified inside the angle brackets `<>` are therefore also known as *generic type parameters* or juect *type parameters*.

Syntax:
```typescript
function generic_name <T> (parameter: T): T
{
   return parameter;
}
```

The `<T>` allows you to capture the type that is provided at the time of calling the function. Also, the function uses the `<T>` type as its return type. By convention, we use the `T` as the type variable. However, you can freely use other letters such as `A`, `B`, `C`, etc. Generics can appear in functions, types, classes and interfaces.

There are two ways to use the generic function. You can expilictly pass the data type as the `T` into the function or let the TypeScript compiler set the value of `T` automatically based on the type of argument that you pass into.

Example:
```typescript
// Defining the data type
let id = generic_name<number>(98172018);
console.log(`ID: ${id}`);

// Passing the value
let message = generic_name("Hello, world!");
console.log(`Message: ${message}`);
```

Output:
```
Message: Hello, world!
ID: 98172018
```

In generics, the type variable only accepts the particular type that the user provides at declaration time. It also preserving the type checking information.

Example:
```typescript
function getItems <T> (items: T[]): T[]
{
   return new Array<T>().concat(items);
}

let users = getItems<string>(['John', 'Mark', 'Paulo']);
console.log(`Users: ${users}`);

let user_id = getItems([98172018, 98182018, 98182018]);
console.log(`Users ID: ${user_id}`);
```

Output:
```
Users: John,Mark,Paulo
Users ID: 98172018,98182018,98182018
```

The `getItems` functions accepts a generic type parameter `T`, which is the type of the first argument, then set the return type to be the same with `: T`. The `user_id` has the type of a number. TypeScript here is inferring the generic type from the calling code itself. This way, the calling code does not need to pass any type parameters.

We can also define multi-type variables with a different name. The `displayDetails()` function displays two objects with the type `T` and `U`.

Example:
```typescript
function displayDetails <T, U>(id: T, details: U): void
{
   console.log(`ID: ${id} \n Details: ${details} \n Data Type of details: ${typeof details}`);
}

displayDetails<number, string>(98172018, "Paulo Coelho");
```

Output:
```
ID: 98172018 
Details: Paulo Coelho 
Data Type of details: string
```

### Advantages of Generics
There are mainly three advantages of generics:
1. **Type-safety**: We can hold only a single type of objects in generics. It doesn't allow to store other objects.
2. **Typecasting is not required**: There is no need to typecast the object.
3. **Compile-Time Checking**: It is checked at compile time so the problem will not occur at runtime.

## Types
Generic types are commonly used to create helper types, especially when using mapped types. TypeScript provides many pre-built helper types.

Syntax:
```typescript
type IdentityType <T> = T;
```

Example:
```typescript
type IdentityType <T> = T;
type IsNumber = IdentityType<number>;
```

## Constraints
A constraint is specified after the generic type in the angle brackets. A type constraint is a *rule* that narrows down the possibilities of what a generic type could be. Tyoe constraint are a very powerful way to supercharge your TypeScript codbases.

Syntax:
```typescript
function generic_name <T extends some_type, U extends some_type> (parameter_1: T, paremter_2: U) {}
```

The constraint `<T extends some_type>` specifies that the generic type `T` must extend the `some_type` that you entered.

## Interfaces
A generic interface has generic type parameter list in an angle brackets `<>` following the name of the interface. This make the paramter `T` visible to all members of the interface.

Syntax:
```typescript
interface interface_name <T> {}
```

A common use case for a generic interface is a generic form interface. This is because all forms have values, validation errors, etc., but the specific fields and validation rules differ form form to form. Using generic interfaces allows generic object types to be created that we can make specifc by supplying our types as parameters.

Example:
```typescript
interface KeyValuePair <T, U>
{
   key: T;
   value: U;
}

let user: KeyValuePair <number, string> = {key: 98182018, value: 'Steve'};
console.log(user);

let item: KeyValuePair <string, string> = {key: 'S202R20307S', value: 'Half-size pallet 22100'};
console.log(item);
```

Output:
```
{
  "key": 98182018,
  "value": "Steve"
}
{
  "key": "S202R20307S",
  "value": "Half-size pallet 22100"
}
```

As you can see, by using generic interface as type, we can specify the data type of key and value. The generic interface can also be implemented in the class, same as the non-generic interface.

## Classes
TypeScript also support generic classes. The generic type parameter is specified in angle brackes (`<>`) following the name of the class. A generic class can have generic fields or methods.

Syntax:
```typescript
class class_name <T, U>
{
   private property_1: T
   private property_2: U

   setValue(property_1: T, property_2: U): void
   {
      this.property_1 = property_1;
      this.property_2 = property_2;
   }
}
```

Example:
```typescript
class KeyValuePair <T, U>
{
   private Key: T;
   private Value: U;

   SetKVP (key: T, value: U): void
   {
      this.Key = key;
      this.Value = value;
   }

   Display(): void
   {
      console.log(`Key: ${this.Key} Value: ${this.Value}`);
   }
}

let user = new KeyValuePair;
user.SetKVP(98172018, 'Paulo Coelho');
user.Display();

let item = new KeyValuePair<number, string>();
item.SetKVP(1234567890, 'Washed Gray Pallet');
item.Display();
```

Output:
```
Key: 98172018 Value: Paulo Coelho
Key: 1234567890 Value: Washed Gray Pallet
```

In the above example, we created a generic class named `KeyValuePair` with a type variable in the angle brackets `<T, U>`. The `KeyValuePair` class includes two private generic member variables and a generic function `SetKVP` that takes two input arguments of type `T` and `U`. This allows us to create an object of `KeyValuePair` with any type of key and value.

The generic class can also implement a generic interface. In the example below,  the generic class `KVP` implements the generic interface `KeyValuePair`. `KVP` class can be used with any type of key and value. Two variables are defined as generic interface type, one without underlying types and one with underlyring types for `T` and `U`.

Example:
```typescript
interface KeyValuePair <T, U>
{
   process(key: T, value: U): void;
}

class KVP <T, U> implements KeyValuePair <T, U>
{
   process(key: T, value: U): void
   {
      console.log(`Key: ${key} Value: ${value}`);
   }
}

let user = new KVP;
user.process("98182018", 'Mark Manson');

let item = new KVP<number, string>();
item.process(9876543210, 'Black Pallet');
```

Output:
```
Key: 98182018 Value: Mark Manson
Key: 9876543210 Value: Black Pallet
```

## Reference
* [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)
* [TypeScript Generics](https://www.javatpoint.com/typescript-generics)
* [TypeScript Generics](https://www.typescripttutorial.net/typescript-tutorial/typescript-generics/)
* [TypeScript - Generics](https://www.tutorialsteacher.com/typescript/typescript-generic)
* [Creating generic interfaces](https://learntypescript.dev/06/l3-generic-interfaces)
* [TypeScript Generic Interfaces](https://www.typescripttutorial.net/typescript-tutorial/typescript-generic-interfaces/)
* [TypeScript - Generic Interface](https://www.tutorialsteacher.com/typescript/typescript-generic-interface)
* [How To Use Generics in TypeScript](https://www.digitalocean.com/community/tutorials/how-to-use-generics-in-typescript)