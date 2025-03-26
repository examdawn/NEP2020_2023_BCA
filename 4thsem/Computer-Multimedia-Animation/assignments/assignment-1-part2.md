---
order: 2
title: CMA Assignment 1 Part B
---
# CMA Assignment 1 Part B
(Due on 17/3/2025)
> [!WARNING]
> This Page is incomplete and answers will be added soon. 4/9 Remaining.
## Q9. Explain different ways using stylesheets in HTML
> [!NOTE]
> This Question was already answered [before](./assignment-1#q3-what-is-css-explain-different-styles-in-css)
## Q10. Explain the difference between `<div>`  and `<span>` tag
| `<div>` | `<span>` |
| --- | --- |
| `<div>` is used to group and structure content on a block level | `<span>` is used to provide a container for inline elements and content |
| It is best to attach it to a section of a web page | It is best to attach a CSS to a small section of a line in a web page |
| It accepts align attribute | It does not accept align attribute |
| This tag should be used to wrap a section, for highlighting that section | This tag should be used to wrap any specific word that you want to highlight in your webpage | 

[GeeksForGeeks](https://www.geeksforgeeks.org/difference-between-div-and-span-tag-in-html/)
## Q11. Briefly describe alert() and confirm() methods in JavaScript
### `alert()` method
This is used to give a quick message to the user along with an "OK" button which dismisses the message
- This is good for quick attention-grabbing alerts

Example:
```javascript
alert("Warning: You have run out of free visits")
```
### `confirm()` method
This is used to ask a question to the user
- It displays a custom message along with two buttons:
    - "OK" - `true`
    - "Cancel" - `false`
- It returns the user's action as `true`/`false`

Example:
```javascript
var result = confirm("Do you want to delete this item?"); 
console.log(result);
```


[Hashnode](https://iamdipankarpaul.hashnode.dev/enhancing-user-interaction-with-javascript-a-guide-to-alert-prompt-and-confirm-functions#heading-confirming-user-actions-with-confirm)
## Q12. Explain addeventListener() method with an example
## Q13. Explain the `<form>` tag and its attributes
## Q14. Write a short note on `<aside>` with any of its unique attributes
## Q15. Explain `<input>` tag with element-specific attributes
## Q16. Explain how to define a JavaScript function with a proper example
A javascript function is a block of code meant to performs a specific task that can be run when something "invokes" it.

Here, we use the `function` keyword to create a function. 
- We pass arguments to the functions
- After the operation inside the code block is done, we ask it to return a certain value so that we can use it

Syntax:
```javascript
function MyFunctionName(arguments) {
    // Your Code here
    return something; // return a value after the task is done  
}
```

Example: 
```javascript
function multiply_vars(a, b){
    return (a*b);
}

multiply_vars(5,10); // should return 50
```

[W3Schools](https://www.w3schools.com/js/js_functions.asp)
## Q17. Explain the different ways of linking stylesheets in HTML5
> [!NOTE]
> This Question was already answered [before](./assignment-1#q3-what-is-css-explain-different-styles-in-css)
## Q18. Explain the steps of creating internal and external stylesheets
> [!NOTE]
> This Question was already answered [before](./assignment-1#q3-what-is-css-explain-different-styles-in-css)