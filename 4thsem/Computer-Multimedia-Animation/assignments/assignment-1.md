---
order: 1
title: CMA Assignment 1 Part A(10/3/25)
---
# CMA Assignment 1 Part A(10/3/25)
## Q1. Explan Table tags with suitable examples
- The table tag is used to display Table in a Web Page.
- An HTML table consists of one table element and one or more tr, th, and td elements.
- Abbrivation of Elements
    1. tr -> table row 
    2. th -> table header
    3. td -> table cell.
- An HTML table may also include caption, colgroup, thead, tfoot, and tbody elements 
<sup>[[1](https://www.w3schools.com/tags/tag_table.asp)]</sup>.

EXAMPLE:
```HTML
 <table>
  <tr>
    <th>Car</th>
    <th>Model</th>
  </tr>
  <tr>
    <td>Lotus</td>
    <td>Elva</td>
  </tr>
  <tr>
    <td>Gordon Murray</td>
    <td>T.50</td>
  </tr>
</table> 
```

## Q2. Explain the key features of HTML.
- It is easy to learn and easy to use:
    - HTML has a simple and intuitive syntax, making it accessible for beginners. This allows users to start creating web pages with minimal effort.
- It is platform-independent:
    - HTML works on any operating system or device with a web browser. Users can access HTML content regardless of their device.
- Images, videos, and audio can be added to a web page:
    - HTML supports embedding multimedia elements like images, videos, and audio files. It allows for a richer user experience.
- Hypertext can be added to the text: 
    - HTML enables the creation of hyperlinks that connect to other web pages or resources. This feature is essential for navigation on the web.
- It is a markup language
    - HTML uses tags to define the structure and presentation of web content. These tags indicate how elements should be displayed in a browser 
<sup>[[1](https://www.geeksforgeeks.org/html-introduction/#features-of-html)]</sup>.

## Q3. What is CSS? Explain different styles in CSS
- Cascading Style Sheets (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML. CSS describes how elements should be rendered on screen, on paper, in speech, or on other media. CSS is among the core languages of the open web and is standardized across Web browsers according to W3C specifications <sup>[[1](https://developer.mozilla.org/en-US/docs/Web/CSS)]</sup>.
- This are the types of CSS:
    1. Inline CSS:
    - It involves applying styles directly to individual HTML elements using the style attribute. This method allows for specific styling of elements within the HTML document, overriding any external or internal styles.

    EXAMPLE:
    ```HTML
    <h1 style="font-style: bold">Hello</h1>
    ```
    2. Internal(Embedded) CSS:
    - Its is defined within the HTML document’s style element inside the head section. It applies styles to specified HTML elements. The CSS rule set should be within the HTML file in the head section.

    EXAMPLE:
    ```HTML
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            div {
                text-align: center;
                background-color: green;
            }
        </style>
    </head>

    <body>
        <div>
            <p>Hello</p>
        </div>
    </body>
    </html>
    ```
    3. External CSS:
    - It contains separate CSS files that contain only style properties with the help of tag attributes. CSS property is written in a separate file with a .css extension and it is linked to the HTML document using a link tag inside the head section <sup>[[1](https://www.geeksforgeeks.org/types-of-css-cascading-style-sheet/)]</sup>.

    EXAMPLE:
    ```HTML
    <!-- This is .html -->
    <html>
    <head>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <div>
        <h1>Hello</h1>
      </div>
    </body>
    </html>
    ```

    ```CSS
    /* This is .CSS */
    body {
      background-color: blue;
    }

    div {
      background-color: lightblue;
    }
    ```
## Q4. What is HTML? Mention any two tags in HTML.
- HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content. Other technologies besides HTML are generally used to describe a web page's appearance/presentation (CSS) or functionality/behavior (JavaScript).
- Types of HTML Tags:
  1. Head Tag: HTML element contains machine-readable information (metadata) about the document, like its title, scripts, and style sheets. There can be only one head element in an HTML document. The Syntax is `<head></head>`.
  2. Image Tag: HTML element embeds an image into the document. The Syntax is `<img></img>` <sup>[[1](https://developer.mozilla.org/en-US/docs/Web/HTML)]</sup>.

## Q5. Define JavaScript and its features
JS is an object oriented scripting language used to create dynamically updating content, control multimedia, and even enable more functionality. 
- Browser Support
  - Javascript is supported by most modern up-to-date browsers out of the box unless you explicitly disable it
- Interoperability
  - Javascript works in tandem with other programming, scripting and markup languages
  - It can be embedded into web pages easily
- DOM Manipulation
  - JS allows you to play around with the Document Object Model(interface between HTML and JS)
- Client Side Scripting
  - JS allows running performant client-side code directly on the user's browser for high performance tasks like games and apps(WebGL, WASM, etc) or even more ordinary tasks like Form Validation and Data Processing.


[Mozilla Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)
## Q6. What is the use of cell padding and cell spacing attributes in `<table>`
### Cell Spacing 
The space between two or more cells is called Cell Spacing 

::: details Show code
```HTML
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
table {
  border-spacing: 30px;
}
</style>
</head>
<body>
<h2>Cellspacing</h2>
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Doe</td>
    <td>80</td>
  </tr>
</table>

<p>Change the space between the cells with the border-spacing property. Code credit to W3Schools! Source: https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_border-spacing</p>

</body>
</html>
```
:::
::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/non-lab/cellspacing)

<iframe src="https://sounddrill31.github.io/html-demos/non-lab/cellspacing" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::


### Cell Padding
The space between cell edges and cell content is called the Cell Padding 

::: details Show code
```HTML
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 15px;
}
</style>
</head>
<body>

<h2>Cellpadding</h2>

<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Doe</td>
    <td>80</td>
  </tr>
</table>
<p>Cell padding specifies the space between the cell content and its borders. Code credit to W3Schools! Source: https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_cellpadding</p>
</body>
</html>
```
:::
::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/non-lab/cellpadding)

<iframe src="https://sounddrill31.github.io/html-demos/non-lab/cellpadding" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

[W3Schools](https://www.w3schools.com/html/html_table_padding_spacing.asp)
## Q7. What are the uses of `==` and `!=` operators in JavaScript?
`==`, `!=`, etc come under `Comparison Operators`. They're used to compare the values of the given operands.
- `==` is used to check if the operand on the left is equal to the one on the right or not
  - eg. 
  ```javascript
  let x = 5;
  console.log(x == 5); //true
  ```
- `!=` is used to check if the operand on the left is equal to the one on the right or not
  - eg.
    ```javascript
    let x = 5;
    console.log(x != 5); //false
    ```
## Q8. Explain about `<a>` tag, href, target and name attributes
### `<a>` Tag and `href` and `target` attributes
We use the `<a>` tag to specify a hyperlink or image.
- Syntax: `<a href="path or url" target="location on doc" name="somename">Some Text</a>`
- Example: `<a href="https://google.com" target="_blank" name="googlelink">Text Link</a>`
- This is used to link from one page to another or load an image, even from an external source
- `href` specifies the path to the file
  - It can be a relative path like `search/index.html`
    - Let's say we are on `https://google.com`, this will lead us to `https://google.com/search`
  - It can be an absolute path like `/posts/index.html`
    - Let's say we are on `https://google.com/search` now, this will lead us to `https://google.com/posts`
  - It can also be a link to an external page[like this](https://www.wikipedia.org/) <!-- This isn't straight html but vitepress renders to html so it's all the same :P -->
- `target` specifies where the link should lead to on the page

  | Value | 	Description |
  | --- | --- |
  | _blank |	Opens the linked document in a new window or tab |
  | _self | Opens the linked document in the same frame as it was clicked (this is default) |
  | _parent |	Opens the linked document in the parent frame |
  | _top | Opens the linked document in the full body of the window |
  | framename |	Opens the linked document in the named iframe |
### `name` attribute
The `name` attribute is used to specify an easily identifiable name for an HTML element.
- We can use it to reference this element later from other elements


[W3Schools(Tag `<a>`)](https://www.w3schools.com/tags/tag_a.asp)

[W3Schools(Target)](https://www.w3schools.com/Tags/att_a_target.asp)
