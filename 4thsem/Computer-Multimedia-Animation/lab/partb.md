---
order: 2
title: CMA Lab - Part B
---
# Computer Multimedia and Animation - Lab Part B

## Q1. Write an HTML/5 program to draw shapes using SVG like rectangle, line, polygon, polyline

::: details See code {open}
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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg1)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg1/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="350px" allowfullscreen></iframe>

:::

## Q2. Write an HTML/5 program to draw linear and radial gradient ellipse using SVG

::: details See code {open}
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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg2)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg2/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="400px" allowfullscreen></iframe>

:::


## Q3. Write an HTML/5 program to draw a star using SVG

::: details See code {open}
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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg3)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg3/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::
## Q4. Write an HTML/5 program to drawline, circle, rectangle, gradient, text using SVG

::: details See code {open}
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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg4)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg4/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="600px" width="600px" allowfullscreen></iframe>

:::
## Q5. Write an HTML/5 program to demonstrate translation, rotation, scaling, and transform using Canvas

::: details See code {open}
```html
<!DOCTYPE html>
<html>
  <head>
	<title>Canvas Transformation</title>
	<style>
	 canvas {
		border: 1px solid black;
	 }
	</style>
  </head>
  <body>
     <canvas id="myCanvas" width="400" height="400"></canvas>
     <script>
    
       const canvas= document.getElementById("myCanvas");
 
       const ctx = canvas.getContext("2d");

	ctx.fillStyle="red";
	ctx.fillRect(50,50,100,100);

	ctx.translate(200,100);
	ctx.rotate(Math.PI/4)
	ctx.scale(2,2);

	ctx.fillStyle="blue";
	ctx.fillRect(-50,-50,100,100);

	ctx.setTransform(1,0,0,1,0,0);

	ctx.fillStyle="green";
	ctx.fillRect(200,200,100,100);

	ctx.setTransform(1,0.5,-0.5,1,0,0);

	ctx.fillStyle="orange";
	ctx.fillRect(200,200,100,100);
	</script>
  </body>
</html>
```
:::

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg5)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg5/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="600px" width="600px" allowfullscreen></iframe>

:::
## Q6. Write an HTML/5 program to demonstrate Bezier Curves and Quadratic Equations

::: details See code {open}
```html
<html>
  <head>
     <title>Bezier and Quadratic Curves Example</title>
     <style>
	 canvas{
	     border: 1px solid black;
	    }
     </style>
  </head>
  <body>
     <canvas id="mycanvas" width="400" height="400"></canvas>
     <script>
    
	const canvas= document.getElementById("mycanvas");
 
	const ctx = canvas.getContext("2d");

	ctx.beginPath();
	ctx.moveTo(50,50);
		ctx.quadraticCurveTo(100,25,150,50);
	ctx.stroke();

	ctx.beginPath();
	ctx.moveTo(200,50);

	ctx.bezierCurveTo(200,25,250,25,250,50);
	ctx.stroke();

	ctx.beginPath();
	ctx.quadraticCurveTo(75,125,100,150);
	ctx.quadraticCurveTo(125,175,150,150);
	ctx.stroke();

	ctx.beginPath();
	ctx.moveTo(200,150);
	ctx.bezierCurveTo(200,125,250,125,250,150);
	ctx.bezierCurveTo(250,175,200,175,200,150);
	ctx.stroke();
    </script>
  </body>
</html>
```
:::

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg6)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg6/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="600px" width="600px" allowfullscreen></iframe>

:::

## Q7. Write a HTML/S program to create canvas and add a red square onto the game area with up/down/left/right controller buttons

> [!NOTE]
> This example NEEDS you to use your keyboard. Press up/down/left/right buttons to move the box. There's no touch equivalent for these actions.

::: details See code {open}
```html
<!DOCTYPE html>
<html>
<head>
    <title>Canvas Game</title>
    <style>
        canvas {
            border: 1px solid #000;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="400"></canvas>
    <script>
        // Get the canvas element
        var canvas = document.getElementById("gameCanvas");
        var context = canvas.getContext("2d");

        // Set initial position of the square
        var squareX = 200;
        var squareY = 200;
        var squareSize = 50;

        // Function to draw the square
        function drawSquare() {
            context.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
            context.fillStyle = "red";
            context.fillRect(squareX, squareY, squareSize, squareSize);
        }

        // Function to handle keyboard input
        function handleKeyDown(event) {
            var keyCode = event.keyCode;
            switch (keyCode) {
                case 37: // Left arrow key
                    squareX -= 10;
                    break;
                case 38: // Up arrow key
                    squareY -= 10;
                    break;
                case 39: // Right arrow key
                    squareX += 10;
                    break;
                case 40: // Down arrow key
                    squareY += 10;
                    break;
            }
            drawSquare();
        }

        // Add event listener for keydown events
        document.addEventListener("keydown", handleKeyDown);

        // Call drawSquare initially to draw the square
        drawSquare();

    </script>
</body>
</html>
```
:::

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg7)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg7/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="600px" width="600px" allowfullscreen></iframe>

:::


## Q8. Write an HTML/5 program to add random size obstacles with a red square controller box

::: details See code {open}
```html
<!DOCTYPE html>
<html>
<head>
    <title>Random Obstacles</title>
    <style>
        #controller {
            background-color: red;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <canvas id="myCanvas" width="200" height="200" style="border:1px solid #000;"></canvas>
    <button id="controller" onclick="addObstacle()">Add Obstacle</button>

<script> 
const canvas = document.getElementById('myCanvas'); 
const ctx = canvas.getContext('2d'); 

function getRandomInt(min, max) { 
    return Math.floor(Math.random() * (max - min + 1)) + min; 
}

function addObstacle() { 
    // Determine random size for the obstacle 
    const obstacleSize = getRandomInt(18, 50); 
    // Determine random position for the obstacle ensuring it fits within the canvas 
    const x = getRandomInt(0, canvas.width - obstacleSize); 
    const y = getRandomInt(0, canvas.height - obstacleSize); 
    // Draw the obstacle 
    ctx.fillStyle = 'grey'; 
    ctx.fillRect(x, y, obstacleSize, obstacleSize); 
} 
</script> 
</body> 
</html>
```
:::

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/partb/prg8)

<iframe src="https://sounddrill31.github.io/html-demos/partb/prg8/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="600px" width="600px" allowfullscreen></iframe>

:::
