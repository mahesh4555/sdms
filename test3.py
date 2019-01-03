#!/usr/bin/python
#working code-dont edit
#importing the 'cgi' module 
import cgi 
import MySQLdb
print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
#print("<h1> Enter the semester to enter the marks </h1>") 

#using HTML input and forms method 

form = cgi.FieldStorage()

#semester = form.getvalue("semester")

semester=1
print("<p>%s</p>" %(semester))
db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
#print("<p>hello</p>")
cursor=db.cursor()
#print("<p>hello1</p>")
list=[]
try:
# 	print("<p>name</p>")
	sql="SELECT * FROM SEM_COURSE_DETAILS WHERE sem_id=%s" % (semester) 
	cursor.execute(sql)	
	results=cursor.fetchall()
	print"<p> Semester %s marks entry </p>" % (semester)
        print("<p>========================================================================================================================</p>")
	print("<p>Reg no: <input type='text' name='reg_no' /></p>")
	
	for row in results:
		s1=row[1]
		a=s1
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
		print("<form method='post' action='test3.py'>")
		print("<p>%s: <input type='text' name='s1_m' /></p>" %(s1))
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
		print("</form")
		
#		print("<p>name2</p>")
	
	db.close()
#	print("<p>name3</p>")
	print(list)
except:
	print("<p>User_name</p>")

print("<p>Aps</p>")
print(list)
s1=list[0]
print("<p>%s<p>"%(s1))
s2=list[1]
s3=list[2]
s4=list[3]
s5=list[4]
s6=list[5]
print("VIEW")
print(list[0])
print(list[1])
print("<p>Aps</p>")

# Using the inbuilt methods 

print("<p>Hello </p>") 

try:
	
	print("<p>Hello </p>")
	if form.getvalue("reg_no"):
	
		reg_no = form.getvalue("reg_no") 
		print("<p>Reg_no is %s</p>" % (reg_no))
		s1 = form.getvalue("s1_m") 
		print("<p>User_name is %s</p>"% (s1))
		s2 = form.getvalue("s2_m") 
		print("<p>User_name is %s</p>"% (s2))
		s3 = form.getvalue("s3_m") 
		print("<p>User_name is %s</p>"% (s3))
		s4 = form.getvalue("s4_m") 
		print("<p>User_name is %s</p>"% (s4))
		s5 = form.getvalue("s5_m") 
		print("<p>User_name is %s</p>"% (s5))
		s6 = form.getvalue("s6_m") 
		print("<p>User_name is %s</p>"% (s6))
		print(list[0])
		at1 = form.getvalue("at1") 
		print("<p>User_name is %s</p>"% (at1))
		at2 = form.getvalue("at2") 
		print("<p>User_name is %s</p>"% (at2))
		at3 = form.getvalue("at3") 
		print("<p>User_name is %s</p>"% (at3))
		at4 = form.getvalue("at4") 
		print("<p>User_name is %s</p>"% (at4))
		at5 = form.getvalue("at5") 
		print("<p>User_name is %s</p>"% (at5))
		at6 = form.getvalue("at6") 
		print("<p>User_name is %s</p>"% (at6))	

except:
	print("<p>Wrong</p>")


db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
print("<p>hello</p>")


cursor=db.cursor()
print("<p>hello1</p>")
try:
	print("<p>name</p>")
	sql="INSERT INTO SEM_MARKS (regno,course_id,marks) VALUES (%s,%s,%s)"
	print("<p>name12</p>")
	cursor.execute(sql,(reg_no,list[0],s1))
	db.commit()
	cursor.execute(sql,(reg_no,list[1],s2))
	db.commit()
	print("<p>name13</p>")
	cursor.execute(sql,(reg_no,list[2],s3))
	db.commit()
	cursor.execute(sql,(reg_no,list[3],s4))
	db.commit()
	cursor.execute(sql,(reg_no,list[4],s5))
	db.commit()
	cursor.execute(sql,(reg_no,list[5],s6))
	db.commit()
	print("<p>name</p>")
	db.close()

except:
	print("<p>User</p>")






print("</body></html>")


