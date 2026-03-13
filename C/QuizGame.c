#include <stdio.h>
#include <string.h>

int  Quiz(){
	int i = 0;
	int score = 0;
	char Reply[3][255];
	char Questions[3][255] = {"Why are you gay?", "Who let the dogs out?", " One-term or Two- term?"};
	char Answers [3][255] = {"Who said I am gay", "Who", "One-Term"};
	for ( i = 0; i < 3 ; i++){
		printf("%s \n", &Questions[i]);
		fgets(Reply[i], 255, stdin);
		Reply[i][strcspn(Reply[i], "\n")] = 0;
		if (strcmp(Reply[i], Answers[i] )== 0){
			score++;
		}else {
			continue;
		}
	}
	return score;
}

int main(){
	int score = Quiz();
	if (score >= 2){
		printf("Congratulations! Your brain is well rotten");
	}else{
		printf("Your brain is not rotten enough!! Sorry");
	}
	return 0;
}
