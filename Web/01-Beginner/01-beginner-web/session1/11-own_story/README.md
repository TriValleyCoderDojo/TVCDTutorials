# Create Your Own Story

Congratulations!  You now know enough about HTML code to be able to create your own story.  How about you go ahead and create a story of your own.  You will want this to be something that interests you, and you would like to share with other people across the Internet.  Give it a moment to think about something really good!  

Feel free to refer back to the previous steps if you don't remember exactly how to do something.  You should be able to use a lot of what we learned with the dog story for you own story.  

## Create At Least One Page

You will want to create at least one page for your story.  However, you are not be limited to a single page.  You can create as many pages as you would like.  All you would need to do is use hyperlinks (the anchor tag) to link multiple pages together.  However, the only thing to think about is that you create navigational links to be able to move around from page to page.  It is not considered a good practice to rely upon the browser Back button.  

## Including Custom Images

Naturally, you are going to want to include your own images.  The images provided in the dog story are great for the dog story, but they probably won't work for your story.  So you are going to need to upload your images and make them available across the Internet, so you can use them in the img tag.  

Actually, Dropbox makes that really easy.  Once Dropbox has been installed on your computer, it will do most of the work for you.  It will take care of uploading the files, and it will create URLs for you.  All you really need to do is to put the image files in the directory created by Dropbox.  But it gets even better because you don't even need to remember where that directory is, just let Dropbox tell you.  

Start by clicking on the Dropbox icon in your tool bar.

![Dropbox Toolbar](https://raw.githubusercontent.com/TriValleyCoderDojo/beginner-web/master/screenshots/dropbox_1.PNG)

After clicking on the Dropbox icon, a new window will popup.  In this window, click on the "Dropbox Folder" link at the bottom.  Then a new file browser window will appear.  This is the magic Dropbox window that takes care of everything for you.  All you need to do is copy your image files into here, using the regular drag-n-drop way.  When you first drop the files in they will get a little blue circle, and eventually that will change into a white check mark in a green circle, which tells you it is ready to use.  

The next thing you are going to need is the public URL to your image file.  Naturally, Dropbox will also give that to you.  All you need to do is to select the file in the Dropbox window and right mouse click on it.  A new menu will appear, and you want to select "Share Dropbox link".  This will actually add the public URL into your copy buffer, and you can go back to your HTML code and paste it in directly.  

![Dropbox Toolbar](https://raw.githubusercontent.com/TriValleyCoderDojo/beginner-web/master/screenshots/dropbox_2.jpg)

**Important Note:** If you are installing Dropbox for the first time and are using the new verion of Dropbox, then you may need to slightly change the URL to make your images render correctly.  The newer versions of Dropbox have a bug where they don't set the MIME content type correctly, depending upon the URL being used.  Sometimes the default public URL will not work and you need to change it.  You might need to change the www.dropbox.com to dl.dropbox.com.  

For example, the following URL might not work from in your HTML:
    
    http://www.dropbox.com/s/4ry0n27gk299vrs/a-Sunset-wave.jpg 
    
but this other URL will work just fine:

    http://dl.dropbox.com/s/4ry0n27gk299vrs/a-Sunset-wave.jpg   

The only difference is the dl.  This can be a particularly frustrating thing to figure out, because it will work just fine in a browser, but not in the HTML.  


--------

**Next Session:** [Introduction to CSS](https://github.com/TriValleyCoderDojo/beginner-web/tree/master/session2)
