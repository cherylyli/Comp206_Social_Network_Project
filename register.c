#include <stdio.h>
#include <stdlib.h>

/*Verify a new user: Unique user name*/

void printWeb(char*);

char userName[20];
    char firstName[20];
    char lastName[20];
    char pwd[20];
    char jobDescr[100];
    char gender[10];
    char* data;
int main(){
    
        //get data from packet
        char* info[] = {userName, pwd, firstName, lastName, jobDescr, gender};
        data = getenv("QUERY_STRING");
        //char* data = "username=2134&password=123&first_name=wer&last_name=234&job_description=rqwe&gender=female";
       
        int i=0; int count=0;
        for(;count<6;count++){
                for(;*(data+i)!='=';i++) ;
                i+=1; int k=0;
        
                for(;*(data+i)!='&'&&*(data+i)!='\0'&&*(data+i)!=EOF;i++) {
                        info[count][k]=*(data+i);
                        k++;

                }
             }
        
        //check if username unique
        FILE* fpt = fopen("user.txt","r+");
        if(!fpt) {
            printf("error opening user.txt:");
            exit(1);
        }
        else{
            
            char user[50];
            while(fgets(user, 199, fpt)){
                    
                    //username unique?
                    if(!strncmp(userName, user, strlen(userName)))
                    {
                        printWeb("../../../../2015/yli205/public_html/error.html");
                        exit(1);
                    }
                    int k=0;
                    for(; *(user+k)!='\0';k++) *(user+k)='\0';
                }       
      
       // fseek(fpt, 0, SEEK_END);
        //append info to the end of file

	//REPLACE '+' WITH ' ' IN jobDescr
	int k=0;
	for(;k<strlen(jobDescr);k++){
        if (jobDescr[k]=='+') jobDescr[k]=' ';
    }

        fprintf(fpt, "%s\n%s\n%s\n%s\n%s\n%s\n", userName, pwd, firstName, lastName, jobDescr, gender);


        fclose(fpt);
        //display success page linking direct back to login page
        FILE* friends = fopen("../../../../2012/mrouss223/public_html/friends.txt","r+");
        fseek(friends, 0, SEEK_END);

	//ADD A \n AFTER %s?
        fprintf(friends, "%s\n", userName);

        fclose(friends);
        
        printWeb("../../../../2015/yli205/public_html/successfulReg.html");

	}
        return 0;
}

void printWeb(char* input){
    printf("Content-Type:text/html\n\n");
    //printf("data:%s",data);
   // printf("%s %s %s %s %s %s ", userName, pwd, firstName, lastName, jobDescr, gender);
    FILE *f = fopen(input, "r");
    int ch;
    
    while((ch=fgetc(f))!=EOF) putchar(ch);

    fclose(f);
    
}
