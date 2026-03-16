#include <stdio.h>
int main(){
	FILE *outFile;
	int value = 123;
	double pi = 3.14259;
	const char *message = "Introduction Protocol";
	
	//Open the file for writing 
	outFile = fopen("output.txt", "w");
	if (outFile == NULL){
		perror("Error opening file");
		return 1;
	}
	
	//write formatted data to file
	fprintf(outFile, "This is an integer: %d\n", value);
	fprintf(outFile, "This is pi: %2f\n", pi);
	fprintf(outFile, "%s\n", message);
	
	fclose(outFile);
	printf("Data written to output.txt\n");
	
	return 0;
}
