# ES 6 – Classes

## What is Object Oriented Programming (OOP)?
OOP describes a way to write programs. this way focuses on data: stored as object properties, and actions: stored as object methods. In OOP, everything is an object, and any actions we need to perform on data are written as methods of an object.

### Concepts
* **Object**
   * An object is a real-time representation of any entity
   * Every object is said to have 3 features
      * State – described by the attributes of an object
      * Behavior – describes how the object will act
      * Identity – a unique value that distinguishes an object from a set of similar such objects
* **Class**
   * In terms of OOP, it is a blueprint for creating objects. It encapsulates data for the object
* **Method**
   * Facilitate communication between objects

## Class
Classes are template for creating objects. They encapsulate data with code to work on that data. Classes are in fact "special function", and just as you can define function expressions and function declarations, the calss syntax has two components: **class expressions** and **class declarations**. The class contains the **Constructors** and **Functions**. The *Constructors* take responsibility for allocating memory for the objects of the class. The *Function* takes the responsibility of the action of the objects. Combing these two Constructor and Function to make the Class.

### Class Declaration
One way to define a class is using a *class declaration*. To declare a class, you use the `class` keyword with the name of the class.

```javascript
class Rectangle {
   constructor(height, width) {
      this.height = height;
      this.width = width; 
   }
}
```

### Class Expression
Class expression can be named or unnamed. The name given to a named class expression is local to the class's body. However, it can be accessed via the name property.

```javascript
// Unnamed
let Rectangle = class {
   constructor(height, width) {
      this.height = height;
      this.width = width;
   }
};

console.log(Rectanlge.name);

// Named
let Rectangle = class Rectangle2 {
   constructor(height, width) {
      this.height = height;
      this.width = width;
   }
};

console.log(Rectangle.name);
```

### Constructor Function
A constructor function is used to create objects. The `Rectangle()` is an object constructor function. To create an object from a constructor function, we use the `new` keyword.

```javascript
// Constructor function
function Rectangle(width, height) {
   this.width = width;
   this.height = height;
}

// Create an object
let rect = new Rectangle(20, 20);
console.log(rect);
```

Output
```
rectangle {width: 20, height: 20}
```

**NOTE**: It is considered a good practice to capitalize the first letter of your constructor function.

Now, we have a keyword called `class` which help us to create classes.
```javascript
class Person {
   // Constructor function is a special method for creating
   // and initializing object created with a class. There can
   // be only one constructor in a class.
   constructor (name, age, profession) {
      this.name = name;
      this.age = age;
      this.profession = profession;
   }
}

let details = new Person('John', 30, 'Programmer');
console.log(details);
```

Output:
```
Person { name: 'John', age: 30, profession: 'Programmer' }
```

Now that we have a Person object with the age, name and profession. 

### Class Inheritance
We use **`extends`**  to inherit from another class and **`super`** keyword to call the parent class function. We use the **`extends`** keyword to implement the inheritance. The class to be extended is called a *base class* or *parent class*. The class that extends the base class or parent class is called *derived class* or *child class*. The **`super()`** method in the constructor is used to access all parent's properties and methods that are used by the derived class.

```javascript
class Person {
   constructor (name, age) {
      this.Name = name;
      this.Age = age;
   }
}

class Student extends Person {
   constructor (school, grade) {
      // Referring to the parent class constructor.
      // In `super()`, we need to define that we are
      // going to give a value for name and age
      super('John', 30);

      this.School = school;
      this.Grade = grade;
   }
}

let student = new Student('USC', 80);
console.log(student);
```

Output:
```
Student { Name: 'John', Age: 30, School: 'USC', Grade: 80 }
```

How to make the `name` and `age` value dynamically? Basically, we can pass the name and age value in the constructor.
```javascript
class Student extends Person {
   constructor (name, age, school, grade) {
      super(name, age);

      this.School = school;
      this.Grade = grade;
   }
}

let student = new Student('Manson', 27, 'USC', 80);
console.log(student);
```

Output:
```
Student { Name: 'Manson', Age: 27, School: 'USC', Grade: 80 }
```

### Getters and Setters
In this example, the `Person` class has the `name` and `age` property. It is being extended by the class `Student` that has the `school` and `grade` property. Also, it has additional methods like `getName()` and `setName()`.

The `getName()` method returns the value of the `name` property.

The `setName()` methods assigns an argiument to the `name` property.

The `getName()` and `setName()` methods are known as getter and setter. They allow us to run the code on the reading or writing of a property.
```javascript
class Person {
   constructor (name, age) {
      this.Name = name;
      this.Age = age;
   }
}

class Student extends Person {
   constructor (name, age, school, grade) {
      super(name, age);

      this.School = school;
      this.Grade = grade;
   }

   getName() { return this.Name }
   setName(name) { this.Name = name }

   getAge() { return this.age }
   setAge(age) { this.Age = age }

   getSchool() { return this.School }
   setSchool(school) { this.School = school }

   getGrade() { return this.Grade }
   setGrade(grade) { this.Grade = grade }

   getCalculateGrade() {
      let total = 100;
      let studentGrade = this.getGrade();
      let result = total - studentGrade;
      return result;
   }
}

let student = new Student('Manson', 27, 'USC', 80);
console.log(student);

console.log(`Name: ${student.getName()}`);
console.log(student.setName('John'));

console.log(`Name: ${student.getName()}`);
console.log(`Final Grade: ${student.getCalculateGrade()}`);
console.log(student);
```

Output:
```
Student { Name: 'Manson', Age: 27, School: 'USC', Grade: 80 }
Name: Manson
undefined
Name: John
Final Grade: 20
Student { Name: 'John', Age: 27, School: 'USC', Grade: 80 }
```

## Reference
* [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [ES6 - Classes](https://www.tutorialspoint.com/es6/es6_classes.htm)
* [ES6 | Classes](https://www.geeksforgeeks.org/es6-classes/)
* [JavaScript ES6: Classes](https://medium.com/@luke_smaki/javascript-es6-classes-8a34b0a6720a)
* [ES6 — classes and inheritance](https://medium.com/ecmascript-2015/es6-classes-and-inheritance-607804080906)
* [How to implement inheritance in ES6?](https://www.geeksforgeeks.org/how-to-implement-inheritance-in-es6/)