---
order: 1
title: CMA Lab - Part A
---
# Computer Multimedia and Animation - Lab Part A

## Q1. Write an HTML/5 program to demonstrate the use of Font family, font variant, font style, and font size. *


::: details See code
```html
<!DOCTYPE html>
<html lang="en">

<head> 
    <meta charset="UTF-8">
    <meta mame="viewport" content="width=device-width",initial-scale=1.0>
    <title>Font Example</title>

    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }
        .bold {
            font-weight: bold;
        }
        .italic {
            font-style: italic;
        }
        .small-caps {
            font-variant: small-caps;
        }
    </style>
</head> 

<body>
    <p>This is a normal Paragraph</p>
    <p class="bold"> Bold Paragraph </p>
    <p class="italic"> Italics Paragraph </p>
    <p class="small-caps"> Small Caps Paragraph </p>
</body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/prg1)

<iframe src="https://sounddrill31.github.io/html-demos/prg1/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

::: details Shortened Code
```html
<!DOCTYPE html>

<html>
<head>
<title>Font Example</title>
</head>

<body style="font-family:monospace;">
<p>Normal Paragraph</p>
<p style="font-weight:bold;">Bold Paragraph</p>
<p style="font-style:italic;">Italic Paragraph</p>
<p style="font-variant:small-caps;">Small Caps Paragraph</p>
</body>
</html>
```

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/short-a/prg1)

<iframe src="https://sounddrill31.github.io/html-demos/short-a/prg1" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

## Q2. Write an HTML/5 program to display random contents using list properties: *
1. ordered list 
2. Unordered list 

::: details See code
```html
<!DOCTYPE html>
<html lang="en">

<head> 
    <meta charset="UTF-8">
    <meta mame="viewport" content="width=device-width",initial-scale=1.0>
    <title>List Demonstration</title>
</head> 

<body>
    <h2>Ordered List, Different Types</h2>
    
    <br>

    <h3>Sort by Numbers</h3>
    <ol type="1">
        <li>Mango</li>
        <li>Guava</li>
        <li>Orange</li>
        <li>Apple</li>
    </ol>

    <br>

    <h3>Sort by Capital Letters</h3>
    <ol type="A">
        <li>Mango</li>
        <li>Guava</li>
        <li>Orange</li>
        <li>Apple</li>
    </ol>

    <br>

    <h3>Sort by Lowercase Roman letters, except it starts from 4</h3>
    <ol type="i" start="4">
        <li>Mango</li>
        <li>Guava</li>
        <li>Orange</li>
        <li>Apple</li>
    </ol>

    <br>

    <h3>Sort by Numbers, Reversed</h3>
    <ol reversed>
        <li>Mango</li>
        <li>Guava</li>
        <li>Orange</li>
        <li>Apple</li>
    </ol>

    <br>

    <h2>Unordered List, Different Types</h2>

    <br>

    <h3>Show Discs</h3>
    <ul type="disc">
        <li>Mango</li>
        <li>Guava</li>
        <li>Orange</li>
        <li>Apple</li>
    </ul>

    <br>

    <h3>Show Circles</h3>
    <ul type="circle">
        <li>Mango</li>
        <li>Guava</li>
        <li>Orange</li>
        <li>Apple</li>
    </ul>

    <br>

    <h3>Show Squares</h3>
    <ul type="square">
        <li>Mango</li>
        <li>Guava</li>
        <li>Orange</li>
        <li>Apple</li>
    </ul>


</body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/prg2)

<iframe src="https://sounddrill31.github.io/html-demos/prg2/" style="border:0px #ffffff none;" name="myiFrame" scrolling="yes" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::


::: details Shortened Code

```html
<!DOCTYPE html>

<html>
<head>
<title>Lists</title>
</head>
<body>

<h2>Ordered</h2>
<h3>Numbers</h3>
<ol>
	<li>Mango</li>
    <li>Guava</li>
</ol>
<h3>Roman</h3>
<ol type="i">
	<li>Mango</li>
    <li>Guava</li>	
</ol>
<h2>Unordered</h2>
<h3>Circles</h3>
<ul type="circle">
	<li>Mango</li>
    <li>Guava</li>
</ul>
<h3>Discs</h3>
<ul type="disc">
	<li>Mango</li>
    <li>Guava</li>
</ul>

</body>
</html>
```

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/short-a/prg2)

<iframe src="https://sounddrill31.github.io/html-demos/short-a/prg2" style="border:0px #ffffff none;" name="myiFrame" scrolling="yes" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>
:::

## Q3. Write an HTML/5 program to create gradient using css. *

