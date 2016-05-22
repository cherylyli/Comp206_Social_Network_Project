Group Name: PandaHuggers
Team Members: Yuchen Li (McGill ID: 260497059), 
			  Mathieu Roussel-Lewis (McGill ID: 260422259), 
			  Jingyun Liu (McGill ID:260657058)

All pages and programs are hosted on the Yuchen and Jingyun's folders because there was an issue with Mathieu's CGI folder.

Contributions:
========================
Landing Page
========================
/home/2015/yli205/public_html/index.html
hyperlink: http://www.cs.mcgill.ca/~yli205/index.html
Made by: Yuchen Li

========================
Login and New User Page
========================
/home/2016/jliu164/public_html/login.html
hyperlink: http://www.cs.mcgill.ca/~jliu164/login.html
Made by: Yuchen Li

========================
login.c
========================
/home/2016/jliu164/public_html/login.c
http://www.cs.mcgill.ca/~jliu164/cgi-bin/login.cgi
Made by: Jingyun Liu

========================
register.c
========================
/home/2016/jliu164/public_html/cgi-bin/register.c
http://www.cs.mcgill.ca/~jliu164/cgi-bin/register.cgi
Made by: Jingyun Liu

========================
Dashboard.py
========================
/home/2015/yli205/public_html/cgi-bin/dashboard.py
Made by: Mathieu Roussel-Lewis

========================
newstatus.py
========================
/home/2015/yli205/public_html/cgi-bin/newstatusmasthieu.py
Made by: Mathieu Roussel-Lewis

========================
makefriends.py
========================
/home/2015/yli205/public_html/cgi-bin/makefriends.py
Made by: Yuchen Li

========================
newfriends.py
========================
/home/2015/yli205/public_html/cgi-bin/newfriends.py
Made by: Mathieu Roussel-Lewis & Yuchen Li

========================
seefriends.c
========================
/home/2016/jliu164/public_html/cgi-bin/seefriends.c
http://www.cs.mcgill.ca/~jliu164/cgi-bin/seefriends.cgi
Made by: Jingyun Liu

========================
see_a_profile.py
========================i
Takes the user to a page to view info regarding the friend that they selected to view
home/2016/jliu164/public_html/cgi-bin/profile.py
http://www.cs.mcgill.ca/~jliu164/cgi-bin/profile.py
Made by: Yuchen Li & Jingyun Liu

========================
list of html templates
========================
Made by: Yuchen Li
1. error.html ----- error message when login fails
2. friendInfo.html ----- displays the infomation of a friend
3. friendshipMade.html ----- template for page after makefriends.py is called
							 links back to dashboard or logout
4. makefriends.template ----- template for the make friends page
5. statusSubmitted.html ----- page for when status has been submitted, links back to dashboard or logout
6. successfulReg.html ----- page to inform user that registration was successful, links to login page
7. sucessLogin.html ----- page to get to when login succeeded, links to dashboard
8. dashboard.template ------ template for the dashboard, has links to the "make new friend", "see friends", and logout
9. see.html ------ template for seefriends page, displays different users with links to their profile
