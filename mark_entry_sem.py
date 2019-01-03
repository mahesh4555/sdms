#!/usr/bin/python

#importing the 'cgi' module 
import cgi 
  
print("Content-type: text/html\r\n\r\n") 
print('''<html>
	<head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head>
	<body>''') 

print("""<div>	<button  type="button" onclick="location.href='login_next_min.py'">Back</button>
		<button  type="button" onclick="location.href='login.py'">Logout</button> </div>""")

print("<h1> Enter the semester to enter the marks </h1>") 
#using HTML input and forms method 
print("<div><form method='post' action='mark_entry_regno.py'>")

print("<p>Semester: <input type='number' name='semester' min='1' max='8' /></p> ")

print("<input type='submit' value='Ok' />")

#semester = form.getvalue("semester")
print("</form></div>")
print("</body></html>")






