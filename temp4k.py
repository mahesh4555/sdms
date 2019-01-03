#!/usr/bin/python

import cgi,cgitb
import MySQLdb

form=cgi.FieldStorage()
      

db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()
semester=0

print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
try:
	
	sql="SELECT * FROM ENTRY WHERE id=1"
	cursor.execute(sql)
	s=cursor.fetchall()
	for k in s:
		global semester
		semester=k[1]
	print "sem=",semester
except:
	print("<p>%s</p>")


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
	



list=[]
try:
	sql="SELECT * FROM SEM_COURSE_DETAILS WHERE sem_id=%s" % (semester) 
	cursor.execute(sql)	
	results=cursor.fetchall()
	print"<p> Semester %s marks entry </p>" % (semester)
        print("<p>========================================================================================================================</p>")
	for row in results:
		print "sem=h",semester
		list.append(row[1])
		list.append(row[2])
		list.append(row[3])
		list.append(row[4])
		list.append(row[5])
		list.append(row[6])
	print "sem"
	

	print(list)
except:
	print("<p>except form not visible</p>")


try:	
	print(list)
	print("<p>name</p>")
	sql="INSERT INTO SEM_MARKS (regno,course_id,marks,attendance) VALUES (%s,%s,%s,%s)"
	cursor.execute(sql,(reg_no,list[0],s1,at1))
	db.commit()
	print("<p>name12</p>")
	cursor.execute(sql,(reg_no,list[1],s2,at2))
	db.commit()
	print("<p>name13</p>")
	cursor.execute(sql,(reg_no,list[2],s3,at3))
	db.commit()
	cursor.execute(sql,(reg_no,list[3],s4,at4))
	db.commit()
	cursor.execute(sql,(reg_no,list[4],s5,at5))
	db.commit()
	cursor.execute(sql,(reg_no,list[5],s6,at6))
	db.commit()
	print("<p>name</p>")
	db.close()

except:
	print("<p>Insertion failed</p>")


print("</body></html>")












