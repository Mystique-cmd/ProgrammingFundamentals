#include <stdio.h>
#include <math.h>

int Add(int num1, int num2){
	int sum = num1 + num2;
	return sum;
}

int Subtract(int num1, int num2){
	int difference = num1 - num2;
	return difference;
}

int  Divide(int num1, int num2) {
	int quotient = num1/ num2;
	return quotient;
}

int Multiply(int num1, int num2){
	int product = num1 * num2;
	return product;
}

int main(){
	int num1;
	int num2;
	int operation;
	
	
	printf("Input Your 1st No.:");
	scanf("%d", &num1);
	getchar();
	
	printf("Enter Your 2nd No.:");
	scanf("%d", &num2);
	getchar();
	
	printf("Choose Your Operation ( e.g 1, 2 ,3 or 4:\n");
	printf("1. Addition \n 2. Subtraction \n 3.Division \n 4. Multiplication \n");
	scanf("%d", &operation);
	
	if (operation==1){
		printf("Sum: %d \n ", Add(num1, num2));
	}else if(operation == 2){
		printf("Difference: %d \n",Subtract(num1, num2));
	}else if (operation == 3){
		printf("Quotient: %d \n", Divide(num1,num2));
	}else if (operation == 4){
		printf("Product: %d \n", Multiply(num1, num2));
	}
	
	return 0;
}
