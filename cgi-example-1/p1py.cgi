#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

#Get data from fields
fname = form.getvalue('first_name')
lname = form.getvalue('last_name')

# Print out info
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title> First CGI Program </title>"
print "</head>"
print "<body>"
print "<h2> Hello %s %s </h2>" % (fname, lname)
print "</body>"
print "</html>"
