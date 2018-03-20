#include <stdio.h>
#include <stdlib.h>

int main(){
	char *plain_text = "abcdefghijklmnopqrstuvwxyz";
	
	int key = 3;

	size_t length = strlen(plain_text);
	printf("Debigging Segmentation Fault\n");
	char *cipher_text;
	cipher_text = (char*) malloc(length * sizeof(char));
	int temp;
	int base = 97;
	
	

	for(int i = 0; i < length; i++){
		//printf("Debigging Segmentation Fault0\n"); 
		//printf("%d\n", plain_text[i]);
		temp = plain_text[i] + key;
		if(temp > 122){
			cipher_text[i] = base;
			base = base + 1;
		}
		else{
			cipher_text[i] = plain_text[i]+key;
		}
		
		// printf("Debigging Segmentation Fault1\n"); 
		// strcpy(cipher_text, *temp);



	}

	printf("%s\n",cipher_text);
	return 0;
}