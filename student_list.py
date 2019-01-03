#!/usr/bin/python

import cgi 
import MySQLdb

db=MySQLdb.connect("localhost","mahe","Mahesh@96*","student_details")
cursor=db.cursor()

try:
	sql="SELECT * FROM GEN_INFO" 
	cursor.execute(sql)	
	details=cursor.fetchall()
	
	sql="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'GEN_INFO' ORDER BY ORDINAL_POSITION" 
	cursor.execute(sql)	
	fields=cursor.fetchall()	
except:
	print("<p>Failed to fetch</p>")



print('''Content-type: text/html\r\n\r\n
       <html>
       <head>
       <link rel="stylesheet" type="text/css" href="css_file.css">
       </head> 
       <body>
       <h1> Welcome to Students list  </h1> 
       <div>
       <table>
         <tr>''')
for i in fields:
    print("<th>%s</th>"%(i))
print("</tr>")

for i in details:
    print("<tr>")
    print("<td>%s</td>"%(i[0]))
    print("<td>%s</td>"%(i[1]))
    print("<td>%s</td>"%(i[2]))
    print("<td>%s</td>"%(i[3]))
    print("<td>%s</td>"%(i[4]))
    print("<td>%s</td>"%(i[5]))
    print("<td>%s</td>"%(i[6]))
    print("</tr>")

print('''</table>                                                                                                         
         </div>
         </body></html>''')


