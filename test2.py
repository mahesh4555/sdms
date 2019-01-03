#!/usr/bin/env python
import cgi 
import MySQLdb
  
  
print("Content-type: text/html\r\n\r\n") 
print('''<html>
        <head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head>
        <body>
	<h1> Student Database </h1>''') 
# Using the inbuilt methods 
  
form = cgi.FieldStorage() 
name = form.getvalue("name") 
password = form.getvalue("password")
#print"<p> %s %s </p>" %(name,password)
	

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
#print "<p> %s %s </p>" % (name,x)

  

if name == x and password == y:
 	
	print("""<div>	 <button  type="button" onclick="location.href='hello3.py'">Enrollment</button>
		<button  type="button" onclick="location.href='test4.py'">Marks Entry</button>
		<button  type="button" onclick="location.href='test6.py'">Marksheet Generation</button>
		<button  type="button" onclick="location.href='test4.py'">Report Generation</button> </div>""")

 
print("</body></html>") 

