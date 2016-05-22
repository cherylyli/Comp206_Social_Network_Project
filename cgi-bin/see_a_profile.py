#!/usr/bin/python

import cgi
form_cgi = cgi.FieldStorage()
username = form_cgi.getvalue("username")
friend_name = form_cgi.getvalue("friend")
see_a_friend_template = open('../friendInfo.html', 'r')
template = see_a_friend_template.read()

#replace names
position = template.find('@')
output = "Content-Type:text/html\n\n" + template[:position] + friend_name + template[(position+1):]

position = output.find('#')
output = output[:position] + username + output[(position + 1):]

print output
print friend_name
print username