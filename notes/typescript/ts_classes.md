# TS – Classes

TypeScript introduced classes so that they can avail the benefits of object-oriented techniques like encapsulation and abstraction. The class in TypeScript is compiled to plain JavaScript functions by the TypeScript compiler to work across platforms and browsers. Classes are blueprints that define the shape and structure of an object. A class in TypeScript can hold any number of properties, functions, “getters” and “setters”. With classes, you can perform encapsulation by assigning different access modifiers (such as public, private and protected). In terms of OOPs, a class is a *template* or *blueprint* for creating objects. It is a logical entity.

A class can include the following:
* Constructor
* Properties
* Methdos

Syntax:
```typescript
class class_name {}
```

The `class` keyword is followed by the class name. The rules for identifiers must be considered while naming a class. A class definition can include the following:
* **Constructors**
   * Responsible for allocating memory for the objects of the class.
* **Properties/Fields**
   * Any variable declared in a class. It represent data pertaining to objects.
* **Methods/Functions**
   * Represent actions an object can take. They are also at times referred to as methods.

Some of the features of a class are:
* Inheritance
* Encapsulation
* Polymorphism
* Abstraction

## Constructors
Class constructors are very similar to functions. You can add parameters with type annotations, default values and overloads. Constructors are used to instantiate object of the class type with the variables of it initialized to specific values.

To define a constructor for a class, use the `constructor` keyword followed the list of variables enclosed in parenthesis, and then body of constructor enclosed in flower brackets. In the constructor, we can access the member of a class by using `this` keyword.

Syntax:
```typescript
class class_name {
   variable_name1: data_type;
   variable_name2: data_type;

   constructor(variable_1: data_type, variable_2: data_type)
   {
      this.variable_1 = variable_1;
      this.variable_2 = variable_2;
   }
}
```

Example:
```typescript
class Point
{
   x: number;
   y: number;

   constructor (x = 0, y = 0)
   {
      this.x = x;
      this.y = y;
   }
}
```

There are just few differences between class constructor signatures and function signatures:
* Constructor can't have type parameters – these belong on the outer class declaration
* Constructor can't have return type annotations – the class instance type is always what's returned

## Methods
A function property on a class is called a *method*. Methods can use all the same type annotations as function and constructors. It is similar to a function used to expose the behaviour of an object.

Advantage of Method:
* Code Reusability
* Code Optimization

Example:
```typescript
// Defining a Point class
class Point
{
   // Defining fields
   x: number;
   y: number;

   constructor(x: number, y: number)
   {
      this.x = x;
      this.y = y;
   }

   // Creating method or function
   scale(n: number): void
   {
      this.x *= n;
      this.y *= n;

      console.log(`X: ${this.x} Y: ${this.y}`);
   }
}

// Creating an object or instance
let obj = new Point(5, 24);
obj.scale(10);
```

Output:
```
X: 50 Y: 240
```

## Inheritance
Inheritance is the ability of a program to create new classes from an existing class. The class that is extended to create newer classes is called *parent class* or *super class*. The newly created classes are called the *child/sub class*. A class inherits from another class using the `extends` keyword. Child classes inherit all properties and methods except private members and constructors from the parent class. We can not implement hybrid and multiple inheritances using TypeScript. The inheritance uses class-based inheritance and it can be implemented using extends keywords in typescript.

```typescript
// Parent / Super / Base Class
class parent_class_name {}

// Child / Sub / Derived Class
class child_class_name extends parent_class_name {}
```

Inheritance can be classified as:
* **Single**
   * Every class can at the most extend from one parent class.
   * The properties and behaviour of the base class can be inherited into at most one derived class. It is used to add new functionality to the already implemented class.
* **Multi-level**
   * The derived class acts as the base class for another derived class. The newly created derived class acquires the properties and behavor of other base classes.

### Why use inheritance?
* We can use it for Method Overriding (so runtime polymorphism can be achieved)
* We can use it for code reusability

### Single Inheritance
Single inheritance can inherit properties and behaviour at most *one parent class*. It allows a derived/child class to inherit the properties and behaviour of a base/parent class that enable the code reusability as well as we cann add new features to the existing code. It makes the code less repetitive.

Example:
```typescript
class Shape
{
   Area: number;

   constructor (area: number)
   {
      this.Area = area;
   }
}

class Circle extends Shape
{
   display() : void
   {
      console.log(`Area of the circle: ${this.Area}`);
   }
}

var obj = new Circle(320);
obj.display();
```

Output:
```
Area of the circle: 320
```

#### Multi-level Inheritance
When a derived class is derived from another derived class, then this type of inheritance is known as *multi-level inheritance*. Thus, a multilevel inheritance has more than one parent class. It is similar to the relation between Grandfather, Father, and Child.

Example:
```typescript
class Animal
{
   eat() : void
   {
      console.log("Eating");
   }
}

class Dogs extends Animal
{
   bark() : void
   {
      console.log("Barking");
   }
}

class Puppy extends Dogs
{
   weep() : void
   {
      console.log("Weeping");
   }
}

let obj = new Puppy();
obj.eat();
obj.bark();
obj.weep();
```

Output:
```
Eating
Barking
Weeping
```

## Class Implements Interface
A class can implement single or multiple interfaces. It implements the interface by using the `implements` keyword.

Example:
```typescript
// Defining interface for class
interface User
{
   first_name: string;
   last_name: string;
   age: number;
   FullName(): string;
   GetAge(): number;
}

// Implementing the interface
class Employee implements User
{
   first_name: string;
   last_name: string;
   age: number;

   constructor (first_name: string, last_name: string, age: number)
   {
      this.first_name = first_name;
      this.last_name = last_name;
      this.age = age;
   }
   
   FullName() : string
   {
      return `${this.last_name}, ${this.first_name}`;
   }

   GetAge() : number
   {
      return this.age;
   }
}

// Create an instance of Employee
// Using the class that implements interface
let employee = new Employee('Mark', 'Manson', 27);
let fullname = employee.FullName();
let age = employee.GetAge();

console.log(`Employee Name: ${fullname} Age: ${age}`);
```

Output:
```
Employee Name: Manson, Mark Age: 27
```

In the above example, we have declared `User` interface with `first_name`, `last_name`, `age` as property and `FullName()` and `GetAge()` as method/function. The `Employee` class implements this interface by using the `implements` keyword. After implementing an interface, we must declare the properties and methods in the class. If we do not implement those properties and methods, it throws a compile-time error. We have also declared a constructor in the class. So when we instantiate the class, we need to pass the necessary parameters otherwise it throws an error at compile time.

## Reference
* [TypeScript Class](https://www.typescripttutorial.net/typescript-tutorial/typescript-class/)
* [TypeScript Classes](https://www.javatpoint.com/typescript-classes)
* [TypeScript - Classes](https://www.tutorialsteacher.com/typescript/typescript-class)
* [TypeScript - Classes](https://www.tutorialspoint.com/typescript/typescript_classes.htm)
* [TypeScript Interface](https://www.javatpoint.com/typescript-interface)
* [TypeScript Inheritance](https://www.javatpoint.com/typescript-inheritance)
* [Everyday Types - Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)
* [TypeScript Tutorial: Beyond the Basics](https://www.itprotoday.com/programming-languages/typescript-tutorial-beyond-basics)
* [How to implement Inheritance in Typescript ?](https://www.geeksforgeeks.org/how-to-implement-inheritance-in-typescript/)
* [Top 50 TypeScript Interview Questions & Answers You Should Know in 2020](https://morioh.com/p/2b395e280dc7)