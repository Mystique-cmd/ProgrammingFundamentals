#include <stdio.h>

int main(){
	int arr[10];
	int size = sizeof(arr)/sizeof (arr[0]);
	int target;

	//GEtting user input for array elements
	printf("Enter %d values for the array:\n",size);
	for (int i=0; i <size; i++){
		scanf("%d", &arr[i]);
	}

	//Getting the number to search for
	printf("Enter the value you are searching for\n");
	scanf("%d", &target);

	//Searching for the number
	int found = 0;
	for ( int i = 0; i < size; i++){
		if (arr[i] == target){
			printf("Element found at index %d\n",i);
			found = 1;
			break; //stop after finding
			}
		}
	if (!found){
		printf("Element not found\n");
		}
return 0;
}
