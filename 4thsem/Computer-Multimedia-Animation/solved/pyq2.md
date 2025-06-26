---
order: 2
title: CMA Previous Paper 2024
---
# PYQs(2024)

> [!WARNING]
> This Page is incomplete and answers will be added soon. 3/20 Remaining.

# SECTION-A (6x2=12) 
## Q1. Write any two features of HTML5.
<!--@include: ../assignments/assignment-1.md{36,47} -->
## Q2. What are the advantages of Javascript?
- **Open source**: Many open-source projects provide useful help for developers to add JavaScript.
- **Programming language**: There are many available courses within the field of JavaScript, because of which you'll quickly and simply expand your knowledge of this programming language.
- **Easy to use**: It is not difficult to start working in JavaScript. For this reason, many of us prefer to start our adventure in the IT sector by learning this language. It gives the power to make rich interfaces.
- **Backend usage**: There are some ways to use JavaScript through Node.js servers. It is possible to develop a whole JavaScript app from front to back using only JavaScript.

[GeeksForGeeks](https://www.geeksforgeeks.org/javascript/advantages-and-disadvantages-of-javascript/)
## Q3. Define interpolation.
Interpolation is a method for estimating new data points based on a set of known data points.
- Interpolation calculates intermediate values in animations that change HTML properties such as height, width, etc. 
- Color interpolation defines intermediate values of colors in color mixing, gradients, compositing, filters, transitions, animations, and color functions.

[Mozilla Developer Docs](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)

<InterpolationExample />

## Q4. What is SVG transition?
TODO 
## Q5. What are filters in SVG?
<!--@include: ./pyq.md{47,51}-->
## Q6. What is radial gradient?
The `radial-gradient()` CSS function creates an image consisting of a progressive transition between two or more colors that radiate from an origin. Its shape may be a circle or an ellipse. The function's result is an object of the `<gradient>` data type, which is a special kind of `<image>`. 

[Mdn Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/radial-gradient)

## Q7. Mention the LineCap attributes.
The LineCap attributes are:
- **butt**: Stroke does not extend beyond endpoints. Zero-length subpath is not rendered. (Default)
- **round**: Stroke ends with a half circle (diameter = stroke width). Zero-length subpath has a full circle at its point.
- **square**: Stroke ends with a rectangle (width = half stroke width, height = stroke width). Zero-length subpath has a centered square (width = stroke width).

[Mdn Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/stroke-linecap)

## Q8. Write the use of Bezier curve.
The `bezierCurveTo()` method adds a curve to the path by using the control points that represent a cubic Bézier curve.
Use the `stroke()` or `fill()` method to draw the path.
A cubic bezier curve requires three points. The first two points are control points that are used in the cubic Bézier calculation and the last point is the ending point for the curve.  The starting point for the curve is the last point in the current path. If a path does not exist, use the `beginPath()` and `moveTo()` methods to define a starting point.

[W3Schools](https://www.w3schools.com/jsref/canvas_beziercurveto.asp)

## Q9. What is canvas-scaling?
The HTML canvas scale() Method is used to scale the current drawing into smaller or larger size. After scaling the drawing, all the feature of drawing scaled. It will have to define before the canvas. 
Syntax:
```html
context.scale( scalewidth, scaleheight )
```
# SECTION-B (4x6=24)
## Q10. Explain any three HTML tags with examples.
| Tag | Description | Example | Common Attributes |
|---|---|---|---|
| **`<a>`** | Defines a hyperlink, used to link from one page to another or to a location on the same page. It's the foundation of navigation on the web. | `<a href="https://www.example.com" target="_blank">Visit Example</a>` | `href` (URL of the link), `target` (_blank, _self), `rel` (relationship to the linked document), `download` |
| **`<img>`** | Embeds an image into an HTML document. This is a self-closing tag, meaning it doesn't need a separate closing tag like `</img>`. | `<img src="images/logo.png" alt="Company Logo" width="100" height="50">` | `src` (source URL of the image), `alt` (alternative text for accessibility), `width`, `height`, `loading` (lazy, eager) |
| **`<div>`** | Defines a division or a section in a document. It is a generic block-level container used to group other elements for styling with CSS or manipulation with JavaScript. | `<div class="user-profile"><p>User Name</p></div>` | `id` (a unique identifier), `class` (one or more class names for styling), `style` (inline CSS) |
| **`<p>`** | Defines a paragraph of text. Browsers automatically add some space (a margin) before and after each `<p>` element to separate them visually. | `<p>This is the first paragraph. It contains some text.</p>` | Global attributes like `id`, `class`, and `style` are the most commonly used. It has no tag-specific attributes. |


## Q11. Explain the features of Javascript.
- **Dynamic Typing**: JavaScript does not require you to declare the data type of a variable when you create it. The type is determined at runtime. 
- **Interpreted Language**: JavaScript code is executed directly by the browser or other environments without needing a separate compilation step. 
- **Object-Oriented**: JavaScript supports object-oriented programming principles, including the use of objects, prototypes, and classes. 
- **Functional Programming**: JavaScript treats functions as first-class citizens, meaning they can be passed as arguments to other functions, returned from functions, and assigned to variables. 

[ScholarHat](https://www.scholarhat.com/tutorial/javascript/features-of-javascript#:~:text=JavaScript%20is%20a%20lightweight%20language,Prototype%2DBased)
## Q12. Write the differences between longhand and shorthand properties.
<!--@include: ./pyq.md{120,144} -->
## Q13. Write a short note on SVG-Polygon.
Polygon comes from Greek. "Poly" means "many" and "gon" means "angle".
The `<polygon>` element is used to create a graphic that contains at least three sides.
Polygons are made of straight lines, and the shape is "closed" (it automatically connects the last point with the first).
The `<polygon>` element has one basic attribute that defines the points of the polygon:
- ***`points`*** - The list of points of the polygon. Each point must contain an x coordinate and a y coordinate.

[W3Schools](https://www.w3schools.com/graphics/svg_polygon.asp)

## Q14. Explain the canvas-drawing rectangles with example.
The three most used methods for drawing rectangles in canvas are:
1. ***`rect()` Method***: The `rect()` method is used to define a rectangle by specifying its upper-left corner coordinates, width, and height. However, it does not draw the rectangle until the `stroke()` or `fill()` method is called. For example:
   ```javascript
   ctx.rect(10, 10, 150, 100);
   ctx.stroke(); // This draws the defined rectangle
   ```

2. ***`fillRect()` Method***: The `fillRect()` method draws a filled rectangle directly on the canvas. It requires the same parameters as `rect()`, and the fill color can be set using the `fillStyle` property. For example:
   ```javascript
   ctx.fillStyle = "pink"; // Set fill color
   ctx.fillRect(10, 10, 150, 100); // Draw filled rectangle
   ```

3. ***`strokeRect()` Method***: The `strokeRect()` method draws an outlined rectangle. Similar to `fillRect()`, it takes the same parameters, and the stroke color can be set using the `strokeStyle` property. For example:
   ```javascript
   ctx.strokeRect(10, 10, 150, 100); // Draw stroked rectangle
   ```

[W3Schools](https://www.w3schools.com/graphics/canvas_rectangles.asp)

## Q15. Explain the following:
1. Canvas rotation
2. Canvas translation.

- ***Canvas Rotation***:
Canvas rotation refers to the transformation that allows you to rotate the drawing surface (canvas) around a specified point, typically the origin (0, 0) or the center of the canvas. This transformation affects all subsequent drawing operations, allowing you to create rotated shapes, images, or text. The rotation is usually specified in degrees or radians, and it can be applied using transformation functions provided by graphics libraries.
- ***Canvas Translation***
Canvas translation is the process of moving the drawing surface (canvas) along the x and y axes. This transformation shifts the origin of the canvas to a new position, allowing you to draw objects at different locations without changing their coordinates. Translation is often used to position elements on the canvas or to create animations by moving objects smoothly across the screen.

[W3Schools](https://www.w3schools.com/graphics/canvas_rectangles.asp)

# SECTION - C (3x8=24)
## Q16. Explain any two types of selectors in CSS with examples.
| Selector Type | CSS Syntax (in .css file) | HTML Markup (in .html file) | Description & Considerations |
|---|---|---|---|
| **Element Selector** | `p { color: #333; }` | `<p>This is a paragraph.</p>` | Selects all HTML elements by their tag name. It's a broad selector that applies a style globally to a specific type of element. |
| **Class Selector** | `.highlight { background: yellow; }` | `<p class="highlight">Important</p>` | Selects all elements that have a specific `class` attribute. Begins with a period (`.`). This is the most common and versatile selector, as a class can be reused on many elements. |
| **ID Selector** | `#main-header { font-size: 32px; }` | `<header id="main-header">...</header>` | Selects one unique element with a specific `id` attribute. Begins with a hash (`#`). An ID must be unique per page, making it ideal for targeting a single, specific element. |
| **Attribute Selector** | `a[target="_blank"] { opacity: 0.8; }` | `<a href="..." target="_blank">Link</a>` | Selects elements based on the presence or value of an attribute. Uses square brackets `[]`. Useful for styling elements with specific attributes without adding extra classes. |
| **Pseudo-class Selector** | `button:hover { background: #555; }` | `<button>Hover over me</button>` | Selects elements based on a specific state or condition, such as being hovered over or being the first child. Begins with a colon (`:`). Essential for creating interactive and dynamic user interfaces. |
| **Universal Selector**| `* { margin: 0; }` | (Applies to all elements) | Selects every single HTML element on the page. Represented by an asterisk (`*`). Often used in CSS resets to establish a consistent baseline for styles across different browsers. |
| **Descendant Selector**| `article p { line-height: 1.6; }` | `<article><p>Text...</p></article>` | Selects an element that is a descendant of another specific element. A space between two selectors indicates this relationship. In the example, it only styles `<p>` tags that are inside an `<article>` tag. |
| **Grouping Selector**| `h1, h2, h3 { font-family: 'Georgia'; }` | `<h1>Title</h1><h2>Subtitle</h2>` | Applies the same styles to multiple selectors at once. Selectors are separated by a comma (`,`). This avoids repeating the same style block for different elements. |


[W3Schools](https://www.w3schools.com/css/css_selectors.asp)
## Q17. Write a HTML program to display random contents using list properties:
1. Ordered list
2. Unordered list.

::: details Program

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML List Examples</title>
</head>
<body>

    <h1>HTML List Examples</h1>

    <!-- 
        Unordered Lists (<ul>) are used for items without a specific sequence.
        The list item marker style can be changed.
    -->
    <h2>Unordered Lists</h2>

    <p>Default Unordered List (disc):</p>
    <ul>
        <li>Coffee</li>
        <li>Tea</li>
    </ul>

    <p>Unordered List with Circles:</p>
    <!-- The list-style-type property is used to define the marker style  -->
    <ul style="list-style-type:circle;">
        <li>Red</li>
        <li>Green</li>
    </ul>

    <p>Unordered List with Squares:</p>
    <ul style="list-style-type:square;">
        <li>Apple</li>
        <li>Banana</li>
    </ul>

    <p>Unordered List with No Markers:</p>
    <ul style="list-style-type:none;">
        <li>First</li>
        <li>Second</li>
    </ul>

    <!-- 
        An ordered list (<ol>) is used when the order of items is important.
        By default, items are marked with numbers .
    -->
    <h2>Ordered List</h2>
    <ol>
        <li>Gather ingredients</li>
        <li>Mix ingredients</li>
        <li>Bake in oven</li>
    </ol>

</body>
</html>
```
:::

::: details Show Output

    <h1>HTML List Examples</h1>

    <h2>Unordered Lists</h2>

    <p>Default Unordered List (disc):</p>
    <ul>
        <li>Coffee</li>
        <li>Tea</li>
    </ul>

    <p>Unordered List with Circles:</p>
    <ul style="list-style-type:circle;">
        <li>Red</li>
        <li>Green</li>
    </ul>

    <p>Unordered List with Squares:</p>
    <ul style="list-style-type:square;">
        <li>Apple</li>
        <li>Banana</li>
    </ul>

    <p>Unordered List with No Markers:</p>
    <ul style="list-style-type:none;">
        <li>First</li>
        <li>Second</li>
    </ul>

    <h2>Ordered List</h2>
    <ol>
        <li>Gather ingredients</li>
        <li>Mix ingredients</li>
        <li>Bake in oven</li>
    </ol>

:::

## Q18. Explain SVG Properties with attributes.
In Scalable Vector Graphics (SVG), attributes are used to modify elements, defining details about how they should be handled and rendered. 
- These attributes control everything from an element's position and size to its color and interactivity. Many of these attributes, known as "presentation attributes," can be used interchangeably with CSS properties to style SVG elements.
- SVG attributes can be grouped into several categories, including core, styling, and geometry attributes.

| Core Attributes | --- | Core attributes are common to all SVG elements and manage fundamental properties like identification and language. |
| Attribute | Description | Applicable Elements |
| --- | --- | --- |
| `id` | Provides a unique identifier for an element, used for linking, scripting, or styling with CSS. | All SVG elements. |
| `class` | Assigns one or more class names to an element, allowing it to be targeted by CSS for styling. | All SVG elements. |
| `style` | Specifies inline CSS styles directly on an element. | All SVG elements. |
| `lang` / `xml:lang` | Defines the natural language of the element's content. `xml:lang` takes precedence if both are present. | All SVG elements. |
| `tabindex` | Controls whether an element is focusable and defines its order in sequential keyboard navigation. | All SVG elements. |
| Styling (Presentation) Attributes | --- | These attributes define the visual appearance of SVG elements, such as color, stroke, and opacity. |
| Attribute | Description | Example Elements |
| --- | --- | --- |
| `fill` | Sets the color inside a shape or the color of text. | ``, ``, ``, `` |
| `stroke` | Defines the color of an element's outline or stroke. | ``, ``, ``, `` |
| `stroke-width` | Sets the thickness of the stroke. | ``, ``, ``, `` |
| `stroke-dasharray` | Creates dashed or dotted outlines by specifying the length of dashes and gaps. | ``, ``, ``, `` |
| `stroke-linecap` | Defines the shape of the ends of open paths (e.g., `butt`, `round`, `square`). | ``, ``, `` |
| `opacity` | Specifies the overall transparency of an element, from 0.0 (fully transparent) to 1.0 (fully opaque). | Graphics and container elements like ``, `` |
| `transform` | Applies geometric transformations like `translate`, `rotate`, `scale`, and `skew` to an element. | Graphics and container elements (``) |
| `font-family`, `font-size` | Specifies the font family and size for text content. | Text content elements like `` and `` |
| `text-anchor` | Aligns text horizontally (e.g., `start`, `middle`, `end`) relative to its `x` coordinate. | Text content elements |
| `visibility` | Controls whether an element is rendered. Can be set to `visible` or `hidden`. | Graphics and text content elements |
| Geometry Attributes | --- | Geometry attributes define the position, size, and shape of an SVG element. With the introduction of SVG 2, many of these can also be styled and animated using CSS. |
| Attribute | Description | Specific Elements |
| :--- | :--- | :--- |
| `x`, `y` | Define the x and y coordinates of an element's top-left corner. | ``, ``, ``, `` |
| `width`, `height` | Specify the width and height of an element. | ``, ``, `` |
| `cx`, `cy` | Define the x and y coordinates of the center point. | ``, `` |
| `r` | Specifies the radius of a circle. | `` |
| `rx`, `ry` | Specify the horizontal and vertical radii for an ellipse or the corner radii for a rectangle. | ``, `` |
| `d` | Defines the shape of a path using a specific command syntax for lines, curves, and arcs. | `` |
| `points` | A list of x and y coordinates that define the vertices of a shape. | ``, `` |

## Q19. Explain the canvas-linear gradients with example.
Gradients let you display smooth transitions between two or more specified colors.
Gradients can be used to fill rectangles, circles, lines, text, etc.
The `createLinearGradient()` method is used to define a linear gradient.
A linear gradient changes color along a linear pattern (horizontally/vertically/diagonally).
The `createLinearGradient()` method has the following parameters:
- `x0` -> The x-coordinate of the start point
- `y0` -> The y-coordinate of the start point
- `x1` -> The x-coordinate of the end point
- `y1` -> The y-coordinate of the end point

The gradient object requires two or more color stops.
The addColorStop() method specifies the color stops, and its position along the gradient. The positions can be anywhere between 0 and 1.
To use the gradient, assign it to the fillStyle or strokeStyle property, then draw the shape (rectangle, circle, shape, or text).

EXAMPLE:
```javascript
 <script>
const c = document.getElementById("myCanvas");
const ctx = c.getContext("2d");

// Create linear gradient
const grad=ctx.createLinearGradient(0,0, 280,0);
grad.addColorStop(0, "lightblue");
grad.addColorStop(1, "darkblue");

// Fill rectangle with gradient
ctx.fillStyle = grad;
ctx.fillRect(10,10, 280,130);
</script> 
```

[W3Schools](https://www.w3schools.com/graphics/canvas_gradients.asp)

## Q20. Explain the canvas text and fonts with example.
HTML5 canvas provides capabilities to create text using different font and text properties listed below −
1. ***`font [ = value ]`***:  
This property returns the current font settings and can be set, to change the font.
2. ***`textAlign [ = value ]`***:  
This property returns the current text alignment settings and can be set, to change the alignment. The possible values are start, end, left, right, and center.
3. ***`textBaseline [ = value ]`***: 
This property returns the current baseline alignment settings and can be set, to change the baseline alignment. The possible values are top, hanging, middle , alphabetic, ideographic and bottom.
4. ***`fillText(text, x, y [, maxWidth ] )`***:
This property fills the given text at the given position indicated by the given coordinates x and y.
5. ***`strokeText(text, x, y [, maxWidth ] )`***:
This property strokes the given text at the given position indicated by the given coordinates x and y.

EXAMPLE:
```html
<!DOCTYPE HTML>
<html>
   <head>
      <style>
         #test {
            width: 100px;
            height:100px;
            margin: 0px auto;
         }
      </style>
      <script type = "text/javascript">
         function drawShape() {
         
            // get the canvas element using the DOM
            var canvas = document.getElementById('mycanvas');
            
            // Make sure we don't execute when canvas isn't supported
            if (canvas.getContext) {
            
               // use getContext to use the canvas for drawing
               var ctx = canvas.getContext('2d');
               
               ctx.fillStyle = '#00F';
               ctx.font = 'Italic 30px Sans-Serif';
               
               ctx.textBaseline = 'Top';
               ctx.fillText('Hello world!', 40, 100);
               
               ctx.font = 'Bold 30px Sans-Serif';
               ctx.strokeText('Hello world!', 40, 50);
            } else {
               alert('You need Safari or Firefox 1.5+ to see this demo.');
            }
         }
      </script>
   </head>
   <body id = "test" onload = "drawShape();">
      <canvas id = "mycanvas"></canvas>
   </body>
</html>
```