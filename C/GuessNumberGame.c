#include <stdio.h>
#include <stdlib.h> //The header file containing the function for random no generation
#include <time.h> //allows for seeding of the current time to the random no

int Generator(){
	//Generates th random number
	
	int LuckyNo = rand();
	printf("Your lucky number is : %d/n", &LuckyNo);
}
int main (){
	int Guess;
	
	//Getting user guess
	printf("What is your lucky number?");
	scanf("%d", &Guess);
	
	srand(time(NULL)); //Seeding the random number
	Generator();
	return 0;
}
