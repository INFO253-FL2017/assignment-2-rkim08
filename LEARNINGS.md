1. What is the function of the following technologies in your assignment:
	HTML:
		HTML contains the code that displays the structure/layout of the website in the way that we intend for it to be. 
	CSS:
		CSS beautifies the website, meaning it decorates the elements of the HTML so that the website looks stylish. 
	JavaScript:
		JavaScript implements the validations/forms. 
	Python:
		Python is the language that is used as a back end program for this assignment. 
	Flask:
		Flask is a type of framework that was used to run the web in the local server.
	HTTP:
		HTTP is the connection that exists between the server and the web. Information is sent back and forth between the two. 
	GET and POST requests:
		GET usually gets/requests information from the server while the POST usually gets information and sends/posts it the server. 
		POST request was mainly used to power the MAILGUN portion of this assignment. 

2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?
HTML provides the structure, CSS decorates it, and JavaScript powers up the program (meaning that the users provide data by inputting into the form)

3. How does Python and Flask work together in the server for this assignment?
Python is used to power the server through the code and for this assignment, Flask is programmed in python. 


4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
GET:/
	renders the index.html template file. 
GET: /index
	renders the index.html template file
GET: /contact
	renders the contact.html template file
GET: /about
	renders the about.html template file
GET: /blog/(blogname)
	renders the blogname in blog folder within the template folder
POST: /contact
	submits information that was inputted to an the MAILGUN api which sends an email to the mainuser (aka the creator) and this will also render the contact.html template file
