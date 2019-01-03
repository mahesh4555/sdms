#!/usr/bin/env python
import cgi 
import MySQLdb
  
  
print("Content-type: text/html\r\n\r\n") 
print('''<html>
         <head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head> 
         <body> 
	<h1> WeLcOmE tO mAdRaS iNsTItUtE oF tEcHnOlOgY! </h1>          
	<p> Login Credentials! </p> ''')
# Using the inbuilt methods 
  
'''form = cgi.FieldStorage() 
if form.getvalue("name"): 
    name = form.getvalue("name") 
    password = form.getvalue("password")'''
  
# Using HTML input and forms method 
print("<div><form method='post' action='test2.py'>") 
print("<p>Name: <input type='text' name='name' /></p>") 
print("<p>Password: <input type='text' name='password' /></p>") 
#print("<input type='checkbox' name='happy' /> Happy") 
#print("<input type='checkbox' name='sad' /> Sad") 
print("<input type='submit' value='Login' />") 
print("</form></div>") 

regno = form.getvalue("reg") 
print("<p> %s</p>" %(reg)) 
print("</body></html>") 

