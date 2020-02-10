#!/usr/bin/python
import cgi, cgitb
import MySQLdb

webForm = cgi.FieldStorage()

username = webForm.getvalue('Username')
mypass = webForm.getvalue('MyPass')

db = MySQLdb.connect("localhost","YourUserName","YourMySQLpassword","YourUserName_db")

myCursor = db.cursor()

sql = "INSERT INTO UserPass VALUES ('%s','%s');" %(username,mypass)

try:
	myCursor.execute(sql)
	db.commit()
except:
	db.rollback()

db.close()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title> REGISTRATION FORM </title>"
print "</head>"
print "<body>"
print "<h2> Congratulations! You have successfully registered with username =
%s </h2>" %(username)
print "</body>"
print "</html>"
