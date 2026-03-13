#include <stdio.h>

void  Display(char name[][255], int phoneNumber[], char email[][255]){
	int i=0;
	printf("Mystique's Address Book:\n");
	
	for(i=0; i<10; i++){
		printf("Name: %s, PhoneNo.: %d, \n Email: %s", name[i], phoneNumber[i], email[i]);
	}
}

int main(){
	char name[10][255];
	int phoneNumber[10];
	char email[10][255];
	int i = 0;
	
	for (i=0; i < 10; i++){
		
		printf("Enter Name:");
		fgets(name[i] , 255, stdin);
	
		printf("Enter Phone Number:");
		scanf("%d", &phoneNumber[i]);
		getchar(); // this consumes the new line before getting the email from the user
	
		printf("Enter Emaiil Address:");
		fgets(email[i], 255, stdin);
	}
	
	Display(name, phoneNumber, email);
	return 0;
}