::: details See Code
```html
<!DOCTYPE HTML>
<HTML>
    <HEAD>
            <title>Gradient Example</title>
            <style>
                body {
                    /*background-color: red;*/
                    background: linear-gradient(to bottom, #ffcccc, #ff99cc) no-repeat;
                    min-height:100vh;
                }
                .gradient-box {
                    background: radial-gradient(circle, #ccffcc, #ccff99);
                    border-radius: 10px;
                }
            </style>
        </HEAD>
        <body>
            <div class="gradient-box">
            <h1>Good Morning</h1>
            <p>This is an example with both a linear and radial gradient.</p>
            </div>
    </body>
    </HTML>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/prg3)

<iframe src="https://sounddrill31.github.io/html-demos/prg3/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

## Q4. Write an HTML/5 code to demonstrate following CSS animation properties: * 
1. Delay 
2. Direction 
3. Duration


::: details See Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Animation Properties Example</title>
    <style>
        .box {
            width: 100px;
            height: 100px;
            background-color: red;
            animation-name: move;
            animation-duration: 2s;
            animation-direction: alternate;
            animation-delay: 1s;
            animation-iteration-count: infinite;
        }

        @keyframes move {
            from {
                transform: translateX(0px);
            }
            to {
                transform: translateX(200px);
            }
        }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/prg4)

<iframe src="https://sounddrill31.github.io/html-demos/prg4/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

::: details Shortened Code
```html
<!DOCTYPE html>

<html>
<head>
<title>CSS Gradients</title>
<style>
	.box {
   		width:100px;height:100px;
        background:red;
        animation: move 1s alternate 1s infinite;
    }
    @keyframes move {
    	from {
        	transform: translateX(0px);
        }
        to {
        	transform: translateX(200px);
        }
    }
</style>
</head>
<body>
<div class="box"></div>

</body>
</html>
```

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/short-a/prg4)

<iframe src="https://sounddrill31.github.io/html-demos/short-a/prg4" style="border:0px #ffffff none;" name="myiFrame" scrolling="yes" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

## Q5. Write an HTML/5 program to demonstrate key frames *

[View Webpage](https://sounddrill31.github.io/html-demos/prg5/)

::: details See Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Keyframes Animation Example</title>
    <style>
        .box {
            width: 100px;
            height: 100px;
            margin: 50px;  /*Personally added by Jp, to ensure that the box is fully visible*/
            background-color: red;
            position: relative;
            animation: move 2s infinite;
        }

        @keyframes move {
            0% {
                left: 0px;
            }
            50% {
                left: 200px;
                transform: rotate(45deg);
            }
            100% {
                left: 0px;
            }
        }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>

```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/prg5)

<iframe src="https://sounddrill31.github.io/html-demos/prg5/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

([Prg 4](./parta.md#q4-write-an-html5-code-to-demonstrate-following-css-animation-properties-) is also an appropriate example)

## Q6. Write an HTML/5 code to demonstrate CSS transition and transformation. *

::: details See code
```html
<!DOCTYPE html>
<html>
 <head>
  <title>CSS Transition and Transformation Example</title>
  <style>
    .box{
     width:100px;
     height:100px;
     background-color: red;
     position: relative;
     transition: transform 4s;
    }
    .box:hover {
     transform: rotate(45deg);
    }
  </style>
 </head>
 <body>
  <div class="box"></div>
 </body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/prg6)

<iframe src="https://sounddrill31.github.io/html-demos/prg6/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::


## Q7. Write an HTML/5 program to turn on/off a light bulb using JavaScript. 
Make use of image and buttons. 

> [!WARNING]
> This program requires you to use an external image for bulb off and bulb on states.
> I used [light_off](https://fonts.google.com/icons?selected=Material+Symbols+Outlined:light_off:FILL@0;wght@400;GRAD@0;opsz@40&icon.query=bulb&icon.size=42&icon.color=%231f1f1f) and [light_2](https://fonts.google.com/icons?selected=Material+Symbols+Outlined:lightbulb_2:FILL@0;wght@400;GRAD@0;opsz@40&icon.query=bulb&icon.size=42&icon.color=%231f1f1f) from google fonts for this.

> [!NOTE]
> Remember to download [light_off](https://fonts.google.com/icons?selected=Material+Symbols+Outlined:light_off:FILL@0;wght@400;GRAD@0;opsz@40&icon.query=bulb&icon.size=42&icon.color=%231f1f1f) as png using the given button and rename it to bulb_off.png. It will not work without this!

> [!NOTE]
> Remember to download [light_2](https://fonts.google.com/icons?selected=Material+Symbols+Outlined:lightbulb_2:FILL@0;wght@400;GRAD@0;opsz@40&icon.query=bulb&icon.size=42&icon.color=%231f1f1f) as png using the given button and rename it to bulb_on.png. It will not work without this!

::: details See code
```html
<!DOCTYPE HTML>
<html>
<head>
	<title> </title>
	<script>
		function toggleLight() {
			var bulb = document.getElementById("lightbulb");
			if (bulb.src.match("bulb_on.png"))
			{
				bulb.src = "bulb_off.png";
				bulb.style.background="";
				
			}
			else
			{
				bulb.src = "bulb_on.png";
				bulb.style.background="radial-gradient(circle, rgba(240,251,63,1) 0%, rgba(252,70,107,0) 58%)";
			}
		}
	</script>
	<style>
		
	</style>
</head>
<body>
	<div>
		<img id="lightbulb" src=bulb_off.png alt="Light Bulb"/>
	</div>
	<div>
		<button onclick="toggleLight()">Toggle Light</button>
	</div>
</body>
</html>
```
:::

::: details Show output {open}

[View Webpage](https://sounddrill31.github.io/html-demos/prg7)

<iframe src="https://sounddrill31.github.io/html-demos/prg7/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::
