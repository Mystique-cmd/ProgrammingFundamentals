#include <stdio.h>

//The function to perform the Binary search
int BinarySearch ( int arr[], int left, int right, int target){
	while(left <= right ){
		int mid = left + ( right - left) /2 //prevents overflow
		if(arr[mid] == target)
			return mid;//Found the element
		else if (arr[mid] < target )
			left = mid + 1; //search  in the right half
		else
			right = mid -1; //search in the left half
	}
	return -1// Not found
}
int main(){
int arr[20];
