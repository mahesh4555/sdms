#!/usr/bin/python

#importing the 'cgi' module 
import cgi 
import MySQLdb
 
#using HTML input and forms method 
print("<form method='post' action='temp2.py'>")

form = cgi.FieldStorage() 
semester = form.getvalue("semester") 

print"<p> Semester %s marks entry </p>" % (semester)


print("<form method='post' action='test3.py'>")
		print("<p>%s: <input type='text' name='s1_m' /></p>" %(s1))
		print("<p>%s</p>") %(s1)
		print("<p>%s: <input type='text' name='s2_m' /></p>" %(row[2]))
		print("<p>%s: <input type='text' name='s3_m' /></p>" %(row[3]))
		print("<p>%s: <input type='text' name='s4_m' /></p>" %(row[4]))
		print("<p>%s: <input type='text' name='s5_m' /></p>" %(row[5]))
		print("<p>%s: <input type='text' name='s6_m' /></p>" %(row[6]))
		print("<p>Attendance1: <input type='text' name='at1' /></p>") 
		print("<p>Attendance2: <input type='text' name='at2' /></p>")
		print("<p>Attendance1: <input type='text' name='at3' /></p>") 
		print("<p>Attendance2: <input type='text' name='at4' /></p>")
		print("<p>Attendance1: <input type='text' name='at5' /></p>") 
		print("<p>Attendance2: <input type='text' name='at6' /></p>")
		print("<input type='submit' value='Ok' />")    
		print("</form")



print("<p>Reg no: <input type='text' name='reg_no' /></p>")
print("<p>================================================================================================================================</p>")
print("<p>Communication Networks: <input type='text' name='s1' /></p>")
print("<p>Wireless Communication: <input type='text' name='s2' /></p>")
print("<p>Wireless Networks: <input type='text' name='s3' /></p> ")
print("<p>Digital Electronics: <input type='text' name='s4' /></p> ")
print("<p>Electonic circuits: <input type='text' name='s5' /></p> ")
print("<p>Avionics: <input type='text' name='s6' /></p> ")
print("<input type='submit' value='Ok' />")

print("</form")
print("</body></html>")


# Using the inbuilt methods 
if form.getvalue("reg_no"): 
    reg_no = form.getvalue("reg_no") 
    print("<p>Reg_no is %s</p>"% (reg_no))
    s1 = form.getvalue("s1") 
    print("<p>User_name is %s</p>"% (s1))
    s2 = form.getvalue("s2") 
    print("<p>User_name is %s</p>"% (s2))
    s3 = form.getvalue("s3") 
    print("<p>User_name is %s</p>"% (s3))
    s4 = form.getvalue("s4") 
    print("<p>User_name is %s</p>"% (s4))
    s5 = form.getvalue("s5") 
    print("<p>User_name is %s</p>"% (s5))
    s6 = form.getvalue("s6") 
    print("<p>User_name is %s</p>"% (s6))
 
#   mydb = mysql.connector.connect(host="localhost", user="root", passwd="mieupro", database="student")
#   mycursor = mydb.cursor()
#   mycursor.execute( "SELECT User_name from Login_details")



    db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
    print("<p>hello</p>")
    
    print("<p>he</p>")
    cursor=db.cursor()
    print("<p>hello1</p>")
    try:
 	print("<p>name</p>")
	sql="INSERT INTO SEM_DETAILS (regno,s1,s2,s3,s4,s5,s6) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	print("<p>name12</p>")
	cursor.execute(sql,(reg_no,s1,s2,s3,s4,s5,s6))	
        print("<p>name2</p>")
	db.commit()
	db.close()

    except:
        print("<p>User_name</p>")







