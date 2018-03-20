#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	char *plain_text = "CRYPTOGRAPHY";
	char *key = "LUCKY";
	size_t length = strlen(plain_text);
	printf("The length of text is %zu\n", length);
	
	size_t key_length = strlen(key);
	printf("The length of key is %zu\n",key_length);
	char * cipher_text = (char*) malloc(length*sizeof(char));
	int j = 0;


	for(int i = 0; i< length; i++){
		cipher_text[i] = plain_text[i]+key[j];
		printf("%d\n",cipher_text[i]);
		
		j++;
		if(j == key_length){
			j = 0;
		}

	}
	printf("%s\n",cipher_text);
	return 0;

}