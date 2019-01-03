#!/usr/bin/env python
import cgi 
import MySQLdb
  
  
print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
#print("<h1> Marksheet of studenr </h1>") 
# Using the inbuilt methods 
  
form = cgi.FieldStorage() 
reg_no = form.getvalue("reg_no") 
sem_id=form.getvalue("sem_id")
#print"<p> %s %s </p>" %(name,password)


db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()



try:
	sql="SELECT * FROM SEM_MARKS WHERE regno= %s and sem_id=%s" %(reg_no,sem_id) 
	cursor.execute(sql)	
	results=cursor.fetchall()
	
except:
	print("<p>Failed to fetch</p>")




print('''Content-type: text/html\r\n\r\n
       <html>
       <head>
       <link rel="stylesheet" type="text/css" href="css_file.css">
       </head> 
       <body>
       <h1> Welcome to Students list section </h1> 
       <div>
       <table>
         <tr>''')

print("<th>Subject</th>")
print("<th>Marks</th>")
print("<th>Results</th>")

print("</tr>")

for i in results:
    print("<tr>")
    print("<td>%s</td>"%(i[2]))
    print("<td>%s</td>"%(i[3]))
    print("<td>%s</td>"%(i[5]))
    print("</tr>")

print('''</table>                                                                                                         
         </div>
         </body></html>''')


