#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pwnable_harness.h"


void handle_connection(int sock) {
	char* username = malloc(50);
	char* shell = malloc(50);
	
	printf("username at %p\n", username);
	printf("shell at %p\n", shell);
	
	strcpy(shell, "/bin/ls");
	
	printf("Enter username: ");
	scanf("%s", username);
	
	printf("Hello, %s. Your shell is %s.\n", username, shell);
	system(shell);
}

/* Everything below can safely be ignored and is not part of the challenge. */
int main(int argc, char** argv) {
	server_options opts = {
		.user = "heap0",
		.chrooted = true,
		.port = 7003,
		.time_limit_seconds = 30
	};
	
	return server_main(argc, argv, opts, &handle_connection);
}
