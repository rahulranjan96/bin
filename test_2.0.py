#!/usr/bin/env python
import cgi

print "Content-type: text/html"
print 
print "<html>"
print "<head><title>Test 2.0</title></head>"
print "<body>"
form = cgi.FieldStorage()
if form.getvalue("firstname"):
    firstname = form.getvalue("firstname")
if form.getvalue("lastname"):
    lastname = form.getvalue("lastname")
print "<h1>Your name: " + firstname + " " + lastname + "</h1><br/>"
print "</body>"
print "</html>"
