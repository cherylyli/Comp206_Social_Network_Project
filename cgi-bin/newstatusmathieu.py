#!/usr/bin/python
###################NOTE TO MATHIEU####################
#we need to check for empty status or status that only have blank spaces inside
#basically, we can parse it with " " and if the len(list)== 0 then we don't do anything
#######################################################

import cgi


form = cgi.FieldStorage()
username = form.getvalue("username")
status = form.getvalue("status")
#username = 'mathieu'
#status = "boooo"

statuses = open('/home/2012/mrouss223/public_html/status.txt', 'a')
#status2 = status.replace('+', ' ')
statuses.write(username + ' ' + status + '\n')

template = open('/home/2015/yli205/public_html/statusSubmitted.html', 'r').read()

pos = template.find('@')
template = template[:pos] + username + template[pos + 1:]
pos = template.find('@')
output = template[:pos] + username + template[pos + 1:]
output = "Content-Type:text/html\n\n" + output
print output
