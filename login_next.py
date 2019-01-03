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
a=0
try:
	cursor.execute(sql)
	results=cursor.fetchall()
	for row in results:	

		if name == row[0] and password == row[1]:
			x=row[0]
			y=row[1]
			global a
			a=1
			print"<p>Access granted</p>"
			break;	

except:
	print"<p>ERROR:Unable to fetch</p>"
db.close()
#print "<p> %s %s </p>" % (name,x)

  

if a==1:
 	
	print("""<div>	 <button  type="button" onclick="location.href='enroll_form.py'">Enrollment</button>
		<button  type="button" onclick="location.href='mark_entry_sem.py'">Marks Entry</button>
		<button  type="button" onclick="location.href='test6.py'">Marksheet Generation</button>
		<button  type="button" onclick="location.href='test4.py'">Report Generation</button> </div>""")

	print("""<div>	 <button  type="button" onclick="location.href='student_list.py'">Students List</button>
		<button  type="button" onclick="location.href='login.py'">Back</button>
		<button  type="button" onclick="location.href='login.py'">Logout</button> </div>""")
else:
	print("""<div>	<p>Access denied</p>
			<p>Invalid user_id or password</p>
	 		<p>click here to login again</p>
			<button  type="button" onclick="location.href='login.py'">Back to Login</button> </div>""")



print("</body></html>") 

