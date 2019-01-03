#!/usr/bin/python

import cgi,cgitb
import MySQLdb




print('''Content-type: text/html\r\n\r\n 
         <html>
         <body> 
	  <h1> Data entered successfully </h1>
         <h1> Do you want to entry another ? </h1>''')

print("""<div>	 <button  type="button" onclick="location.href='hello3.py'">YES</button>
	<button  type="button" onclick="location.href='test1.py'">NO</button> </div>""")

print("</body></html>")

