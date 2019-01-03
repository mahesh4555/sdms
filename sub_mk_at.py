#!/usr/bin/python

import cgi,cgitb
import MySQLdb

form=cgi.FieldStorage()
semester = form.getvalue("semester")


#print("<p>%s</p>"%semester)
print('''Content-type: text/html\r\n\r\n 
         <html>
	 <head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head> 
         <body> 
         <h1> Enter the semester to enter the marks </h1>''') 
      


db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()

list=[]
try:
	sql="UPDATE ENTRY SET sem=1 where id=1"
	cursor.execute(sql)
	
except:
	print("<p>except 1st dummy</p>")

try:
	sql="SELECT * FROM SEM_COURSE_DETAILS WHERE sem_id=%s" % (semester) 
	cursor.execute(sql)	
	results=cursor.fetchall()
	print"<p> Semester %s marks entry </p>" % (semester)
        print("<p>========================================================================================================================</p>")
	print("<div><form method='post' action='mark_entry.py'>")	
	print("<p>Reg no: <input type='text' name='reg_no' /></p>")
	
	for row in results:
		s1=row[1]
		s2=row[2]
		s3=row[3]
		s4=row[4]
		s5=row[5]
		s6=row[6]
		list.append(row[1])
		list.append(row[2])
		list.append(row[3])
		list.append(row[4])
		list.append(row[5])
		list.append(row[6])
		
		print("<p>%s: <input type='text' name='s1_m' /></p>" %(row[1]))
		print("<p>%s: <input type='text' name='s2_m' /></p>" %(row[2]))
		print("<p>%s: <input type='text' name='s3_m' /></p>" %(row[3]))
		print("<p>%s: <input type='text' name='s4_m' /></p>" %(row[4]))
		print("<p>%s: <input type='text' name='s5_m' /></p>" %(row[5]))
		print("<p>%s: <input type='text' name='s6_m' /></p>" %(row[6]))
		print("<p>Attendance1: <input type='text' name='at1' /></p>") 
		print("<p>Attendance2: <input type='text' name='at2' /></p>")
		print("<p>Attendance3: <input type='text' name='at3' /></p>") 
		print("<p>Attendance4: <input type='text' name='at4' /></p>")
		print("<p>Attendance5: <input type='text' name='at5' /></p>") 
		print("<p>Attendance6: <input type='text' name='at6' /></p>")
		print("<input type='submit' value='Ok' />")    
		print("</form></div>")
	
	db.close()
	
	print(list)
except:
	print("<p>except form not visible</p>")

print("</body></html>")


