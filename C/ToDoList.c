#include <stdio.h>

void DisplayList (char item[][255]) {
	//this fucntions displays the to-do-list
	int i = 0;
	for (i = 0; i<10; i++) {
		printf("%d. %s", i+1, item[i]);
	}
}
int main() {
	char item [10][255];
	int i =0;
	for (i=0; i < 10; i++){
		printf("What's on your  mind : \n");
		fgets( item[i], 255, stdin);
	}
	DisplayList(item);
	return 0;
}
