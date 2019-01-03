#!/usr/bin/python

import cgi,cgitb
import MySQLdb




print('''Content-type: text/html\r\n\r\n 
         <html>
	 <head>
         <link rel="stylesheet" type="text/css" href="css_file.css">
         </head>
         <body> 
	  <p> Data entered successfully </p>
         <p> Do you want to entry another ? </p>''')

print("""<div>	 <button  type="button" onclick="location.href='enroll_form.py'">YES</button>
	<button  type="button" onclick="location.href='login_next_min.py'">NO</button> </div>""")

print("</body></html>")

