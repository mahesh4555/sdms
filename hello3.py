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
print("<h1> Enter the student details </h1>") 
#using HTML input and forms method 
print("<div><form method='post' action='hello3.py'>")
print("<p>Reg_no: <input type='text' name='reg_no' /></p>")
print("<p>Name: <input type='text' name='name' /></p>")
print("<p>Department: <input type='text' name='dept' /></p> ")
print("<p>Mobile_no: <input type='text' name='mobile_no' /></p> ")
print("<p>Email: <input type='text' name='email' /></p> ")
print("<p>Batch: <input type='text' name='batch' /></p> ")
print("<p>Semester: <input type='text' name='semester' /></p> ")
print("<input type='submit' value='Submit' />")
print("</form></div>")
print("</body></html>")

# Using the inbuilt methods 
form = cgi.FieldStorage() 
if form.getvalue("name"): 
    reg_no = form.getvalue("reg_no") 
    print("<p>User_name is %s</p>"% (reg_no))
    name = form.getvalue("name") 
    print("<p>User_name is %s</p>"% (name))
    dept = form.getvalue("dept") 
    print("<p>User_name is %s</p>"% (dept))
    mobile_no = form.getvalue("mobile_no") 
    print("<p>User_name is %s</p>"% (mobile_no))
    email = form.getvalue("email") 
    print("<p>User_name is %s</p>"% (email))
    batch = form.getvalue("batch") 
    print("<p>User_name is %s</p>"% (batch))
    semester = form.getvalue("semester") 
    print("<p>User_name is %s</p>"% (semester))
#   mydb = mysql.connector.connect(host="localhost", user="root", passwd="mieupro", database="student")
#   mycursor = mydb.cursor()
#   mycursor.execute( "SELECT User_name from Login_details")

    db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
    cursor=db.cursor()
    try:
	sql="INSERT INTO GEN_INFO (regno,name,dept,mob,email,batch,semester) VALUES (%s,%s,%s, %s,%s,%s,%s)"
	cursor.execute(sql,(reg_no,name,dept,mobile_no,email,batch,semester))
	db.commit()
	db.close()

	


	redirectURL = "http://localhost/cgi-enabled/roundabout1.py"

	print('<html>')

	print('  <head>')
	print('<p>DATA ENTERED SUCCESSFULLY</p>')

	print('    <meta http-equiv="refresh" content="0;url=' + str(redirectURL) + '" />')

	print('  </head>')

	print('</html>')

	print("</body></html>")




    except:
        print("<p>User_name</p>")
    

