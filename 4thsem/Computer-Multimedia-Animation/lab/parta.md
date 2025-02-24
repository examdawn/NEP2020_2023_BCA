---
order: 1
title: CMA Lab - Part A
---
# Computer Multimedia and Animation - Lab Part A

## Q1. Write a HTML/5 program to demonstrate the use of Font family, font variant, font style, and font size. 


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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/prg1)

<iframe src="https://sounddrill31.github.io/html-demos/prg1/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

## Q2. Write a HTML/5 program to display random contents using list properties: 
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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/prg2)

<iframe src="https://sounddrill31.github.io/html-demos/prg2/" style="border:0px #ffffff none;" name="myiFrame" scrolling="yes" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

## Q3. Write a HTML/5 program to create gradient using css. 

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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/prg3)

<iframe src="https://sounddrill31.github.io/html-demos/prg3/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

## Q4. Write a HTML/5 code to demonstrate following CSS animation properties: 
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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/prg4)

<iframe src="https://sounddrill31.github.io/html-demos/prg4/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

## Q5. Write a HTML/5 program to demonstrate key frames 

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

::: details Show output

[View Webpage](https://sounddrill31.github.io/html-demos/prg5)

<iframe src="https://sounddrill31.github.io/html-demos/prg5/" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="200px" width="200px" allowfullscreen></iframe>

:::

## Q6. Write a HTML/5 code to demonstrate CSS transition and transformation. 
## Q7. Write a HTML/5 program to turn on/off a light bulb using JavaScript. 
Make use of gif image and buttons. 
