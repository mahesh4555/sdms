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



print("""<div>	<button  type="button" onclick="location.href='login111.py'">Back</button>
		<button  type="button" onclick="location.href='login.py'">Logout</button> </div>""")

#<p>Regno: <input type='text' name='reg_no'/></p>
print('''<h1> Enter the student details </h1>
	<div><form method='post' action='hello3.py'>
	<p>Name: <input type='text' name='name' /></p>
	<label for="name">Department:</label>
         <select id="dept" name="dept">
         <option value="AERO" > AERO </option>
	 <option value="AERO" > ECE </option>
	</select><br>
	<p>Mobile: <input type='text' name='mobile_no' /></p> 
	<p>Email: <input type='email' name='email' /></p> 
	<label for="batch">Batch:</label>
         <select id="batch" name="batch">
         <option value="2016" > 2016 </option>
	 <option value="2017" > 2017 </option>
	 <option value="2018" > 2018 </option>
	</select><br>
	<label for="semester">Semester:</label>
         <select id="semester" name="semester">
         <option value="1" > 1 </option>
	 <option value="2" > 2 </option>
	 <option value="3" > 3 </option>
	</select><br>
	<input type='submit' value='Submit' />
	</form></div>
	</body></html>''')

reg_no=101


form = cgi.FieldStorage() 
try:
	if form.getvalue("name"): 

		name = form.getvalue("name") 
#		print("<p>User_name is %s</p>"% (name))
		dept = form.getvalue("dept") 
#		print("<p>User_name is %s</p>"% (dept))
		mobile_no = form.getvalue("mobile_no") 
#		print("<p>User_name is %s</p>"% (mobile_no))
		email = form.getvalue("email") 
#		print("<p>User_name is %s</p>"% (email))
		batch = form.getvalue("batch") 
#		print("<p>User_name is %s</p>"% (batch))
		semester = form.getvalue("semester") 
#		print("<p>User_name is %s</p>"% (semester))
except:
	print("<p>Entry derror</p>")

db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()

try:
	sql="select regno from GEN_INFO "
	cursor.execute(sql)
	results=cursor.fetchall()
	for i in results:
		global reg_no
		reg_no+=1	
#	print("<p>regno=%s<p> %(regno)")

except:
	print("<p>Fetch error</p>") 

try:
	sql="INSERT INTO GEN_INFO (regno,name,dept,mob,email,batch,semester) VALUES (%s,%s,%s, %s,%s,%s,%s)"
	cursor.execute(sql,(reg_no,name,dept,mobile_no,email,batch,semester))
	db.commit()
	db.close()

	

except:
        print("<p>Failed </p>")  
    

