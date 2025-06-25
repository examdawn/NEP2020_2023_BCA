---
order: 1
title: CMA Previous Paper 2023
---
# PYQs(2023)

# SECTION-A (6x2=12) 
## Q1. What is HTML? Mention any two tags in HTML. 
HTML(Hypertext Markup Language) is the markup language used to structure documents displayed in a web browser. 
- We usually use CSS(Cascading StyleSheets) for Styling
- and Javascript for more advanced logic 

- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: Defines headings of different levels, with `<h1>` being the most important. 
- `<p>`: Represents a paragraph of text. 
- `<a>`: Defines a hyperlink (link to another page or section of the same page)
## Q2. Define Javascript.
JavaScript (JS) is a lightweight interpreted (or just-in-time compiled) programming language with functions. 
- While it is most well-known as the scripting language for Web pages, it is also used on many non-browser environments
- JavaScript is a prototype-based, multi-paradigm, single-threaded, dynamic language, supporting object-oriented, imperative, and declarative (e.g., functional programming) styles.

[Mozilla Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
## Q3. Define animation and multimedia.
Multimedia is used primarily to create interactive experiences that engage and inform the audience. 
- It can be used for educational or training purposes, advertising, gaming, or any other application where an interactive experience is desired 

Animation, on the other hand, is primarily used to create visual effects or tell a story through moving images. 
- It is often used in film and television, advertising, and gaming to create compelling visuals that engage the audience

[GeeksForGeeks](https://www.geeksforgeeks.org/difference-between-multimedia-and-animation/)
## Q4. What are End and Start state in animation. 
CSS animations make it possible to animate transitions from one CSS style configuration to another. 

Animations consist of two components: 
- a style describing the CSS animation
- a set of keyframes that indicate the start and end states of the animation's style, as well as possible intermediate waypoints

A smooth animation may be generated between the provided start and end states

[Mozilla Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)
## Q5. Define SVG. 
Scalable Vector Graphics (SVG) is an XML-based markup language for describing two-dimensional based vector graphics.
- As such, it's a text-based, open Web standard for describing images that can be rendered cleanly at any size and are designed specifically to work well with other web standards including CSS, DOM, JavaScript, and SMIL. 
- SVG is, essentially, to graphics what HTML is to text.

[Mozilla Web Docs](https://developer.mozilla.org/en-US/docs/Web/SVG)
## Q6. Mention the usage of `<Filter>` element in SVG. 
SVG filters are used to add special effects to SVG graphics.
- All SVG filters are defined within a `<defs>` element. The `<defs>` element is short for "definitions", and contains definition of special elements (such as filters).
- The `<filter>` element is used to define an SVG filter. 
- The `<filter>` element has a required id attribute which identifies the filter. The graphic/image then points to the filter to use.
- Then, inside the `<filter>` element, we put one or more filter effects to use on the graphic.

[W3Schools](https://www.w3schools.com/graphics/svg_filters_intro.asp)
## Q7. What is canvas rendering context in HTML? 
The CanvasRenderingContext2D interface, part of the Canvas API, provides the 2D rendering context for the drawing surface of a `<canvas>` element. 
- It is used for drawing shapes, text, images, and other objects.

[Mozilla Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)
## Q8. What is purpose of `<canvas>` in HTML? 
The `<canvas>` HTML element provides a surface for drawing graphics via JavaScript. 
- It acts as a container for drawing and is transparent by default, 
    - meaning it doesn't have a background color or predefined content
## Q9. What are the transformations in HTML5 in canvas? 
With transformations we can translate the origin to a different position, rotate and scale it.

The six methods for transformations are:
- `translate()` - moves elements on the canvas to a new point in the grid
- `rotate()` - rotates elements on the canvas clockwise or counter-clockwise
- `scale()` - scales elements on the canvas up or down
- `transform()` - multiplies the current transformation with the arguments described
- `resetTransform()` - resets the the current transformation to the identity matrix
- `setTransform()` - resets the the current transformation to the identity matrix, and then runs a transformation described by the arguments

[W3Schools](https://www.w3schools.com/graphics/canvas_transformations.asp)
# SECTION-B (4x6=24) 
# Q10. Explain table tags with a suitable example. 
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
From [Assignment-1](../assignments/assignment-1.md#q1-explain-table-tags-with-suitable-examples)
# Q11. Explain the key features of HTML5. 
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

From [Assignment-1](../assignments/assignment-1.md#q2-explain-the-key-features-of-html)

# Q12. Differentiate between long hand and short hand properties
- CSS transitions can be defined using both longhand and shorthand properties. These two approaches offer distinct levels of control or convenience for specifying transition effects.
    1. ***Longhand Properties***: They  are CSS properties that are written out in full, with each individual aspect of the transition such as the properties being transitioned, the duration the timing function and the delay.
    - EXAMPLE:
        ```css
        .ballontop {
            transition-property: width;
            transition-duration: 1s;
            transition-timing-function: ease-in-out;
            transition-delay: 0.2s;
        }
        ```
    2. ***Shorthand Properties***: It allows to specify multiple properties in a single line of code. Shorthand properties offer a more concise way to declare transition by combining multiple aspects into a single property called transition.
    - EXAMPLE:
        ```css
        transition: width 1s case-on-out 0.2s;
        ```

    | ***Aspects*** | ***Longhand Properties*** | ***Shorthand Properties*** |
    |---------|---------------------|----------------------|
    | NO. OF DECLARATION | For separate declaration for property, duration. | A single declaration combining all aspects.  |
    | CONTROL | Provides precise control over each aspects. | Offers more concise way to declare. |
    | READABILITY | May result in longer, more detailed code. | Provides a compact and readable declaration. |
    | FLEXIBILITY | Allows different properties to have individual settings. | Suitable for straightforward transitions. |


# Q13. Write a HTML program to draw a rectangle in SVG. 
```html
<html>
	<head>
    	<title>Rectangle</title>
    </head>
    <body>
    	<svg width="200" height="100">
        	<rect x="10" y="10" width="150" height="80" style="fill:white;stroke-width:1;stroke:black"/>
        </svg>
    </body>
</html>
```

<iframe src="https://sounddrill31.github.io/html-demos/non-lab/rectangle" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

# Q14. Explain the two types of rendering contexts in canvas. 
- `"2d"`
    - Creates a CanvasRenderingContext2D object representing a two-dimensional rendering context.
- `"webgl"` (or "experimental-webgl")
    - Creates a WebGLRenderingContext object representing a three-dimensional rendering context. This context is only available on browsers that implement WebGL version 1 (OpenGL ES 2.0).
- `"webgl2"`
    - Creates a WebGL2RenderingContext object representing a three-dimensional rendering context. This context is only available on browsers that implement WebGL version 2 (OpenGL ES 3.0).
- `"webgpu"`
    - Creates a GPUCanvasContext object representing a three-dimensional rendering context for WebGPU render pipelines. This context is only available on browsers that implement The WebGPU API.
- `"bitmaprenderer"`
    - Creates an ImageBitmapRenderingContext which only provides functionality to replace the content of the canvas with a given ImageBitmap

[Mozilla Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext#contexttype)
# Q15. Describe the different methods used in canvas transform. 
 Canvas transformation methods allow you to manipulate the drawing area, affecting how elements are drawn and displayed. 
 
 
These methods include `translate()`, `rotate()`, `scale()`, `transform()`, `resetTransform()`, and `setTransform()`. 
- `translate(x, y)`:
    - Moves the canvas origin to a new position, shifting the drawing area horizontally by x units and vertically by y units. 
- `rotate(angle)`:
    - Rotates the canvas clockwise around the current origin by the specified angle (in radians). 
- `scale(x, y)`:
    - Scales the canvas and its elements horizontally by x and vertically by y. If x and y are equal, it's a uniform scaling. 
- `transform(a, b, c, d, e, f)`:
    - Applies a more general transformation matrix, enabling scaling, rotation, skewing, and translation, according to RGraph. 
- `resetTransform()`:
    - Resets the transformation matrix to the identity matrix, effectively undoing all previous transformations. 
- `setTransform(a, b, c, d, e, f)`:
    - Resets the transformation matrix to the identity matrix and then applies the specified transformation described by the parameters a, b, c, d, e, and f, according to W3Schools. 

# SECTION-C (3x8=24) 
## Q16. What is CSS? Explain the different styles in CSS. 
- Cascading Style Sheets (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML. CSS describes how elements should be rendered on screen, on paper, in speech, or on other media. CSS is among the core languages of the open web and is standardized across Web browsers according to W3C specifications <sup>[[1](https://developer.mozilla.org/en-US/docs/Web/CSS)]</sup>.
- This are the types of CSS:
    ### 1. Inline CSS:
    - It involves applying styles directly to individual HTML elements using the style attribute. This method allows for specific styling of elements within the HTML document, overriding any external or internal styles.

    EXAMPLE:
    ```HTML
    <h1 style="font-style: bold">Hello</h1>
    ```
    ### 2. Internal(Embedded) CSS:
    - Its is defined within the HTML document’s style element inside the head section. It applies styles to specified HTML elements. 
    - The CSS rule set should be within the HTML file in the head section.

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
    ### 3. External CSS:
    - It contains separate CSS files that contain only style properties with the help of tag attributes. 
    - CSS property is written in a separate file with a .css extension and it is linked to the HTML document using a link tag inside the head section <sup>[[1](https://www.geeksforgeeks.org/types-of-css-cascading-style-sheet/)]</sup>.

    EXAMPLE:
    ```HTML
    <!-- This is index.html -->
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
    /* This is style.css */
    body {
      background-color: blue;
    }

    div {
      background-color: lightblue;
    }
    ```
## Q17. Explain different ways of creating animations in HTML. 
#### 1. CSS Transitions:
- Purpose:
    - To smoothly change an element's appearance over a specified duration when a CSS property changes. 

- Mechanism:
    - Define the properties to be animated (e.g., opacity, width, height, background-color) and the duration of the transition.
- Example:
    - `transition: background-color 1s ease;` will make the background color change smoothly over 1 second. 
- Use Cases: Hover effects, navigation transitions, smooth scrolls. 

2. CSS Animations:
- Purpose: 
    - To create more complex and customizable animations with keyframes. 

- Mechanism: 
    - Use the `@keyframes` rule to define the animation's different states at specific points in time.

- Example: `@keyframes myAnimation { from { opacity: 0; } to { opacity: 1; } }` defines an animation that fades an element in. 

- Use Cases: Rotating elements, sliding effects, creating custom animations. 

3. JavaScript Animations:
- Purpose:
    - To create dynamic and interactive animations by manipulating element styles in real-time. 

- Mechanism:
    - Use JavaScript to access and modify an element's CSS properties, often using requestAnimationFrame for smooth frame-by-frame updates. 
- Example:
    - `element.style.left = (parseInt(element.style.left) + 10) + 'px';` moves an element 10 pixels to the right in each frame. 
- Use Cases: Interactive animations, game development, and custom effects. 

4. `<canvas>` Element:

- Purpose: 
    - To draw animations using a bitmap image.
- Mechanism: 
    - Use JavaScript to access the canvas's drawing API (e.g., `beginPath()`, `fillRect()`, `drawImage()`) and redraw the scene in each frame.
- Example: 
    - `context.clearRect(0, 0, canvas.width, canvas.height);` clears the canvas, and `context.fillRect(x, y, width, height);` draws a rectangle.
- Use Cases:
    - Interactive drawing apps, simulations, and advanced graphics. 

## Q18. Write a HTML program to draw a line using SVG.

```html
<html>
<body>
	<svg height="200" width="200">
    	<line x1="0" y1="0" x2="160" y2="160" style="stroke:red;stroke-width:2" />
    </svg>
</body>
</html>
```
<iframe src="https://sounddrill31.github.io/html-demos/non-lab/line" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

## Q19. Explain the steps for drawing Bezier curves in canvas. 
To draw a Bezier curve on a canvas, you'll primarily use the `bezierCurveTo()` method in the `CanvasRenderingContext2D` object. 
- This method takes six arguments: 
    - two control points and the ending point of the curve. 
    - The starting point is implicitly taken from the last point defined in the path, so you'll need to use `beginPath()` and `moveTo()` to set the initial point before calling `bezierCurveTo()`. 
Steps:
- Get the canvas context: Obtain a reference to the canvas element and its 2D rendering context using `document.getElementById("canvasId").getContext("2d")`. 
- Start a new path: Initialize a new path using `context.beginPath()`. 
- Move to the starting point: Define the starting point of the curve using `context.moveTo(x, y)`. 
- Draw the Bezier curve: Use `context.bezierCurveTo(c1x, c1y, c2x, c2y, x, y)` to add the curve to the path. c1x, c1y and c2x, c2y are the coordinates of the control points, and x, y are the coordinates of the ending point. 
- Render the curve: Use `context.stroke()` to draw the path with a stroke or `context.fill()` to fill the path. 

```html
<html>
<body>
<canvas id="myCanvas" width="300" height="150"></canvas>

<script>
const c = document.getElementById("myCanvas");
const ctx = c.getContext("2d");
ctx.beginPath();
ctx.moveTo(20, 20);
ctx.bezierCurveTo(20, 100, 200, 100, 200, 20); // (controlpoint1x, controlpoint1y, controlpoint2x, controlpoint2y, endingx, endingy)
ctx.stroke();
</script> 

</body>
</html>
```

<iframe src="https://sounddrill31.github.io/html-demos/non-lab/bezier" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

[W3Schools](https://www.w3schools.com/jsref/canvas_beziercurveto.asp)

## Q20. Explain the styles and colors in HTML5 with an example

Below content will explore how to:
- Use the style attribute for styling HTML elements
- Use background-color for background color
- Use color for text colors
- Use font-family for text fonts
- Use font-size for text sizes
- Use text-align for text alignment


### Style Attribute
The HTML style attribute is used to add styles to an element, such as color, font, size, and more.
- Setting the style of an HTML element, can be done with the style attribute.
- The HTML style attribute has the following syntax:
    ```html
    <tagname style="property:value;">
    ```
- The property is a CSS property. 
    - The value is a CSS value.

### Background Color
The CSS background-color property defines the background color for an HTML element.
- Set the background color for a page to powderblue:
    ```html
    <body style="background-color:powderblue;">
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    </body>

### Text Color

The CSS color property defines the text color for an HTML element. Example: 
```html
<h1 style="color:blue;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
```

### Fonts

The CSS font-family property defines the font to be used for an HTML element. Example:
```html
<h1 style="font-family:verdana;">This is a heading</h1>
<p style="font-family:courier;">This is a paragraph.</p>
```
### Text Size
The CSS font-size property defines the text size for an HTML element. Example:

```html
<h1 style="font-size:300%;">This is a heading</h1>
<p style="font-size:160%;">This is a paragraph.</p>
```
### Text Alignment

The CSS text-align property defines the horizontal text alignment for an HTML element. Example:
```html
<h1 style="text-align:center;">Centered Heading</h1>
<p style="text-align:center;">Centered paragraph.</p>
```

[W3Schools](https://www.w3schools.com/html/html_styles.asp)
