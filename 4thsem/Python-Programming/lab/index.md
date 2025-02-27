---
order: 0
title: Python - Lab View
---
# Python Programming

Others:
- [Lab PartA](parta.md)
- [Lab PartB](partb.md)

## Use Python in Web

::: details More Info
> This is done using [vitepress-python-editor](https://vitepress-python-editor.netlify.app/), which uses [Pyodide](https://pyodide.org/) to run your code and [CodeMirror](https://codemirror.net/) to display it.

Fun fact: this is running completely inside your browser securely without any extra servers, serverless functions or external workers! This also allows our website to stay static and not incur any (additional) cost.
:::

If this feature is not working as expected, [please report it to us!](https://github.com/examdawn/NEP2020_2023_BCA/issues)

> [!WARNING]
> This will not work if your browser is too old or does not support Web Assembly/Web Workers. If you're using a privacy focused browser like cromite, please enable JavaScript JIT and WebAssembly from the permissions menu.

If the Run Button doesn't show the run or loading button, try reloading your browser!

It will take some time to load, especially if your internet is slow.

Example Code:
```python
print("Hello world")
```

::: details Try it out
```python:line-numbers
print("Hello world")
```
<Editor id="helloworld-trial" />
:::
