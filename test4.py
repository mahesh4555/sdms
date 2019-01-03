#!/usr/bin/python

#importing the 'cgi' module 
import cgi 
  
print("Content-type: text/html\r\n\r\n") 
print('''<html>
	<head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head>
	<body>''') 
print("<h1> Enter the semester to enter the marks </h1>") 
#using HTML input and forms method 
print("<div><form method='post' action='sub_mk_at.py'>")

print("<p>Semester: <input type='text' name='semester' /></p> ")

print("<input type='submit' value='Ok' />")

#semester = form.getvalue("semester")
print("</form></div>")
print("</body></html>")






