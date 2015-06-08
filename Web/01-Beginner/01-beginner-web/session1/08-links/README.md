# Hyperlinks

One of the things that makes web pages so amazing for telling stories is you can **link** things together with other web pages on the internet and it is really easy to do!

In the previous example I included three kinds of dogs that we saw at the park, now I'm going to use hyperlinks (the `<a>` tag) to link the dog names to their descriptions on Wikipedia.

The anchor (`<a>`) tag has an attribute called `href` and we will set that attribute equal to the url of the web page we want to link to. Here is an example where I link the word Poodles to the web page about Poodles on Wikipedia:

```
<a href="http://en.wikipedia.org/wiki/Poodle">Poodles</a>
```

Here is what it looks like in the context of our story:

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
			<li><a href="http://en.wikipedia.org/wiki/Poodle">Poodles</a></li>
			<li><a href="http://en.wikipedia.org/wiki/Great_Dane">Great Danes</a></li>
			<li><a href="http://en.wikipedia.org/wiki/Labrador_Retriever">Black Labs</a></li>
		</li>
	</body>
</html>
```

This is the simplest and most common use of the anchor tag, but there are many others.  For example the href could point to a named element on the same page.  Another example is to make the linked page open in a new window by adding target="_blank".  For more information on the anchor tag, refer to [HTML anchors](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a). 

--------

**Next HTML Topic:** [Saving the URL](https://github.com/TriValleyCoderDojo/beginner-web/tree/master/session1/09-save_url)
