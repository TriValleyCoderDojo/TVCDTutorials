This is a very simple Python Web Application.  It uses pure Python.
It does not use any frameworks, such as Django, Flask, etc...
The intention is to provide a very simple introduction to a 
Web Application for younger kids without adding a bunch of 
complexities.  Just provide a starting place to describe the 
request and response of HTTP, and show how that translates 
on the client(browser) and server side.  

The structure of the app is very simple.  There is a landing page,
index.html.  That branches off to two pages.  The first branch 
is to an input form page, form1.html, which accepts a name and 
an age.  The input is save to a text file to simulate a database.
The second branch is to a listing page which reads the text 
files and displays a list of the currently added users.  

To run the web app you will need to have Python 3.3.x or 
better.  You can get this from http://www.python.org/download/
then all you need to do is launch it with the command 

    python simpleWebApp.py

Next, in the browser you will be use it with the URI

    http://localhost:8000/index.html

