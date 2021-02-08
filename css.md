# CSS
---

#### GENERAL [jump to...](#general)
#### ATTRIBUTES [jump to...](#attributes)
#### FORMATING SNIPPETS [jump to...](#formating-snippets)
#### FONT DEFINITION [jump to...](#font-definition)
#### ICON USE [jump to...](#icon-use)
#### PARENT CHILD RELATIONSHIP [jump to...](#parent-child-relationship)
#### SELECTORS AND COMBINATIONS [jump to...](#selectors-and-combinations)
#### CLASSES [jump to...](#classes)
#### ID [jump to...](#id)
#### INLINE STYLE [jump to...](#inline-style)
#### SPECIFICITY [jump to...](#specificity)
#### PSEUDO CLASSES [jump to...](#pseudo-classes)
#### BOX MODEL [jump to...](#box-model)
#### LAYOUTS, FLOATING [jump to...](#layouts-floating)
#### LAYOUT FLEXBOX [jump to...](#layout-flexbox)
#### LAYOUT GRID [jump to...](#layout-grid)
#### RESPONSIVE DESIGN [jump to...](#responsive-design)
#### MEDIA QUERIES [jump to...](#media-queries)
#### ANIMATING, TRANSFORM [jump to...](#animating-transform)
#### VARIABLES [jump to...](#variables)
#### TEMPLATE [jump to...](#template)
#### PERFORMANCE ORGANIZATION [jump to...](#performance-organization)
#### CHROME HACKS [jump to...](#chrome-hacks)
#### PREPROCESSORS [jump to...](#preprocessors)
#### SASS [jump to...](#sass)



