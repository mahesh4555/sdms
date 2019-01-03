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

print("""<div>	 <button  type="button" onclick="location.href='enroll_form.py'">Enrollment</button>
	<button  type="button" onclick="location.href='mark_entry_sem.py'">Marks Entry</button>
	<button  type="button" onclick="location.href='test6.py'">Marksheet Generation</button>
	<button  type="button" onclick="location.href='test4.py'">Report Generation</button> </div>""")

print("""<div>	 <button  type="button" onclick="location.href='student_list.py'">Students List</button>
	<button  type="button" onclick="location.href='login.py'">Back</button>
	<button  type="button" onclick="location.href='login.py'">Logout</button> </div>""")





print("</body></html>") 




