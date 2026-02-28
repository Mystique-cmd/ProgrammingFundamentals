#include <stdio.h>

void greetings(char* name, int age){
	age = age +1;
	printf("Hi %s You will turn %d next year", name, age);
}

int main() {
	char name [255];
	int age;
	printf("What is your name:");
	fgets(name, 255, stdin);
	printf("What is your age:");
	scanf("%d", &age);

	greetings(name,age);
	return 0;
	
}
