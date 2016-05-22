#!/usr/bin/python

import cgi
form_cgi = cgi.FieldStorage()
username = form_cgi.getvalue("username")
friend_name = form_cgi.getvalue("friend")
#username = 'mathieu'
#friend_name='KurtZouisnotawesome'
see_a_friend_template = open('../friendInfo.html', 'r')
template = see_a_friend_template.read()

#replace names
position = template.find('@')
output = "Content-Type:text/html\n\n" + template[:position] + friend_name + template[(position+1):]
position = output.find('@')
output = output[:position] + username + output[(position+1):]

#open user.txt and find the friend
#index of friend willbe in i
alluserinfo = open('./user.txt', 'r').read()
userlines = alluserinfo.split('\n')
i = userlines.index(friend_name)

firstname = userlines[i+2]
lastname = userlines[i+3]
job = userlines[i+4]
gender = userlines[i+5]


position = output.find('#')
output = output[:position] + '<h2>'+ firstname + " " + lastname +" (" + gender + ") - " + friend_name +'</h2>\n<h3>' + job + '</h3>'+output[(position+1):]


print output

