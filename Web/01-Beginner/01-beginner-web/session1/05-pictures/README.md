# Adding Pictures

This story would be a lot more interesting with pictures! Adding a picture to our story is simple, we just need to use the `<img>` tag and tell it where our image is.

The `<img>` tag has an attribute called `src` and this is the web address (also known as a Uniform Resource Locator, or URL) to where the image has been saved. In this example, the image has been saved and then mapped with a bitly URL, and we are using a fully qualified web address.  However, that is not the only way images can be referenced.  The image could just be a file name that the page can reach directly.  More information can be found at [HTML img tag](http://www.w3schools.com/tags/tag_img.asp).

Here is an example `<img>` tag:

```html
<img src="http://f.cl.ly/items/2f473l1d233S0S1k3J3d/dogs-playing.jpg">
```

Now we can add a couple of images to our story, as shown below:

```html
<html>
	<head>
		<title>A day at the dog park</title>
	</head>
	<body>
		<h1>A day at the dog park</h1>
		<p>Today I took the dogs to the park and we had a great time!</p>
		<img src="http://f.cl.ly/items/2f473l1d233S0S1k3J3d/dogs-playing.jpg">
		<p>After the dogs played with their friends we took a walk around the track together.</p>
		<img src="http://f.cl.ly/items/0o0T0V0g261C1R0I022z/walking-the-track.jpg">
	</body>
</html>
```

![Story with images](http://cl.ly/image/3w2d1C0P1N3I/content#.png)

-------------------------

**Next HTML Topic:** [Emphasizing Text](https://github.com/TriValleyCoderDojo/beginner-web/tree/master/session1/06-emphasis)
