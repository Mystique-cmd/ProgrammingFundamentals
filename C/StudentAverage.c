#include <stdio.h>
int main(){
	//Getting the student details
	char name[255];
	int math, eng, kisw, bio, chem, phy, geo, bus;
	
	printf("Enter your marks Marks \n");
	printf("Student's Name:");
	fgets(name, 255, stdin);
	printf("Math:");
	scanf("%d", &math);
	
	printf("English:");
	scanf("%d", &eng);
	
	printf("Kiswahili:");
	scanf("%d", &kisw);
	
	printf("Biology:");
	scanf("%d", &bio);
	
	printf("Chemistry:");
	scanf("%d", &chem);
	
	printf("Physics:");
	scanf("%d", &phy);
	
	printf("Geography:");
	scanf("%d", &geo);
	
	printf("Business:");
	scanf("%d", &bus);
	
	//calculating the average
	float avg = (math + eng + kisw + bio + chem + phy + geo + bus ) / 8;
	
	printf("The average marks is : %f", avg);
	return 0;
}
