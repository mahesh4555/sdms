#!/usr/bin/python

#importing the 'cgi' module 
import cgi 
import MySQLdb

print('''Content-type: text/html\r\n\r\n 
	<html>
	<head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head>
	<body>''') 

print("""<div>	<button  type="button" onclick="location.href='mark_entry_sem.py'">Back</button>
		<button  type="button" onclick="location.href='login.py'">Logout</button> </div>""")

form=cgi.FieldStorage()
semester=form.getvalue('semester')

print("<h1>SEMESTER : %s</h1>" %(semester) )
print("<div><form method='post' action='sub_mk_at.py'>") 


db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()



print("<h1> Select the reg_no to enter the marks </h1>")
try:
	sql="UPDATE ENTRY SET sem=%s where id=1" %(semester)
	cursor.execute(sql)
	db.commit()

except:
	print("<p>except 1st dummy</p>")




try:
	sql="SELECT regno FROM GEN_INFO WHERE semester=%s" % (semester) 
	cursor.execute(sql)	
	res=cursor.fetchall()

	print('''<label for="name">Reg_no</label>
	<select id="reg_no" name="reg_no">''')
	for i in res:	
		print('<option value="%s" > %s </option>'%(i[0],i[0]))	
	print('''</select><br>
	<input type='submit' value='Login' /> 
	</form></div>''') 

 



except:
	print("sdfvs")
	
