#!/usr/bin/python

import cgi 
import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", passwd="mieupro", database="student")
mycursor = mydb.cursor(dictionary=True)

mycursor.execute("SELECT User_name FROM Login_details ")
User_name = mycursor.fetchall()

print('''Content-type: text/html\r\n\r\n 
      <html>
      <head>
      <link rel='stylesheet' type='text/css' href='css_file.css'>
      </head>
      <body>
      <h1> welcome to madras institute of technogy </h1>
      <div>
      <form method='post' action='hello2.py'> 
          <label for="name">User Name</label><br>
          <select id="name" name="name">''')

for i in User_name:
    print('<option value="%s" > %s </option>'%(i['User_name'],i['User_name']))

print('''</select><br>
          <label for="password">Password</label><br>
          <input type="password" id="password" name="password" placeholder="Enter Password" required>
          <br>
          <input type="submit" value="LOGIN">
      </form>
      </div>
      </body></html>''') 

