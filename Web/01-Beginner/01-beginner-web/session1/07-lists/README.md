## Lists

When making web pages, you will often need to create lists.  You may want to created a numbered list to show a sequence of things that need to happen.  You may want to just give a list of things that are grouped together.  Fortunately, HTML lets us create lists very easily.  There are two kinds ordered (`<ol>`) and unordered (`<ul>`).  The ordered list will put a number in front of each item in the list.  An unordered list will simply put a large dot in front of each item in the list.  For both ordered and unordered list, the items will use the `<il>` tags.  For more information on lists, refer to [HTML lists](http://www.w3schools.com/html/html_lists.asp). 

You can easily add a list to your story using `<ul>` and `<li>` tags. Here is an example:

```html
<html>
	<head>
		<title>A day at the dog park</title>
	</head>
	<body>
		<h1>A day at the dog park</h1>
		<p>Today I took the dogs to the park and <strong>we had a great time!</strong></p>
    <img src="http://f.cl.ly/items/2f473l1d233S0S1k3J3d/dogs-playing.jpg">
    <p>After the dogs played with their friends <em>we took a walk around the track together.</em></p>
    <img src="http://f.cl.ly/items/0o0T0V0g261C1R0I022z/walking-the-track.jpg">
		<p>While we were at the dog park we saw many kinds of dogs, including:</p>
		<ul>
			<li>Poodles</li>
			<li>Great Danes</li>
			<li>Black Labs</li>
		</ul>
	</body>
</html>
```

The `<ul>` tag tells the browser this is a list of items. The `<li>` tags are used around each list item.

![Story with list of dogs](https://raw.githubusercontent.com/TriValleyCoderDojo/beginner-web/master/screenshots/Lists_01.png)

If you want the list to use numbers instead of bullet points you can change the `<ul>` tag (unordered list) to an `<ol>` tag (ordered list).

```html
<html>
	<head>
		<title>A day at the dog park</title>
	</head>
	<body>
		<h1>A day at the dog park</h1>
		<p>Today I took the dogs to the park and <strong>we had a great time!</strong></p>
    <img src="http://f.cl.ly/items/2f473l1d233S0S1k3J3d/dogs-playing.jpg">
    <p>After the dogs played with their friends <em>we took a walk around the track together.</em></p>
    <img src="http://f.cl.ly/items/0o0T0V0g261C1R0I022z/walking-the-track.jpg">
		<p>While we were at the dog park we saw many kinds of dogs, including:</p>
		<ol>
			<li>Poodles</li>
			<li>Great Danes</li>
			<li>Black Labs</li>
		</ol>
	</body>
</html>
```

![Story with ordered list](http://cl.ly/image/3x2t1c1N1v3o/content#.png)

-----------------------

**Next HTML Topic:** [Hyperlinks](https://github.com/TriValleyCoderDojo/beginner-web/tree/master/session1/08-links)
