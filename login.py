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


print('''<div><form method='post' action='login_next.py'> 
	<p>User ID: <input type='text' name='name' /></p> 
	<p>Password: <input type='password' name='password' /></p>  
	<input type='submit' value='Login' /> 
	</form></div>''') 




print("</body></html>") 




