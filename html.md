



---
## OVERVIEW
- HTML = content / structure (core focus...)
- CSS = style (a little bit...)
- JS = behaviour / interaction (a little bit...)
- bandwidth focus more html and less of css/js




---
## STRUCTURE
- https://in.pinterest.com/pin/345862446359675335/

<br>Should be the first site
```markdown
index.html
```

<br>Standard structure in the html-file
```markdown
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">                                                      # Define standard charset
        <meta name="description" content="Techcrunch">                              # Description of the site
        <meta name="keywords" content="one, two, three">                            # Keywords of the site
        <meta name="viewport" content="width=device-width, initial-scale=1">        # Viewport Definition
        <title>Techcrunch</title>                                                   # Title of the site
        <link rel="preconnect" href="https://fonts.gstatic.com">                    # Use Google Font Style
        <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">     # Use Google Font Style
        <link rel="stylesheet" href="css/normalize.css">                            # Normalizing the CSS-Browser-Styles
        <link rel="stylesheet" href="css/techcrunch_layout1.css">                   # External CSS-File-Link
        <script src="https://kit.fontawesome.com/bf5e040b82.js" crossorigin="anonymous"></script>       # Use FontAwesome Icons
    </head>
    <body>
        <!--Everything the user sees -->
    </body>
</html>
```



---
## GROUPING, LAYOUT
- https://www.w3schools.com/html/html_layout.asp

<br>grouping some html-area
```markdown
<div></div>
```
main part of the homepage
```markdown
<main></main>
```
part of the homepage - eg. the core middle of the site
```markdown
<section></section>
```
part of the section - can be taken and dropped to another place
```markdown
<article></article>
```
mostly on the side of the homepage - something you can take away and the page would still be working (eg. ads)
```markdown
<aside></aside>
```
eg. menue at the title
```markdown
<header>...</header>
```
Navigation info for the user (unordered ul list normaly)
```markdown
<nav></nav>
```
bottom of the document
```markdown
<footer></footer>
```



---
## ELEMENTS
- https://www.w3.org/community/webed/wiki/HTML/Training/Tag_syntax#:~:text=HTML%20is%20using%20tags%20for,to%20compose%20an%20HTML%20element.
- https://developer.mozilla.org/de/docs/Web/HTML/HTML5/HTML5_element_list

<br>commentar in HTML
```markdown
<!-- This is a comment -->
```
anker link element
```markdown
<a href="www.x.com">X</a>
```

<br>form element
```markdown
<form action="search.html" method="post">
    <label>Search:</label>
</form>
```

<br>Normal Paragraph (long text)
```markdown
<p>text</p>
```
Paragraph / Text with anchor link
```markdown
<p>Text <a href="www.x.com">X</a></p>
```
Paragraph with a class
```markdown
<p class="nine">Hello</p>
```
Short text
```markdown
<span>text</span>
```
Header1-Tag with Text (most important on the page)
```markdown
<h1>Import Header</h1>
```
Header2-Tag with Text (second important)
```markdown
<h2>2nd important thing</h1>
```
Header6-Tag with Text (sixth important thing on the page)
```markdown
<h6>6th important thing</h1>
```
Insert picture - no close tag (with alternative text - when img can´t be displayed)
```markdown
<img src="pic.jpeg" alt="text">
```
Preserves whitespace (not good - should be done by CSS)
```markdown
<pre> </pre>
```
linebreak (not good - should be done by css)
```markdown
<br>, </br>
```
htmlbreak (not good - should be done by css)
```markdown
<hr>, </hr>
```
Emphasis some text - but only for accessibility reason (not styling!)
```markdown
<em> Stress Emphasis </em>
```
Bold some text - but only for accessibility reason (not styling!)
```markdown
<strong> Strong Importance </strong>
```
Insert / embedd video with iframe
```markdown
<iframe src="" frameborder="0"></iframe>
```
Set JumpMark at a specific position in the html-file (jump to with index.html#1)
```markdown
<a id="1"></a>
```

<br>Insert video
```markdown
<video width="400" controls>
  <source src="mov1.mp4" type="video/mp4">
  <source src="mov2.ogg" type="video/ogg">
  Your browser does not support HTML video.
</video>
```


<br>Unordered List with anchor links
```markdown
<ul>
    <li><a href="x.html">One</a></li>
    <li><a href="y.html">Two</a></li>
    <li><a href="z.html">Three</a></li>
</ul>
```

<br>Ordered List
```markdown
<ol>
    <li>One</li>
    <li>Two></li>
    <li>Three></li>
</ol>
```

<br>Table Definition
```markdown
<table>
    <tr>
        <th>First table header</th>
        <th>Second table header</th>
    </tr>
    <tr>
        <td>First row, first column</td>
        <td>First row, second column</td>
    </tr>
    <tr>
        <td>Second row, first column</td>
        <td>Second row, second column</td>
    </tr>
</table>
```


---
## FORMS, BUTTONS
<br>Different input fields can be arranged in a form tag
```markdown
<form> ... </form>
```
Label is shown before the element(for-name should be ident with the id-name or name-tag of the object)
```markdown
<label for="name">First Name:</label>
```
Text-Inputfield - with id, name and value (default)
```markdown
<input type="text" id="name"  name="" value="">
```
Telephon-Inputfield - with id, name and value (default)
```markdown
<input type="tel" name="" value="">
```
EMail-Inputfield - with id, name and value (default)
```markdown
<input type="email" name="" value="">
```

<br>Range/Slider-Inputfield with id, name, min/max-value for the slider, value (default) and data-sizing-definition (px)
```markdown
<input type="range" id="xyz" name="xyz" min="0" max="25" value="10" data-sizing="px"#
```

<br>Definition of a TextField for input with id, name, number of rows and columns
```markdown
<textarea id="textField" name="w3review" rows="4" cols="50">
    Pls input your UPPERCASE text here!
</textarea>
```

<br>Define Button with id, name and text on the button
```markdown
<button id="check" type="button" name="button">check</button>
```



---
## TEMPLATE
see Learning-Documentation
<a href="../docs/htmlTemplate.zip">link</a>



---
## MARKDOWN FILE INTEGRATION
- Create Text-File
- Convert Text-File with ConverTXT_MD.py to MD-File
- Read MD-File with Markdown Monster - check if formating is ok in the editor
- Save To - Save to HTML - Choose Zip Archive - store the zip-file somewhere and extract
- Copy the part from <Markdown Monster Content> to <End Markdown Monster Content> in the HTML-File



---
## CHROME EXTENSION TOOLS
- Wappalyzer - tool for showing which CMS is used, which e-commerce platform, marketing automation tool
- Window Resizer - resize the window for reponsive design
- Viewport Resizer - resize the window for reponsive design
- Marmoset - make an eye-catching snapshot form your code
- CSSViewer - show the css-styles on a site
- WhatFont - shows the used font on the site
- Lighthouse - audit the site - gives feedback what can / should be improved







