#include <stdio.h>

void displayList(char item[][255], int count){
	printf("Here is your list for the shopping!");
	for (int i =0; i < count; i++){
		printf("%d. %s", i+1, item[i]);
	}
}

int main() {
	//To implement many items i should use an array
	//The shopping list takes 10 items at a time.
	char item[10][255];
	int n;
	
	printf("Mystique's Shopping List Program\n");
	printf("How man items do you want to add ( max 10 )\n");
	scanf("%d", &n);
	
	for (int i =0; i< n && i < 10; i++){
		printf("Enter item %d:", i+1);
		fgets(item[i], 255, stdin);
	}
	displayList(item, n);
	return 0;
}
