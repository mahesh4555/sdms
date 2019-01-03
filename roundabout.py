#!/usr/bin/python

import cgi,cgitb
import MySQLdb




#print("<p>%s</p>"%semester)
print('''Content-type: text/html\r\n\r\n 
         <html>
	<head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head>
         <body> 
	 print('<h1>DATA ENTERED SUCCESSFULLY</h1>')
         <p> Do you want to entry another ? </p>''')

print("""<div>	 <button  type="button" onclick="location.href='mark_entry_sem.py'">YES</button>
	<button  type="button" onclick="location.href='login.py'">NO</button> </div>""")

print("</body></html>")
