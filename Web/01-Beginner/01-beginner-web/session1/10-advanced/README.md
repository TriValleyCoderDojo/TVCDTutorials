# Advanced Topics

## Telling More Than One Story

If you want to write another story you don't have to start a whole new web page, you can use the same page you have been working on and use HTML to indicate where one story stops and the next begins. Typically we will use `<article>` tags to accomplish this. Here is an example:

```html
<html>
  <head>
    <title>A day at the dog park</title>
  </head>
  <body>
    <h1>Dog Stories</h1>
    <article>
      <h2>A day at the dog park</h2>
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
    </article>
    <article>
      <h2>Driving Across The Country With Leo and Bailey</h2>
      <p>A year ago we drove across the country <em>with Leo and Bailey</em> when we moved from Indiana to California.</p>
      <img src="http://cl.ly/image/3G2Z3x0G3Z46/content#.png">
      <p>One time after stopping to eat lunch we found Leo in the front seat ready to drive. <strong>This made us laugh really hard :)</strong></p>
    </article>
  </body>
</html>
```

You will notice a few new things in the html above. We added a second story, we enclosed both stories in `<article>` tags, we changed the story titles to use `<h2>` (Heading 2) tags, and we changed the `<h1>` (Heading 1) at the top to say **Dog Stories**.


## Style

In the next session we will start learning how to add style to our story using html attributes and CSS. Here is an example to help get you excited about it.

In CodePen we want to check the box next to CSS and then paste the following css code into the CSS box:

```css
body {
  font-family: Arial;
  background-color: #eee;
  color: green;
}

img {
  border: 2px solid green;
  padding: 2px;
}
```

![Story with CSS](http://cl.ly/image/002B0l3l090P/content#.png)

--------

**Next HTML Topic:** [Create Your Own Story](https://github.com/TriValleyCoderDojo/beginner-web/tree/master/session1/11-own_story)


