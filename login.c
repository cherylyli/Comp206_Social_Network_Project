/*********************************************************
login.c: 
  A text file named <users.txt> exists on the server 
that contains the profile information and login credentials 
of all the users. If the login operation fails the program 
displays an error web page to the user with two links that 
directs them back to the landing page or the login page. If 
the login operation was successful then the program generates 
the user's dashboard page.
***********************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char userName[20];
char pwd[20];
char data[100];
char file[100];
char pwdLine[100];

void printWeb(char*);

int main(){
	//POST: read from stdin
	int length = atoi(getenv("CONTENT_LENGTH"));
	fgets(data, length, stdin);
	//sscanf(data, "username=%s&password=%s", userName, pwd);

	char* info[] = {userName, pwd};
       
        int i=0; int count=0;
        for(;count<2;count++){
                for(;*(data+i)!='=';i++) ;
                i+=1; int k=0;
        
                for(;*(data+i)!='&'&&*(data+i)!='\0'&&*(data+i)!=EOF;i++) {
                        info[count][k]=*(data+i);
                        k++;

                }
             }
	//check login info
	FILE *fpt=fopen("user.txt", "r");
	if(!fpt) {
		perror("Error opening file");

		//WHY NOT RETURN 1?
		return (-1);
	}
	while(fgets(file, 100, fpt)){
		int k=0;
		
		//read a line. check if is one of the usernames
		if(!strncmp(file, userName, strlen(userName))){
			fgets(pwdLine, 100, fpt);
			if(!strncmp(pwdLine, pwd, strlen(pwd))){
				//print user page
				
				printWeb("../../../../2015/yli205/public_html/sucessLogin.html");
				goto end;
			}
			else{
				printWeb("../../../../2015/yli205/public_html/error.html");
				goto end;
			}
			
		}
		for(; *(file+k)!='\0';k++) *(file+k)='\0';
	}

	fclose(fpt);
	//username not found
	printWeb("../../../../2015/yli205/public_html/error.html");
end:
	return 1;
}

void printWeb(char* input){
	printf("Content-Type:text/html\n\n");
	//printf("%s",data);
	
	FILE *f = fopen(input, "r");
	int ch;

	
	while((ch=fgetc(f))!=EOF){
		if (ch=='@'){
			printf("%s", userName);
			ch=fgetc(f);
		} 
		putchar(ch);
	}

	fclose(f);
	
}
