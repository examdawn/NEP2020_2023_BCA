---
order: 0
title: CMA Assignment 1(10/3/25)
---
# CMA Assignment 1(10/3/25)
## Q1. Explan Table tags with suitable examples
- The table tag is used to display Table in a Web Page.
- An HTML table consists of one table element and one or more tr, th, and td elements.
- Abbrivation of Elements
    1. tr -> table row 
    2. th -> table header
    3. td -> table cell.
- An HTML table may also include caption, colgroup, thead, tfoot, and tbody elements.
<sup>[[1](https://www.w3schools.com/tags/tag_table.asp)]</sup>
- Example:
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
    - HTML uses tags to define the structure and presentation of web content. These tags indicate how elements should be displayed in a browser.
<sup>[[1](https://www.geeksforgeeks.org/html-introduction/#features-of-html)]</sup>

## Q3. What is CSS? Explain different styles in CSS

## Q4. What is HTML? Mention any two tags in HTML
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

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/non-lab/cellspacing)

<iframe src="https://sounddrill31.github.io/html-demos/non-lab/cellspacing" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::


### Cell Padding
The space between cell edges and cell content is called the Cell Padding 
::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/non-lab/cellpadding)

<iframe src="https://sounddrill31.github.io/html-demos/non-lab/cellpadding" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

[W3Schools](https://www.w3schools.com/html/html_table_padding_spacing.asp)
## Q7. What are the uses of `==` and `!=` operators in JavaScript?
`==`, `!=`, etc come under `Comparison Operators`. They're used to compare the values of the given operands.
- `==` is used to check if the operand on the left is equal to the one on the right or not
  - eg. If the value of x is 5, `x==5` will return true, `x==6` will return false
- `!=` is used to check if the operand on the left is equal to the one on the right or not
  - eg. If the value of x is 5, `x!=5` will return false, `x!=6` will return true
## Q8. Explain about `<a>` tag, href, target and name attributes
### `<a>` Tag and `href` and `target` attributes
We use the `<a>` tag to specify a hyperlink or image.
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
<!--9. Explain different ways using style sheet in HTML?
10. Explain the difference between <div>  and <span> tag?
11. Briefly describe alert() and confirm() methods in java script?
12. Explain addeventListener() method with example?
13. Explain the<form> tag and its attributes?
14. Write a short note on  <aside> with  any of its unique attributes?
15. Explain <input> tag with element specific attributes?
16. Explain how to define a  JavaScript function  with proper Example?
17. Explain different ways linking style sheet in HTML5?
18. Explain the steps of creating internal and external style sheet?
-->