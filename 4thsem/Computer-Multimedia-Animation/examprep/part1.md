---
order: 1
title: CMA - "Exam Preparation" Part1
---
# Computer Multimedia Animation
# Faculty-Shared Solved Questions, Part 1

## What is CSS? Explain difference between styles in CSS.
- CSS[Cascading Style Sheets] is a style sheet language used to describe the presentation and visual appearance of HTML and XML documents.
    1. ***Inline Styles***: Inline style are applied directly to html elements using the style attribute. Inline style have high specific but the code result in code duplication if used externally.   
    - EXAMPLE:
        ```html
        <p style="color: blue; font-size: 16px;">
        ```
    2. ***Internal Styles***: This are defined within the `<style>` tag within document CSS rules are written directly with style block, allows to define syles for specific for specific html elements within the same html file.
    - EXAMPLE:
        ```html
        <head>
            <style>
                color: blue;
                font-size: 16px;
            </style>
        </head>
        ````
    3. ***External Styles***: This are the separates CSS files linked to html documents using the `<link>` tag. There are rules within the external CSS file, which is referenced in the `href` attribute of the `<link>` tag.
    - EXAMPLE:
        ```html
        <head>
            <link ref="stylesheet" href="styles.css">
        </head>
        ```  
         
    4. [OTHER]***CSS Framework:*** It is like a bootstrap foundation and Bulma offer pure-designed styles, layout systems and components.

## What is JavaScript and it's features.
- JS[JavaScript] is a high-level programming language primarily used for the client-side web development.
- Features: 
    1. ***Client-Side***: It runs on the user's browser.
    2. ***Versatile***: JS can be used for wide range of tasks, from simple calculation to complex server-side application.
    3. ***Dynamic Typing***: JS is a dynamically typed language which means types of variable are defined based on stored values.

## Explain about `<a>` tag: `href`, `target` and `name` attributes.
- `<a>` tag: This tag is also known as anchor tag used to create hyperlinks in HTML and it allows navigate to other web pages, email address or locations within the same page.
    1. ***`href`[HyperText Reference]***: It specifies the URL of the link. It can be an absolute or a relative URL.  
    EXAMPLE:
    `/examprep`
    2. ***`target`***: It specifies where to open the link.
        - `_blank`: Opens the link in a new tab or window.
        - `_self`[default]: Opens the link in the same tab or window.
        - `_parent`: Opens the link in the parent frame.
        - `_top`: Opens the link in full page.
    3. ***`name`***: It specifies a name for the "anchor". This attributes is used for book marking purpose, allowing users to create a link to a specific section of a page.
- EXAMPLE:
```html
<a href="https://www.github.com/jack-pots/" target = "_blank" name = "github-account">
    SIGMA MALE
</a>
```

## Briefly describe alert() and confirm() methods in JavaScript.
- ***`alert()`***:
    - Displays a message box with a specified message.
    - It is used to display the warning or error message to the user.
    - It is used to provide information to the user, such as a confirmation message.
    - It is used in debugging purposes to display variable values or other information.
    - EXAMPLE:
        ```javascript 
        alert("Hello!") 
        ```
- ***`confirm()`***: 
    - It is used to display a dialog box with specified message and two button and two button: OK and Cancel.
    - It is used to confirming users actions, such as deleting a file or submitting a form.
    - EXAMPLE:
        ```javascript
        confirm("Speed your computer by deleting System32");
        ```
        