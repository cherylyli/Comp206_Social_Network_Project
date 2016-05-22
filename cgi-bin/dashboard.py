#!/usr/bin/python

print "Content-Type:text/html\n\n"

import cgi

form_cgi = cgi.FieldStorage()
username = form_cgi.getvalue("username")

#username = "cheryl"
template = open('dashboard2.template', 'r').read()


#replace # with the username
pos = template.find('#')
template = template[:pos] + username + template[pos + 1:]
pos = template.find('#')
template = template[:pos] + username + template[pos + 1:]
pos = template.find('#')
template = template[:pos] + username + template[pos + 1:]
pos = template.find('#')
template = template[:pos] + username + template[pos + 1:]

#get all updates in db and store into a list all_updates_list
#get all friends in db and store into a list friends_list
all_updates = open('../../../../2012/mrouss223/public_html/status.txt', 'r').read()
friends = open('../../../../2012/mrouss223/public_html/friends.txt', 'r').read()
friends_list = friends.split('\n')
all_updates_list = all_updates.split('\n')

#store all friends of user and the username of said user into list unames
index = 0
while (index < len(friends_list)):
    line = friends_list[index]
    unames = line.split(' ')
    index = index + 1
    if (unames[0] == username):
        break

#find statuses of everyone in the unames array and place them in a list
pos = template.find('@')
first_output = template[:pos]
last_output = template[(pos + 1):]
i = 0
j = 0
list_update = []
while (i < 20 and j < len(all_updates_list)):
    one_line_of_update = all_updates_list[j]
    j = j + 1
    person = one_line_of_update.split(' ')[0]
    if (person in unames):
    	words = one_line_of_update.split(' ')
        a_update = ' '.join(words[1:])
        list_update.append(person)
        list_update.append(a_update)
    	i = i + 1

#If j == 0 here, there are no status updates to display - do something!

list_update.reverse()




print first_output

count = 0
while count < len(list_update):
	print '<div class="status"><span>' + list_update[count+1] + ' : </span> ' + list_update[count] + '</div>'
	count = count + 2

print last_output