---
## GENERAL
[jump to top...](#css)<br><br>
- should go in seperate file (better than inline or in the head)
- css statements are called "rules"
- resetting all browser-styles: http://meyerweb.com/eric/tools/css/reset/
- normalize the alle browser-styles: github.com/necolas/normalize.css

<br>link the html-file to the css-file
```markdown
<link rel="stylesheet" href="css/style.css">
```
comment in css
```markdown
/* comment */
```

<br>syntax of the css statement / rule
```markdown
p {
    color: red;                                 /* (p => selector, color:red; => declaration) */
}                                               /* color => property, red => value) */
```

<br>set rule with 2 declerations for p => red and bold
```markdown
p {
    color: red;
    font_weight: bold;
}
```

<br>Cascade Rules (but Specificity overrules - see below)
```markdown
p {                                             /* cascading rules (from top to bottom, step by step) */
    color: red;                                 /* output is blue+bold */
    font_weight: bold;
}
p {
    color: blue;
}
```



---
## ATTRIBUTES
[jump to top...](#css)<br><br>
https://www.w3schools.com/cssref/
<br>Define red color for element
```markdown
color: red;
```
Define color with hex code
```markdown
color: #FF0000;
```
Defome color with rgb code (4th parameter is opaque - 0.5. means half transparent, 1 no transparent)
```markdown
color: rgba(255,0,0,1);
```
define color per hsla value
```markdown
color: hsla(0, 100%, 50%,1);
```
Font bold
```markdown
font_weight: bold;
```
Define when a font is downloaded from eg. google fonts
```markdown
font_weight: 700;
```
Define font size with 25 pixel
```markdown
font-size: 25px;
```
Font italic / cursive
```markdown
font-style: italic;
```
Defines line-height as 1.5 of the normal height
```markdown
line-height: 1.5;
```
Define text decoration a red underline
```markdown
text-decoration: underline red;
```
Define text with line-through
```markdown
text-decoration: line-through;
```
Center text / or list-entries in ul
```markdown
text-align: center;
```
Display text as blocktext (left and right in a line)
```markdown
text-align: justify;
```
Make text uppercased
```markdown
text-transform: uppercase;
```
Define background color
```markdown
background-color: #e2b007;
```
Define border of element (width, style, color) - "shorthand"-method
```markdown
border: 3px solid #FFA500;
```
Define border of element (width, style, color) - "shorthand"-method
```markdown
border: thin solid red;
```
Define only the bottom-border - "longhand"-method
```markdown
border-bottom: 6px dashed #FFA500;
```
Define only the bottom-border-width - "longhand"-method
```markdown
border-bottom-width: 12px;
```
Define a border radius with 5 pixel - "shorthand"-method
```markdown
border-radius: 5px;
```
Define the border radius for top right corner  - "longhand"-method
```markdown
border-top-right-radius: 5px;
```
Define border color with red
```markdown
border-color: red;
```
Define border width with 1px/2px (clockwise => up-rigth-down-left)
```markdown
border-width: 1px 2px 1px 2px;
```
Define border style
```markdown
border-style: solid;
```
Height of the box
```markdown
height: 100px;
```
Margin of the box (outside the border, for all 4 sites) - "shorthand"-setting
```markdown
margin: 20px;
```
Margin of the box (10 pixel for top/bottom and 20 pixel for left/right)
```markdown
margin: 10px 20px;
```
Margin of the box (clockwise from tom) => 10px top, 20px right, 0px bottom, 115px left
```markdown
margin: 10px 20px 0 15px;
```
Margin of the box => will do this clockwise for top+right and bottom-left => 100px for top+bottom, 0 for right+left
```markdown
margin: 100px 0;
```
Set the margin automatc - wg. when the width is set to a percentage
```markdown
margin: auto;
```
Center the content horizontal
```markdown
margin: 0 auto;
```
Setting the margin to 10 pixel - "longhand"-method
```markdown
margin-top: 10px
```
Padding on all sides
```markdown
padding: 20px;
```
Padding only on the bottom side (values are going clockwise starting at the top)
```markdown
padding: 0 0 20px 0;
```
Padding on the left and right - no padding at top and bottom
```markdown
padding: 0 10px;
```
Setting the padding to 6 pixel - "longhand"-method
```markdown
padding-left: 6px
```
Define width in percent (relative to the width of the parent element)
```markdown
width: 50%;
```
Define width (calculated on elements font size - when font-size=14px - the width would be 70px (5*14)
```markdown
width: 5em;
```
Define width (and reserve additional 10px for eg. the margin of each element)
```markdown
width: calc(33.3% - 20px)
```
Define height of element
```markdown
height: 200px;
```
Resize something eg. img
```markdown
max-width:20%;
```
Prevents the eg. image from getting bigger than its original size
```markdown
max-width:100%;
```
Resize something eg. img
```markdown
max-height:20%;
```
no bullets in unordered list (using at ul-element)
```markdown
list-style-type: none;
```
hide element
```markdown
disply: none;
```
show element in line - eg. horizontal li-elements - or wrap border only around a paragraph p (and not the whole block)
```markdown
display: inline;
```
show element as a block (max width of the window) - eg. wrap border around a span element over the whole window (and not only the span)
```markdown
display: block;
```
show elements in the block in a line - eg. all p-elements in a div-element
```markdown
display: inline-block;
```
show elements in the block in the flex system
```markdown
display: flex;
```
Define floating for an image (text will float her on the right side of the image)
```markdown
float: left;
```
Clear floating (for left and right)
```markdown
clear: both;
```
Change the background fading in for 5 seconds	(eg. going from white to dark blue)
```markdown
transistion: background 5s;
```
Static element - is not positioned in any way (position tags top-bottom-left-rigth will have no effect)
```markdown
position: static;
```
With the position tags (top, botom, left, right) the element is shifted away from its normal position
```markdown
position: relative;
```
Element stays according the position tags - but will not change the place even if the windows is scrolled
```markdown
position: fixed;
```
Default-value - we can see the content when it overflows
```markdown
overflow: visible;
```
Hides the overflow (can not see the text which is outside the box)
```markdown
overflow: hidden;
```
Shows a scrollbar when the content is overflowing
```markdown
overflow: auto;
```
Can overlap other elements - element with the highest z-index in front
```markdown
z-index: 2;
```
Make a picture darker
```markdown
filter: brightness(40%);
```
Make cursor a pointer when going over the element
```markdown
cursor: pointer;
```
Disable highlighting of text selection
```markdown
user-select: none;
```
Make copyright-sign
```markdown
&copy
```



---
## FORMATING SNIPPETS
[jump to top...](#css)<br><br>
center an unordered list
```markdown
ul {
   text-align: center;					# center the whole ul in the block
}
ul li {
   display: inline-block;				# arrange list elements vertically
   list-style-type: none;			   	# not dots for the list elements
}
```

<br>show sepeartor between unordered list
```markdown
li + li:before{
    content: " | ";
    padding: 0 3px;
}
```

<br>resize a block element and center it
```markdown
(if using only "width" => when the window is to small - the browser resolves this with a horizontal scrollbar)
(so its better to use "max-width" => this reduces the width when the windows is / becomes to small)
    max-width: 600px;
    margin: 0 auto;
```

<br>let a image float right - and let the text float around it in the left and bottom area around the picture
```markdown
img {
  float: right;
  margin: 0 0 1em 1em;
}
```

<br>when floating and the image is bigger then the element use this so the element is adjusted to the image heigth
```markdown
.clearfix {
  overflow: auto;
}

```

<br>nav menue on the left side - with several section beside the nav in the right area
```markdown
(with a percentage parameter - better then fixed px-amounts especially when using smaller windows)
nav {
  float: left;
  width: 25%;}
section {
  margin-left: 25%;
}
```

<br>show all elements in a div-block flexible as inline
```markdown
div {
    display: inline-block;
    width: 300px;
    height: 100px;
    margin: 1em;
}
```


<br>size div automatically according to the content
```markdown
height: fit-content
```

<br>styling link based on state
```markdown
a:link {...}		=> format link when not allready clicked
a:visited {...}		=> format link when allready clicked
a:hover {...}		=> format link when hovered over with the mouse
```

<br>center the whole site in the middle
```markdown
body {
	width: 75%;						# space which can be taken by the body
	margin: 0 auto;}				# rest of the space (=25%) will be splitted left and right
```

<br>make media scalable
```markdown
img, video, canvas {
	max-width: 100%;}
```

<br>show different images depending on browser width
```markdown
<picture>
  <source srcset="img_smallflower.jpg" media="(max-width: 600px)">
  <source srcset="img_flowers.jpg" media="(max-width: 1500px)">
  <source srcset="flowers.jpg">
  <img src="img_flowers.jpg" alt="Flowers" style="width:auto;">
</picture>
```

<br>define variable at the very beginning:
```markdown
:root {
  --primary-color: #047aed
}
```
<br>use the variable somewhere in the css:
```markdown
background-color: var(--primary-color);
```

<br>no border when entering an input field
```markdown
input:focus {
  outline: none;
}
```

<br>button attention (makes button during hovering a little bit smaller)
```markdown
transform: scale(0.98);
```

<br>button / picture attention (shift button / pic up for 15px when hoovered)
```markdown
transform: translateY(-15px);}				# shift up element for 15px when hoovered
transition: 1.5s ease;						# make smooth transisition (with ease => slow - than fast - than slow again)
```

<br>make a obliquely line
```markdown
.element::before					# define area before the element
.element::after						# define area after the element
	height: 100px;					# define heigth for the element
	transform (skeyY(-3deg);		# make it oblique before / after the element
```



---
## FONT DEFINITION
[jump to top...](#css)<br><br>
https://fonts.google.com/
<br>taken from google fonts for example (take fonts and then create link in upper right corner for the link
```markdown
<head>                     # define in html in the header
    <link href="https://fonts.googleapis.com/css2?familiy=Source+Sans+Pro:wght@300;400;700&display=swap" rel="stylessheet">
</head>
```

<br>Helvetica and sans-serif are the fallback fonts when Source Sans Pro is not loading
```markdown
p {
    font-family: "Source Sans Pro", "Helvetica", sans-serif;
	font-weight: 700;				# how thick / bold the font is
}
```


---
## ICON USE
[jump to top...](#css)<br><br>
Using icons directly from https://fontawesome.com/
```markdown
<head>      # Definition in the head
	<script src="https://kit.fontawesome.com/bf5e040b82.js"
        crossorigin="anonymous"></script>
</head>
<i class="fas fa-search">		# use icon in css (change size, color)
```

<br>Using svg-files
```markdown
put full svg-code (source) of the svg in a svg-tag
		like: <svg enable-background="new 0 0 515.91 728.5"
            height="512" id="Layer_1" version="1.1"
            xmlns="http://www.w3.org/2000/svg"...</svg>
		change all fill="#123456" entries to fill=currentColor
put a div-wrapper around the svg-element (and probably a a-tag for a link around the wrapper too)
		like: <div class="wrapperSVG"> ... </div>
format the svg:						# for sizing the svg-icon with width and height
	svg {
		width: 1.4%;
		height: 1%;}
format the div-wrapper:				# for coloring and positioning the svg-icon (in the wrapper)
	div.wrapperSVG {
		color: var(--darkest);
		display: inline;
		position: relative;
		top: 3px;
	}
```


---
## PARENT CHILD RELATIONSHIP
[jump to top...](#css)<br><br>
Overview Complex Selectors see: https://learn.shayhowe.com/advanced-html-css/complex-selectors/
<br>direct parent/child relationship
```markdown
<section>
    <p>hello, twitch!</p>
</section>                 # direct parent relationsship > child connection with ">"
section > p {              # direct child connection (only the p which are direct unter section
    color:red;             # p is the direct child of section
}
```

<br>normal parent/child realtionship
```markdown
<section>
    <article>
        <p>hello, twitch!</p>
    </article>
</section>                 # normal parent child connection (ignores deepeness)
section p {                # all connections above (when there is a p - somewhere on a level - in the section)
    color:red;             # p is the grandchild of section / somewhere a child of section
}
```

<br>Sibling Relationship
```markdown
<section>
    <p>Hello, Twitch!</p>
	<p>Hello, YouTube!</p>
</section>				   # previous sibling + next sibling
p + p {					   # format is used when two <p>s are after each other
	color: red;			   # only the second p will get red
}
```



---
## SELECTORS AND COMBINATIONS
[jump to top...](#css)<br><br>
<br>Type Selector - Select one specific type
```markdown
h1 {...}
```
Universal Selector - Select everything
```markdown
* {...}
```
Class Selector - Select specific class
```markdown
.box {...}
```
ID Selectors - Select specific ID
```markdown
#unique {...}
```
Attribute Selectors - Select elements which have the attribute "title"
```markdown
Attribute selector	a[title] {...}
```
Pseudo Class Selector - Select elements with special state (eg. first-child, hover, focus, clicked,...)
```markdown
p:first-child {...}
```
Pseudo Elements Selector - Style a specific part of the selected element (eg. first-letter, first-line,...)
```markdown
p::first-line {...}
```
Descendant combinator - all connections above (when there is a p - somewhere on a level - in the article)
```markdown
article p
```
Child Combinator - direct child connection (only the p which are direct unter article)
```markdown
article > p
```
Adjacent Sibling - format is used when a p-element is following directly after a h1-element
```markdown
h1 + p
```
General Sibling - selects any p-element which is following somewhere after a h1-element
```markdown
h1 ~ p
```
selects any span-element that is inside a p-element, which is inside an article-element
```markdown
article p span {...}
```
selects any p-element that comes directly after a ul-element, which comes directly after an h1-element
```markdown
h1 + ul + p {...}
```
select elements with class "special" which are somwhere after p which is directly after h1 which is somewhere in the body
```markdown
body h1 + p .special {...}
```



---
## CLASSES
[jump to top...](#css)<br><br>
class is used for formating many different elements
```markdown
<section>
	<p class="robot">Hello, Twitch!</p>
	<p id="zebra" class="bob">Hello, YouTube!</p>
	<p class="bob">Goodbye!</p>
</section>
.bob {
	color: red;
}
```
<br>both classes have to be in the SAME element
```markdown
.class1.class2 {...}
```
both classes have to be in the SAME element - only for p-elements
```markdown
p.class1.class2 {...}
```
the parent-element has to be class1 and the child-element class2
```markdown
.class1 .class2 {...}
```
the parent-element section has to be class1 and the child-element h2 class2
```markdown
section.class1 h2.class2 {...}
```
one of the classes have to be in the element
```markdown
.class1,.class2 {...}
```
rule is for p with class1+class2 or a with class2
```markdown
p.class1.class2, a.class2 {...}
```
h2, which have class2+classe3 in h2, their parent has class1, and the parent is in body
```markdown
body article.class1 h2.class2.class3 {...}
```
rule for h3 which have a parent-element aside with class aExtra
```markdown
aside.aExtra h3
```




---
## ID
[jump to top...](#css)<br><br>
id is used for formating unique elements
```markdown
<section>
	<p>Hello, Twitch!</p>
	<p id="zebra">Hello, YouTube!</p>
</section>
```
<br>can used only ONE time - only one id per element - nothing else can have this id
```markdown
#zebra {color: red;}
```
one of the ids have to be in the element
```markdown
#class1,#class2 {...}
```
h2, which has id=rhino, the parent has class=top and the parent is in body
```markdown
body section.top h2#rhino {...}
```
rule for h2 which have a parent-element section with id aMilk
```markdown
section#aMilk h2
```




---
## INLINE STYLE
[jump to top...](#css)<br><br>
!important
```markdown
.bob {
	color: red !important;						# with !important this style get the maximum priority / overwrites everything
}												# not often used - eg. in cases of immediate urgency to show something - when a error is not found cxurrently
```



---
## SPECIFICITY
[jump to top...](#css)<br><br>
https://down4kode.wordpress.com/2014/05/21/css-specificity-calculator/
<br>defines the priority which styles can overwrite which style
```markdown
priority has the style which came later - but only when the specificity is equal or higher!
1 point for tags
10 points for classes
100 points for ids
1000 points for Inline Style
```
<br>1 point (1 tag)
```markdown
p{}
```
100 points (1 id)
```markdown
#zebra{}
```
11 points (1 tag + 1 class)
```markdown
section .bob { }
```
1010 points (1 class + 1 other)
```markdown
.bob{ !important }
```
11 points (1 tag + 1 class) for section1 and for section2
```markdown
section1,section2 .bob { }
```




---
## PSEUDO CLASSES
[jump to top...](#css)<br><br>
overview see: https://learn.shayhowe.com/advanced-html-css/complex-selectors/
<br>special classes which are dinamically populated as a result of user actions of document structure
```markdown
a:link{...}								=> format link when not clicked
a:visited{...}							=> format link when allready clicked
a:hover{...}							=> format link when hoovered over it
li:first-child							=> Selects an element that is the first within a parent
li:last-child							=> Selects an element that is the last within a parent
p:first-of-type							=> Selects an element that is the first of its type within a parent
p:last-of-type							=> Selects an element that is the last of its type within a parent
div p:nth-child(2)						=> Select the second p-child in the div-element
```



---
## BOX MODEL
[jump to top...](#css)<br><br>
https://en.wikipedia.org/wiki/CSS_box_model#/media/File:Boxmodell-detail.png
<br>every element is a box - box in the middle
<br>box has a heigth and width - eg. 100px*100px
<br>padding outside the box - between box and border (top,right,bottom,left)
<br>border (outside padding) (top,right,bottom,left)
margin (outside border) (top,right,bottom,left)<br>
eg. h1, p - break to new line, fill the maximum available space, width and heigth will be respected
```markdown
block boxes
```
eg. a, span, em, strong - will not break to new line, use only the minium space, width/heigth will not apply
```markdown
inline boxes
```
With this statement every sizing is included with the border
```markdown
*{box-sizing: border-box}
```




---
## LAYOUTS, FLOATING
[jump to top...](#css)<br><br>
=>old layouting - not state of the art!
<br>element tries to got as much up to the top - and as much left (or right according if floated left or right)
<br>normaly everything will float to the left

<br>example1 - without cass all the elements will be positoned from top to bottom
```markdown
Positioning Content
<header>...</header>
<section>...</section>
<aside>...</aside>
<footer>...</footer>

section {									# with that css-command section and aside will be on the same level
	float:left;								# section on the left side and aside on the right side
}
aside {
	float:right;
}

section {									# with that css-command section and aside will be on the same level
	float:left;								# section on the left side with 63% of the space and aside with 30% of the space
	margin 0 1.5%;							# both have a margin outside the element
	width: 63%
}
aside {
	float:right;
	margin 0 1.5%;
	width: 30%
}
footer {
	clear: both;							# after the float - the floats have to be cleared to get the old normal vertically float
}
```

<br>example2 - without cass all the elements will be positoned from top to bottom
```markdown
<header>...</header>
<section>...</section>
<section>...</section>
<section>...</section>
<footer>...</footer>

section {									# with that all 3 section elements will float left
	float: left								# so they are horizontal alligned side by side
	margin 0 1.5%;							# width has to be adjusted accordingly
	width: 30%
}
footer {
	clear: both;							# after the float - the floats have to be cleared to get the old normal vertically float
}
```



---
## LAYOUT FLEXBOX
[jump to top...](#css)<br><br>
css-tricks.com: Complete Guide To Flexbox<br>
Initialize flexcontainer (parent element as a block)
```markdown
display: flex;
```
Initialize flexcontainer (as inline-element - not as block)
```markdown
display: inline-flex;
```
Items are placed horizontal from left to right (DEFAULT)
```markdown
flex-direction: row;
```
Items are placed horizontal from rigth to left (main axis is horizontal and cross axis is vertical)
```markdown
flex-direction: row-reverse;
```
Items are placed vertical top to bottom
```markdown
flex-direction: column;
```
Items are placed vertical top to bottom (main axis is vertical and cross axis is horizontal)
```markdown
flex-direction: column-reverse;
```
No wrapping - shows all items in one line (overwrites element width) (DEFAULT)
```markdown
flex-wrap: nowrap;
```
Wrap elements to next line in the flexcontainer section (according to the width)
```markdown
flex-wrap: wrap;
```
Wrap elements but start at the bottom left corner(and going from left to right)
```markdown
flex-wrap: wrap-reverse;
```
Combination from direction + row (same as flex-direction:	row and flex-wrap: wrap)
```markdown
flex-flow: row wrap;
```
Give every element equal space / proportion
```markdown
flex: 1;
```
One element or all elements should have 2 proportions - eg. more space for a specific item
```markdown
flex: 2;
```
Defines the order of the specific element (if > 0 then put it at the end - when < 0 put it at the very beginning)
```markdown
order: 1;
```
Show every item in a single line in the flexcontainer section
```markdown
flex-wrap: nowrap;
```
Wrap elements to next line in the flexcontainer section
```markdown
flex-wrap: wrap;
```
Combination from direction + row (same as flex-direction:	row and flex-wrap: wrap)
```markdown
flex-flow: row wrap;
```
Put elements to the max left/top (for the main axis) (DEFAULT)
```markdown
justify-content: flex-start;
```
Put elements to the max right/bottom (for the main axis=
```markdown
justify-ccontent: flex-end;
```
Center the elements (for the main axis)
```markdown
justify-content: center;
```
Place elements with equal space around the elements (for the main axis)
```markdown
justify-content: space-around;
```
Place elements with equal space between the elements (for the main axis)
```markdown
justify-content: space-between;
```
Stretches the elements on the cross axis (DEFAULT)
```markdown
align-items: stretch;
```
Align elements from the top or left (for the cross axis)
```markdown
align-items: flex-start;
```
Align elements from the bottom or right (for the cross axis)
```markdown
align-items: flex-end;
```
Center the elements (for the cross axis)
```markdown
align-items: center;
```
Align elements on the baseline of the elements (for the cross axis) - eg. when there are different font-sizes in the flex-items
```markdown
align-items: baseline;
```
Align individual element at the bottom or right (for the cross axis) - overwrittes the align-items-setting for the single item
```markdown
align-self: flex-end;
```
Gives the flex-item 1 proportion value (when there are 3 items - every item gets the same space)
```markdown
flex: 1 200px;
```
Give the element 5times the overall room - eg. 3 items get 1 spaces and 1 item get 5 spaces (8 spaces overall)
```markdown
flex: 5;
```
Gives the 3rd item 2 proportion (item 1+2 get 1/4 of the space - item 3 gets 1/2 of the space)
```markdown
article:nth-of-type(3) { flex: 2 200px; }
```
Overwrites the vertical position of the item in the flexcontainer
```markdown
button:first-child { align-self: flex-end; }
```
Change the order of the first item (everything has order 0 - with 1 it goes to the very right position)
```markdown
button:first-child { order: 1; }
```
Change the order of the last item (everything has order 0 - with -1 it goes to the very first position)
```markdown
button:last-child { order: -1; }
```

<br>flex-basis, flex-grow, flex-shrink (longhanded values for flex)
```markdown
flex: 10 5 400px								# means 10 for flex-grow, 5 for flex-shrink, 400px for flex-basis
	=> flex-basis: set the basis width of the flex-element
	=> flex-grow: how to deal with the extra-space (in the main axis)
	=> flex-grow: when there is extra space would should be done with them - DEFAULT is 0 => do nothing
	=> flex-grow: when set to 1 for one element the whole extra-space will be taken for this element
	=> flex-shrink: what to do when there is not enough space when the window gets shrinked
	=> flex-shrink: DEFAULT is 0 - when there is not enough space the elments get shrinked equally
```



---
## LAYOUT GRID
[jump to top...](#css)<br><br>
<br>Define grid for the layouting as block)
```markdown
display: grid;
```
Define grid as inline-block
```markdown
display: inline-grid;
```
Define 3 fixed columns with 200px each
```markdown
grid-template-columns: 200px 200px 200px;
```
Define 3 flexible columns with fr-units (define 3 columns with max possible place)
```markdown
grid-template-columns: 1fr 1fr 1fr;
```
2nd way: Define 3 flexible columns with fr-units (define 3 columns with max possible place)
```markdown
grid-template-columns: repeat(3, 1fr);
```
3rd way: Define 3 flexible columns with auto
```markdown
grid-template-columns: auto auto auto;
```
Define 3 flexible columns with fr-units (4 spaces - 1st column takes 2; 2nd+3rd colujmn take 1)
```markdown
grid-template-columns: 2fr 1fr 1fr;
```
Create as many columns as will fit into the container
```markdown
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
```
Define gap between the elements (20 px for rows and columns)
```markdown
grid-gap: 20px;
```
Define gap between the elements (10px for the row-gap and 50px for the column-gap)
```markdown
grid-gap: 10px 50px;
```
Define the gap only for the rows
```markdown
grid-row-gap: 30px;
```
Define the gap only for the columns
```markdown
grid-column-gap: 20px;
```
Define heigth of the row
```markdown
grid-auto-rows: 100px;
```
Define heigth of the row (100px is minimum, auto expand to fit the content)
```markdown
grid-auto-rows: minmax(100px, auto);
```
Use for element grid-columns 1 - 3
```markdown
grid-column 1 / 3;
```
Use for element gird columns 1 and 2
```markdown
grid-column 1 / span 2;
```
Use for element grid-row 1
```markdown
grid-row: 1;
```
Use for element area => grid-row-start / grid-column-start / grid-row-end / grid-column-end
```markdown
grid-area: 1 / 2 / 5 / 6;
```
Arrange grid elements (horizontally) with equal space around every element
```markdown
justify-content: space-evenly;
```
Same space around every grid
```markdown
justify-content: space-around;
```
Same space between the elements
```markdown
justify-content: space-between;
```
Center the elements
```markdown
justify-content: center;
```
Arrange the elements on the starting left side
```markdown
justify-content: start;
```
Arrange the elements on the ending right side
```markdown
justify-content: end;
```
Arrange grid elements (vertically) - center the elements
```markdown
align-content: center;
```
Same options as horizontaly with justify-content
```markdown
align-content: start, space-around,...
```

<br>Element spans from 1st column to thue 3rd column
```markdown
grid-column-start: 1
grid-column-end: 4
```

<br>Element spans from the 1st row to the 2nd row in the 3rd column
```markdown
grid-column: 3;
grid-row-start: 1;
grid-row-end: 3;
```

<br>Name all items
```markdown
.item1 { grid-area: header; }					# Name the different areas
.item2 { grid-area: menu; }
.item3 { grid-area: main; }
.item4 { grid-area: right; }
.item5 { grid-area: footer; }
.gid-container {
  grid-template-areas:
    'header header header header header header' # Define where the areas should be displayed in the grid
    'menu main main main right right'
    'menu footer footer footer footer footer';
}
```


---
## RESPONSIVE DESIGN
[jump to top...](#css)<br><br>
Running the page on different / smaller devices
```markdown
- Fluid - everything sized with percentage (no fixed measures)
	=> looks more or less good on every windows-size
- Elastic - using em and rem (em looks at the parents fontsize and use this as a base / rem looks at the html-element)
	(set a standard font-size as a base for the whole document)
	=> em: the change has only to be done at the one font-size decleration
	=> rem: the change has only to be done at the font-size from the html
	=> font-size: 62.5%; /* font-size 1em = 10px bei normaler Browser-Einstellung */
	(so everything would response to the default font size from the actual user)
	(only changing the font-size central when changes)
- Content Decision - Mobile First or Desktop to Mobile
	=> first think about the design on mobile (and then bigger and bigger from Tablet to fully desktop)
	=> or make it the other way (desktop design first and then shrinking to mobile version)
	=> decide what should be shown on mobile devices and what not
	=> using media queries
```

<br>Make YouTube-Video responsive
```markdown
.financeToolsDetail .videoContainer {
    position: relative;
    padding-bottom: 56.25%;
    padding-top: 30px; height: 0; overflow: hidden;
}
.financeToolsDetail .videoContainer iframe {
    position: absolute;
    top: 0;
    left: 15%;											# Position the video in the middle of the div-box
    width: 60%;											# Defines how big the video should be displayed (width)
    height: 55%;										# Defines how big the video should be displayed (height)
}
```



---
## MEDIA QUERIES
[jump to top...](#css)<br><br>
smartphones: this rule get only be used when the device width is between 0 and 600 pixel
```markdown
@media screen and (max-width: 600px) {
	h1 { color: blue; }              }
```

<br>tablets: this rule is used when the width is greater 600px
```markdown
@media screen and (min-width: 600px) {
    .middle{color: yellow; }         }
```

<br>desktop: this rule is used when the width is greater 900px
```markdown
@media screen and (min-width: 900px) {
    .middle{color: yellow; }         }
```

<br>this rule is used when the width is between 600px and 900px
```markdown
@media screen and (min-width: 600px) and (max-width: 900px){
	img {border: 2px solid red;}     }
```

<br>use the full length of the width
```markdown
section {
	height: 200px;
	border 1px solid black;
	flex: 1;
}
```

<br>arranges elements in main and class bottom with flex-system
```markdown
main,.bottom {
	display: flex;
}
```

<br>Important addition to the template-columns:
```markdown
<meta name="viewport" content="width=device-width, initial-scale=1">
	=> enables the windows to be zoomed
	(never set initial-scale to none - zooming would be not possible)
```




---
## ANIMATING, TRANSFORM
[jump to top...](#css)<br><br>
<br>combines the follwing 6 rules
```markdown
transform: matrix(1,2,3,4,5,6);
```
move left/right, up/down4kode
```markdown
transform: translate (120px, 50%);
```
change the scale of the object
```markdown
transform: scale (2, 0.5);
```
rotate object (possible for any axes (rotateX, rotateY, rotateZ)
```markdown
transform: rotate (0.5turn);
```
skew object
```markdown
transform: skew(30deg, 20deg);
```
combine some transformations
```markdown
transform: scale(0.5) translate(-100%,-100%)
```

<br>responsible for the animation - is corresponding to a class definition (see below)
```markdown
@keyframes xyzAction{
	0% {transform: rotateZ(0deg)};				# at 0% of the animation nothing should change on the z-axe
	50% {transform: rotateZ(180deg)};			# at 50% of the antimaton the z-axe should rotate 180deg
	100% {transform: rotateZ(360deg)};			# at 100% of the antimaton the z-axe should rotate 360deg
}
```

<br>define the class for the @keyframe above
```markdown
.letRip{}
```
Name of the keyframe (puts together the setup to the keyframe)
```markdown
animation-name: xyzAction;
```
How many times the animation runs (infinite or eg. 5 for 5 times)
```markdown
animation-iteration-count: infinite;
```
Lenght of one duration of the animation eg. 500ms or 0.5sec
```markdown
animation-duration: 500ms;
```
Animation is progressing linear
```markdown
animation-function: linear;
```
Animation is progressing faster to the end
```markdown
animation-function: easy-in-out;
```
Animation is progressing in steps (not smooth)
```markdown
animation-function: step(5,end);
```
Possible values are runnning or pause (can be used with javacript to start/stop)
```markdown
animation-play-state: running;
```
How long the start of the animation delays
```markdown
animation-delay
```
Control of the progression - forward, backward, alternate
```markdown
animation-direction:
```
Animation fill mode
```markdown
animation-fill-mode
```



---
## VARIABLES
[jump to top...](#css)<br><br>
Define variables in css
```markdown
:root {											# Highest possible level of setting a variable
	--var1: 10px;								# Define variable and initialize with 10px
	--var2: #ffd166;							# Define variable and initialize with color hex code
	--var3: 20%;								# Define variable and initialize with percentage value
}
```

<br>Use variables in in css
```markdown
img {											# Eg. using for image-rule
	padding: var(--var1)						# Using Variable
	background: var(--var2)
	max-width: var(--var3)
}
(Changing variable in JS have a look at JS Learning Path / Cheatsheet)
```



---
## TEMPLATE
[jump to top...](#css)<br><br>
see Learning-Documentation
<a href="../docs/htmlTemplate.zip">link</a>



---
## PERFORMANCE ORGANIZATION
[jump to top...](#css)<br><br>
https://learn.shayhowe.com/advanced-html-css/performance-organization/
<br>keep selector shorthand
<br>use no or less ids - better classes
<br>do not use elements before classes (Bad: article.feat Good: .feat)
<br>reuse styles whereever its possible
<br>compress files with gzip
<br>compress / convert images (program PNGGauntlet)



---
## CHROME HACKS
[jump to top...](#css)<br><br>
<br>live the selected element in the browser
```markdown
select the width or heigth - press rigth strg - up/down
```



---
## PREPROCESSORS
[jump to top...](#css)<br><br>
https://learn.shayhowe.com/advanced-html-css/preprocessors/
<br>Haml: Preprocessor for HTML
Ruby must be installed before<br>
Installation of haml
```markdown
gem install haml
```
Compile the .haml-file to html
```markdown
haml index.haml index.html
```

---
## SASS
[jump to top...](#css)<br><br>
(more like a programming language with expressions, loops, if-statements,...)
Many other preprocessors like Jade, Slim, LESS, Stylus, CoffeeScript<br>
Installation of Sass
```markdown
gem install sass
```

