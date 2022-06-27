# ECMA 6 – Template Strings

Template literals (template strings) are literals delimited with backtick (`), allowing for multi-line strings, for string interpolation with embedded expressions, and for special constructs called [tagged templates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates). Template strings allow you to embed code expressions within string literals.


## Without template strings

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset = "UTF-8">
   <meta http-equiv = "X-UA-Compatible" content = "IE=edge">
   <meta name = "viewport" content = "width=device-width, initial-scale=1.0">
   <title>
      TypeScript Course
   </title>
</head>
<body>
   <script src = "script.js"></script>
</body>
</html>
```

#### script.js
```javascript
function print(name, age, profession, gender)
{
   document.write("Name: " + name);
   document.write("Age: " + age);
   document.write("Profession: " + profession);
   document.write("Gender: " + gender);
}

print("Robert", 29, "Developer", "male");
```

Output:
```
Name: RobertAge: 29Profession: DeveloperGender: male
```

As you can see, it doesn't have the spaces within so it is taking a lot more work to finish that. If you want to go to the next line, you are going to add `document.write('<br>').`
```javascript
document.write("Name: " + name);
document.write('<br>');
```

Output:
```
Name: Robert
Age: 29Profession: DeveloperGender: male
```

## With template strings

#### script.js
```javascript
function print(name, age, profession, gender)
{
   document.write(`Name: ${name}
                  Age: ${age}
                  Profession: ${profession}
                  Gender: ${gender}`);
}

print("Robert", 29, "Developer", "male");
```

Output:
```
Name: Robert Age: 29 Profession: Developer Gender: male
```

As you can see, it got all the spaces in between. If you add a `<br>`, it will go create a new line.
```javascript
document.write(`Name: ${name} <br>
               Age: ${age} <br>
               Profession: ${profession} <br>
               Gender: ${gender} <br>`);
```

Output:
```
Name: Robert
Age: 29
Profession: Developer
Gender: male
```

## Reference
* [Template literals (Template strings)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)