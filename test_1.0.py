#!/usr/bin/env python
import cgi

print "Content-type: text/html"
print 
print "<html>"
print "<head><title>Test 1.0</title></head>"
print "<body>"
print "<p>SearchEngine Frontend Test</p>"
print '<form method="post" action="test_2.0.py">'
print '<p>First Name:<input type="text" name="firstname"/></p>'
print '<p>Last Name:<input type="text" name="lastname"/></p>'
print '<input type="submit" value="Submit"/>'
print "</form>"
print "</body>"
print "</html>"
