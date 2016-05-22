#!/usr/bin/python

import cgi
form = cgi.FieldStorage()
username = form.getvalue("username")
#username = 'curtis'
#selected_users is a list with everything that's selected
#selected_users = ['username']
selected_users = form.getlist("user")


#open friends.txt file
friendsfile = open('/home/2012/mrouss223/public_html/friends.txt', 'r')
#split the lines in a list
friendsfile_list = friendsfile.read().split('\n')
#close the file (we have the list)
friendsfile.close()
#Loop through the lines
i = 0
for friendsfile_line in friendsfile_list:
	#Split the lines into the different names
	friends = friendsfile_line.split(' ')
	#If the first names is the username...
	if (friends[0] == username):
		#Loop through the selected users
		for user in selected_users:
			#if the selected user is not in the list
			if not user in friends:
				#Add it to the list
				friends = friends + [user]
        #After adding the new friends, join back the line
		friendsfile_line = ' '.join(friends)
		friendsfile_list[i] = friendsfile_line
		break
	i = i + 1

#Open friends.txt again, for writing
friendsfile_write = open('/home/2012/mrouss223/public_html/friends.txt', 'w')
#Write the new file
friendsfile_write.write('\n'.join(friendsfile_list))
#Close friends.txt
friendsfile_write.close()


madeFriends_template = open('/home/2015/yli205/public_html/friendshipMade.html', 'r').read()
madeFriends_template = "Content-Type:text/html\n\n" + madeFriends_template

position = madeFriends_template.find('@')
madeFriends_template = madeFriends_template[:position] + username + madeFriends_template[(position+1):]


print madeFriends_template


