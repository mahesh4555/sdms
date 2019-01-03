#!/usr/bin/python

import cgi,cgitb
import MySQLdb

form=cgi.FieldStorage()
      

db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()
semester=0

print("Content-type: text/html\r\n\r\n") 
print('''<html>
	 <head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head> 
	<body>''') 
try:
	
	sql="SELECT * FROM ENTRY WHERE id=1"
	cursor.execute(sql)
	s=cursor.fetchall()
	for k in s:
		global semester
		semester=k[1]
#	print "sem=",semester
except:
	print("<p>%s</p>")


if form.getvalue("reg_no"):
	reg_no = form.getvalue("reg_no")
#	print("<p>Reg_no is %s</p>" % (reg_no))
	s1 = form.getvalue("s1_m") 
#	print("<p>User_name is %s</p>"% (s1))
	s2 = form.getvalue("s2_m") 
#	print("<p>User_name is %s</p>"% (s2))
	s3 = form.getvalue("s3_m") 
#	print("<p>User_name is %s</p>"% (s3))
	s4 = form.getvalue("s4_m") 
#	print("<p>User_name is %s</p>"% (s4))
	s5 = form.getvalue("s5_m") 
#	print("<p>User_name is %s</p>"% (s5))
	s6 = form.getvalue("s6_m") 
#	print("<p>User_name is %s</p>"% (s6))
	at1 = form.getvalue("at1") 
#	print("<p>User_name is %s</p>"% (at1))
	at2 = form.getvalue("at2") 
#	print("<p>User_name is %s</p>"% (at2))
	at3 = form.getvalue("at3") 
#	print("<p>User_name is %s</p>"% (at3))
	at4 = form.getvalue("at4") 
#	print("<p>User_name is %s</p>"% (at4))
	at5 = form.getvalue("at5") 
#	print("<p>User_name is %s</p>"% (at5))
	at6 = form.getvalue("at6") 
#	print("<p>User_name is %s</p>"% (at6))	
res=[]

'''s1=int(s1)
s2=int(s2)
s3=int(s3)
s4=int(s4)
s5=int(s5)
s6=int(s6)'''
reg_no=115
s1=90
s2=99
s3=89
s4=78
s5=65
s6=85
dict={}
marks=[s1,s2,s3,s4,s5]

clear=0
tot_marks=0
for i in marks:
	tot_marks+=i
	if i >=50:
		res.append('P')
		clear+=1

	else:
		res.append('F')



print(res)

"""if s1 >=50:
	res.append('P')
	clear+=1
else:
	res.append('F')

if s2 >=50:
	res.append('P')
	clear+=1
else:
	res.append('F')

if s3 >=50:
	res.append('P')
	clear+=1
else:
	res.append('F')

if s4 >=50:
	res.append('P')
	clear+=1
else:
	res.append('F')

if s5 >=50:
	res.append('P')
	clear+=1
else:
	res.append('F')

if s6 >=50:
	res.append('P')
	clear+=1
else:
	res.append('F') """


if clear==6:
	all_clear=1
else:
	all_clear=0


avg=(tot_marks/6)
gpa=(avg/10)
print(avg)
print(gpa)





list=[]
try:
	sql="SELECT * FROM SEM_COURSE_DETAILS WHERE sem_id=%s" % (semester) 
	cursor.execute(sql)	
	results=cursor.fetchall()
#	print"<p> Semester %s marks entry </p>" % (semester)
#       print("<p>========================================================================================================================</p>")
	for row in results:
#		print "sem=h",semester
		list.append(row[1])
		list.append(row[2])
		list.append(row[3])
		list.append(row[4])
		list.append(row[5])
		list.append(row[6])
	print "sem"
	

#	print(list)
except:
	print("<p>except form not visible</p>")

print(res)
try:	
#	print(list)
#	print("<p>name</p>")
	sql="INSERT INTO SEM_MARKS (regno,sem_id,course_id,marks,attendance,result) VALUES (%s,%s,%s,%s,%s,%s)"
	cursor.execute(sql,(reg_no,semester,list[0],s1,at1,res[0]))
	db.commit()
#	print("<p>name12</p>")
	cursor.execute(sql,(reg_no,semester,list[1],s2,at2,res[1]))
	db.commit()
#	print("<p>name13</p>")
	cursor.execute(sql,(reg_no,semester,list[2],s3,at3,res[2]))
	db.commit()
	cursor.execute(sql,(reg_no,semester,list[3],s4,at4,res[3]))
	db.commit()
	cursor.execute(sql,(reg_no,semester,list[4],s5,at5,res[4]))
	db.commit()
	cursor.execute(sql,(reg_no,semester,list[5],s6,at6,res[5]))
	db.commit()
#	print("<p>name</p>")
	db.close()

except:
	print("<p>Insertion failed</p>") 

try:	
	sql="INSERT INTO SEM_RESULTS (regno,sem_id,gpa,all_clear) VALUES (%s,%s,%s,%s)"
	cursor.execute(sql,(reg_no,semester,gpa,all_clear))
	db.commit()
	db.close()
except:
	print("<p>Insertion failed for gpa</p>") 


'''print('Content-type:text/html\n')


redirectURL = "http://localhost/cgi-enabled/roundabout.py"

print('<html>')

print('  <head>')
print('<p>DATA ENTERED SUCCESSFULLY</p>')

print('    <meta http-equiv="refresh" content="0;url=' + str(redirectURL) + '" />')

print('  </head>')

print('</html>')

print("</body></html>")'''












