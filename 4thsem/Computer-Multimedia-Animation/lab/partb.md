---
order: 2
title: CMA Lab - Part B
---
# Computer Multimedia and Animation - Lab Part B

## Q1. Write a HTML5 program to draw shapes using SVG like rectangle, line, polygon, polyline

::: details See code
```html
<!DOCTYPE html>
<html>
<head>
    <title>SVG Shapes!</title>
</head>

<body>
    <svg width="400" height="400">
        <rect x="50" y="50" width="100" height="50" fill="blue"/>
        <line x1="50" y1="150" x2="150" y2="150" stroke="red" stroke-width="2"/>
        <polygon points="200,50 250, 100 200, 150 150, 100" fill="green"/>
        <polyline points="250,150 300,200 350,150 300,100" stroke="purple" stroke-width="3" fill="none"/>
    </svg>
</body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg1)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg1/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="350px" allowfullscreen></iframe>

:::

## Q2. Write a HTML5 program to draw linear and radial gradient ellipse using SVG

::: details See code
```html
<!DOCTYPE html>
<html>
<head>
    <title>SVG Gradient Ellipse Example</title>
</head>
<body>
    <svg width="400" height="400">
        <defs>
            <linearGradient id="linearGradient">
                <stop offset="0%" stop-color="red"/>
                <stop offset="50%" stop-color="orange"/>
                <stop offset="0%" stop-color="yellow"/>
            </linearGradient>
            <radialGradient id="radialGradient" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="blue"/>
                <stop offset="50%" stop-color="purple"/>
                <stop offset="0%" stop-color="pink"/>
            </radialGradient>
            </defs>
            <ellipse cx="200" cy="100" rx="100" ry="50" fill="url(#linearGradient)"/>
            <ellipse cx="200" cy="300" rx="100" ry="50" fill="url(#radialGradient)"/>
    </svg>
</body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg2)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg2/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="400px" allowfullscreen></iframe>

:::


## Q3. Write a HTML5 program to draw a star using SVG

::: details See code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Drawing a Star using SVG</title>
    <style>
        svg {
            border: 1px solid block;
        }
    </style>
</head>
<body>
    <svg width="200" height="200">
        <polygon points="100, 10 40, 198 190, 78 10, 78 160, 198"
            style="fill: yellow; stroke: black; stroke-width: 2px;"/>
    </svg>
</body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg3)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg3/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::
## Q4. Write a HTML5 program to drawline, circle, rectangle, gradient, text using SVG

::: details See code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Canvas Drawing</title>
</head>
<body>
    <canvas id="myCanvas" width="600" height="600"/>
    <script>
        var canvas = document.getElementById('myCanvas');
        var ctx = canvas.getContext('2d');

        //Draw line
        ctx.beginPath();
        ctx.moveTo(50, 50);
        ctx.lineTo(550, 50);
        ctx.strokeStyle = 'black';
        ctx.stroke();

        // Draw circle
        ctx.beginPath();
        ctx.arc(100, 150, 50, 0, Math.PI * 2, false);
        ctx.fillStyle='red';
        ctx.fill();
        ctx.strokeStyle = 'blue';
        ctx.stroke();

        // Draw Rectangle
        ctx.beginPath();
        ctx.rect(200, 130, 150, 75);
        ctx.fillStyle = 'green';
        ctx.fill();
        ctx.strokeStyle = 'orange';
        ctx.stroke();

        //Draw gradient
        var gradient = ctx.createLinearGradient(400, 130, 600, 130);
        gradient.addColorStop(0, 'yellow');
        gradient.addColorStop(1, 'purple');
        ctx.fillStyle = gradient;
        ctx.fillRect(400,130,150,75);

        // Draw text
        ctx.font = '20px Arial';
        ctx.fillStyle = 'black';
        ctx.fillText('Hello Canvas!', 250, 300);
    </script>
</body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg4)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg4/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="600px" width="600px" allowfullscreen></iframe>

:::
