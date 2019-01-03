#!/usr/bin/python

#importing the 'cgi' module 
import cgi 
import MySQLdb
  
print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
print("<h1> ENTER THE MARKS AND ATTENDANCE! </h1>") 
#using HTML input and forms method 

form = cgi.FieldStorage()
semester= form.getvalue('semester')

db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()
list=[]
s=[]
print(s)
try:
	sql="SELECT * FROM SEM_COURSE_DETAILS WHERE sem_id=%s" %(semester)
	print("<p>name:try</p>")
	cursor.execute(sql)
	print("<p>name:try</p>")	
	results=cursor.fetchall()
	print("<p>name:try</p>")
	
	for i in results:
		list.append(i[1])
		list.append(i[2])
		list.append(i[3])
		list.append(i[4])
		list.append(i[5])
		list.append(i[6])
	
	print(list)
	print("<p>name;ex</p>")
except:
	print("<p>hai exception</p>")
print(list)
db.close()
print("<p>name:2</p>")
print("<form method='post' action='temp2.py'>")
print("<p>name:2</p>")
j=0
print(list)
i=0
for j in list:
	s.append(j)

	







print("</body></html>")
