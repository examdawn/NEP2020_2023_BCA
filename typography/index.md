# Markdown Typography Guide
## A Collection of Simple Styles
You can Use any of the Below styles to customize and beautify your content. Markdown is extremely simple and can be done by anyone, even if you've never used it before! In my personal opinion, it is even simpler than using MS Word or LibreOffice Writer

Credits:
- Official Docs which I used as reference. [\[Link\]](https://vitepress.dev/guide/markdown)
- Github Guide for this which I also used as reference. [\[Link\]](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### Headings
```
# H1
## H2
### H3
```
and so on...
::: details Show How it Looks 
# H1
## H2
### H3
:::

### Italics, bold, etc
```
*simple italics*

**bold text**

***bold italics***

~~Strikethrough text~~
```
::: details Show How it Looks 
*simple italics*

**bold text**

***bold italics***

~~Strikethrough text~~
:::

### Bullet Points
```
Some Text Here:
- Point1
    - Subpoint1
    - Subpoint2
```

::: details Show How it Looks 
Some Text Here:
- Point1
    - Subpoint1
    - Subpoint2
:::

### Tables
```
| Month    | Savings |
| -------- | ------- |
| January  | $250    |
| February | $80     |
| March    | $420    |
```

For More info on markdown tables

::: details Show How it Looks 
| Month    | Savings |
| -------- | ------- |
| January  | $250    |
| February | $80     |
| March    | $420    |
:::
### Quote
```
> Some Text or FAQ here.

Response text...
```

::: details Show How it Looks 
> Some Text or FAQ here.

Response text...
:::
### Alerts
```
> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.
```
::: details Show How it Looks 
> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.
:::
### Custom Containers
```
::: info
This is an info box.
:::

::: tip
This is a tip.
:::

::: warning
This is a warning.
:::

::: danger
This is a dangerous warning.
:::

::: details
This is a details block.
:::
```

:::: details Show How it Looks 
::: info
This is an info box.
:::

::: tip
This is a tip.
:::

::: warning
This is a warning.
:::

::: danger
This is a dangerous warning.
:::

::: details
This is a details block.
:::
::::

You can use containers to Show/Hide given content as well.
```
::: details Your Title Here 
Your hidden text here
:::
```

:::: details Show How it Looks 
::: details Your Title Here 
Your hidden text here
:::
::::

::: details More Info on Nested Containers 
If you're interested in Nested Containers like how we have above, please read this to get an idea of how to do it: https://github.com/vuejs/vitepress/issues/764
:::
### Code Blocks
Vitepress uses shiki to render code blocks and perform syntax highlighting. 

For a list of supported languages, please check out [the official list](https://shiki.style/languages).
```
```C
#include <stdio.h>
void main()
{
    printf("Hello world");
}
```
```
::: details Show How it Looks
```C
#include <stdio.h>
void main()
{
    printf("Hello world");
}
```
:::

You can also add `// [!code focus]` at the part where you want to focus the code
```
```C
#include <stdio.h>
void main()
{
    printf("Hello world"); // [!code focus]
}
```
```

::: details Show How it Looks
```C
#include <stdio.h>
void main()
{
    printf("Hello world"); // [!code focus]
}
```
:::

### Equation and Math

<!--Need to do npm add -D markdown-it-mathjax3 and math: true in config -->

Here is a formula to calculate the Cut-off Frequency of a Low Pass Filter(Hz) that is built as an RC circuit:
```math
$$
f_c = \frac{1}{2\pi RC}
$$
```
::: details Show How it Looks 
$$
f_c = \frac{1}{2\pi RC}
$$
:::

### More Info
For more advanced features, I highly suggest taking 10 to 15 minutes and reading through the official docs: https://vitepress.dev/guide/markdown

It is definitely helpful and allows you to stylize your content better.