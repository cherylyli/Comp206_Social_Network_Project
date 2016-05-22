/****************************************************
seefriends.c:
	This program generates a webpage that lists all 
	the usernames of friends for the current user.
****************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printWeb(char*);

char userName[20];
int main(){
	char*data =(char*) malloc(100);
	
	char line[200];
	//method = POST
	fgets(data,100,stdin);
	int i=9;//counter
	for(;data[i]!='\0';i++) userName[i-9]=data[i];

	FILE *f = fopen("../../../../2012/mrouss223/public_html/friends.txt", "r");
	//read a line of file
	while(fgets(line, 200, f)){
		//check the first token
		if (!strncmp(line, userName, strlen(userName))){
			//print see.html
			printWeb(line);

			fclose(f);
			exit(0);
		}
		//clear data
		int k=0;
		for(; *(line+k)!='\0';k++) *(line+k)='\0';
	}
	fclose(f);
	return 0;
}


void printWeb(char* input){
	printf("Content-Type:text/html\n\n");
	FILE* see = fopen("see.html","r");
	
	int ch;
	while((ch=fgetc(see))!='$') putchar(ch);
	char *p = strtok(input, " ");
	while((p=strtok(NULL, " "))!='\0'){    //while have more friends
		//print form
		printf("<ul class=\"prettyfriends\">\n<li><form method=\"get\" action=\"http://cgi.cs.mcgill.ca/~jliu164/cgi-bin/profile.py\">\n\t<input type=\"text\" class=\"hidden\" name=\"username\" value=\"%s\">\n\t<input type=\"text\" class=\"hidden\" name=\"friend\" value=\"%s\">\n<button type=\"submit\">%s</button>\n</form></li>\n</ul>", userName, p, p);
	}
	ch=fgetc(see);
	while((ch=fgetc(see))!='@') putchar(ch);
	printf("%s",userName);
	//REMOVE THIS LINE?
	ch=fgetc(see);
	//REMOVE ABOVE LINE?
	while((ch=fgetc(see))!=EOF) putchar(ch);

	fclose(see);
}
