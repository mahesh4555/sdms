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


print('''<div><form method='post' action='test2.py'> 
	<p>Name: <input type='text' name='name' /></p> 
	<p>Password: <input type='text' name='password' /></p>  
	<input type='submit' value='Login' /> 
	</form></div>''') 

form = cgi.FieldStorage() 

regno = form.getvalue("reg")
password = form.getvalue("password")


db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()
sql="SELECT * FROM login_creds"
try:
	cursor.execute(sql)
	results=cursor.fetchall()
	for row in results:	

		if name == row[0] and password == row[1]:
			x=row[0]
			y=row[1]
			print"<p>Access granted</p>"
			break;	

except:
	print"<p>ERROR:Unable to fetch</p>"
db.close()

print("<p> %s</p>" %(reg)) 
print("</body></html>") 




