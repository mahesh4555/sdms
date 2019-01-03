#!/usr/bin/python

#importing the 'cgi' module 
import cgi 
import MySQLdb
  
print("Content-type: text/html\r\n\r\n") 
print('''<html>
        <head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head>
	<body>''') 
print("<h1> Students Mark Details! </h1>") 
print("<p> Enter the reg no to fetch the student semester details </p>")
#using HTML input and forms method 

print("<div><form method='post' action='mark_display_table.py'>")
print("<p>Reg_no: <input type='text' name='reg_no' /></p>")
print("<p>Semester: <input type='text' name='sem_id' /></p>")
print("<input type='submit' value='Submit' />")

print("</form")
print("</body></html></div>")
