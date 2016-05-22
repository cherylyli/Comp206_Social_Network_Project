#!/usr/bin/python


import cgi
form = cgi.FieldStorage()
username = form.getvalue("username")
#username = "Cheryl234"

make_friend_template = open('../makefriends.template', 'r')
template = make_friend_template.read()

#replace the value in the hidden field with username
position = template.find('#')
output = "Content-Type:text/html\n\n" + template[:position] + username + template[(position + 1):]

#get the database of all users in the database and parse into user_list
users_listing = open('../../../../2016/jliu164/public_html/cgi-bin/user.txt', 'r').read()
userlist = users_listing.split('\n')

#while we haven't gotten to the end of friends_list, put all first_name, last_name, and username in a list
i = 0
toBePrinted = []

while (i <= len(userlist)):
	if (i+1 >=len(userlist)):
		break
	else:
		toBePrinted.append(userlist[i])
		i += 6

#print stuff before the %
position = output.find('%')
print output[:position]
position += 1


#print the names from names_list into the 
i = 0
while ( i <= len(toBePrinted)):
	if (i+1 > len(toBePrinted)):
		break
	else:
		print toBePrinted[i] + '<input type="checkbox" value="' + toBePrinted[i] + '" name="user"></input><br>'
		i += 1
print output [(position + 2 ):]


#print new_line\
# output = output[:position] + friends_list[first_name] + friends_list[last_name] + ' - ' + friends_list[username] + output[(position + 1):]
# position = output.find('%')
# print output
