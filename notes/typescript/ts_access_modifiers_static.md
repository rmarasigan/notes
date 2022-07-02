# TS – Classes | Access Modifiers, Accessor and `static`

## Access Modifers
In object-oriented programming, the concept of *Encapsulation* is used to make class members public or private. For example, a class can control the visibility of tis data members. This is done using access modifiers. It gives direct access control to the class members. These class members are functions and properties. We can use class members inside its own class, anywhere outside the class, or within its child or derived class.

The access modifier increases the security of the class membes and prevents them from invalid use. We can also use it to control the visibility of data members of a class. If the class does ot ahve to be set any access modifier, TypeScript automatically sets public access modifier to all class members.

### `public`
A public data member has universal accessibility. Data members in a class are public by default. So, there is no need to prefix members with this keyword. We can access this data member anywhere without any restriction.

Example:
```typescript
class User
{
   public ID: string;
   FirstName: string;
   LastName: string;

   constructor (user_id: string, first_name: string, last_name: string)
   {
      this.ID = user_id;
      this.FirstName = first_name;
      this.LastName = last_name;
   }
}

let user = new User("0098172018", "Mark", "Manson");
console.log(user.ID);
```

Output:
```
0098172018
```

In the example above, the `ID` is public and  the `FirstName` and `LastName` is declared without a modifer, so TypeScript will treat them as *public* by default. Since the data memebrs are public, they can be accessed outside of the class using an object of the class.

### `private`
Private data members are accessible only within the class that define these members. If an exertnal class member tries to access a private member, the compiler throws an error. It ensures that the class members are visible only to that class in which it is containing.

Example:
```typescript
class User
{
   public ID: string;
   private Name: string

   constructor (user_id: string, full_name: string)
   {
      this.ID = user_id;
      this.Name = full_name;
   }

   public display()
   {
      return(`User ID: ${this.ID} Name: ${this.Name}`);
   }
}

let user = new User("0098172018", "Mark Manson");
console.log(user.display());
```

Output:
```
User ID: 0098172018 Name: Mark Manson
```

In here, we have marked the `Name` as private. Hence, when we create an object `user` and try to access the `user.Name` member, it will give an error. To access the `Name` property, we created a public function that will return a message including the `Name` property.

### `protected`
A protected data member is accessible by the members within the same class as that of the former and also by the members of the child classes. We cannot access it from the outside of a class in which it is containing.

Example:
```typescript
class User
{
   public ID: string;
   protected Name: string

   constructor (user_id: string, full_name: string)
   {
      this.ID = user_id;
      this.Name = full_name;
   }
}

class Employee extends User
{
   private Department: string;

   constructor(user_id: string, full_name: string, department: string)
   {
      super(user_id, full_name);
      this.Department = department;
   }

   public EmployeeDetails()
   {
      return (`User ID: ${this.ID} Employee Name: ${this.Name} Department: ${this.Department}`);
   }
}

let user = new User("0098172018", "Mark Manson", "Software Developer");
console.log(user.EmployeeDetails());
```

Output:
```
User ID: 0098172018 Employee Name: Mark Manson Department: Software Developer
```

In the above example, we can't use the name from outside of `User` class. We can still use it from within an instance of method of `Employee` class because `Employee` class derives from `User` class.

#### `super` keyword
The `super()` keyword is used to call the parent constructor and passes the property values. The type of a `super()` call expression is `void`. We must call `super()` method first before assigning values to properties in the constructor of the derived class.

### `readonly`
The `readonly` keyword makes a property as read-only in the class, type or interface. Prefix `readonly` is used to make a propery as read-only. Read-only members can be accessed outside the class, but their value cannot be changed. Since read-only members cannot be changed outside the class, they either need to be initialized at declaration or initialized inside the class constructor.

The assignment to a `readonly` property can only occur in one of two places:
* In the property declaration
* In the constructor of the same class

To mark a property as immutable, you use the `readonly` keyword.

Syntax:
```typescript
class class_name
{
   readonly property_name: data_type;
}
```

Example:
```typescript
class User
{
    constructor(public id: number, readonly name: string){}
}

let user = new User(98172018, 'Mark Manson');
console.log(`User ID: ${user.id} Name: ${user.name}`);
```

Output:
```
User ID: 98172018 Name: Mark Manson
```

The `user.name` syntax will throw an error because the property cannot be changed.
```typescript
user.name = 'Paulo Coelho';
```

Error:
```
Cannot assign to 'name' because it is a read-only property.
```

#### `readonly` vs `const`
`readonly`                                                    | `const`                |
------------------------------------------------------------- | ---------------------- | 
Class properties                                              | Variables              |
In the declaration or in the constructor of the same class    | In the declaration     |

## Accessor
In TypeScript, the accessor property provides a method to access and set the class members. The greater method control over how a member is accessed on each object.

It has two methods:
* getter
   * Comes when you want to access any property of an object
* setter
   * Comes when you want to change any property of an object

Example:
```typescript
class User
{
   private _id: string;
   private _name: string;
   private _department: string;

   // Getters
   get id() : string
   {
      return this._id;
   }

   get name() : string
   {
      return this._name;
   }

   get department() : string
   {
      return this._department;
   }

   // Setters
   set id(value: string)
   {
      this._id = value;
   }

   set name(value: string)
   {
      this._name = value;
   }

   set department(value: string)
   {
      this._department = value;
   }
}

// Create an instance of User
let user = new User();

// Setting the user name
user.name = "Mark Manson";

// Getting the user name to print
console.log(`User Name: ${user.name}`);
```

Output:
```
User Name: Mark Manson
```

### getter
The getter accessor property is the conventional method which is used for retrieving the value of a variable. In object literal, the getter property denoted by **`get`** keyword. A getter can be a public, private, and protected. It is just artificial to make something behave like a property or a function. 

Syntax:
```typescript
get property_name() {}
```

### setter
The setter accessor property is the conventional method which is used for updating the value of a variable. In object literal, the setter property is denoted by **`set`** keyword.

Syntax:
```typescript
set property_name(value)
{
   obj.property_name = value;
}
```

## `static`
The `static` keyword can be applied to the data members of a class. A static variable retains its values till the program finishes the execution. Static members are referenced by the class name. The static members of a class are accessed using the class name and dot notation, without creating an object.

The static members can be defined by using the keyword `static`. The class or constructor cannot be static in TypeScript.

Syntax:
```typescript
class class_name
{
   static property_name: data_type = data_value;
}
```

Example:
```typescript
class Circle
{
   static PI = 3.14;

   static Area(radius: number)
   {
      return this.PI * radius * radius;
   }

   Circumference(radius: number) : number
   {
      return 2 * Circle.PI * radius;
   }
}

console.log(Circle.Area(48));

let circle = new Circle()
console.log(circle.Circumference(50));
```

Output:
```
7234.5599999999995
314
```

In the above example, the `Circle` class includes a static method `Area` and non-static method `Circumference`. As you can see, the static field `PI` can be accessed in the static method using `this.PI` and in the non-static (instance) method using `Circle.PI`.

### `static` vs `const`
`static`                                      | `const`                                 |
----------------------------------------------- | --------------------------------------- |
Class properties and methods                    | Variables                               |
Can be accessed on the class definition only    | Can be accessed globally or locally     |

## Reference
* [TypeScript - Static](https://www.tutorialsteacher.com/typescript/typescript-static)
* [TypeScript Accessor](https://www.javatpoint.com/typescript-accessor)
* [TypeScript - ReadOnly](https://www.tutorialsteacher.com/typescript/typescript-readonly)
* [TypeScript Access Modifiers](https://www.typescripttutorial.net/typescript-tutorial/typescript-access-modifiers/)
* [TypeScript Access Modifiers](https://www.javatpoint.com/typescript-access-modifiers)
* [TypeScript - Data Modifiers](https://www.tutorialsteacher.com/typescript/data-modifiers)
* [TypeScript Static Methods and Properties](https://www.typescripttutorial.net/typescript-tutorial/typescript-static-methods-and-properties/)