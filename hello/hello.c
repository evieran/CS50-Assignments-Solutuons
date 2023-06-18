#include <stdio.h>
int main(void)
{
    char name[100];

    // Prompt the user to enter their name
    printf("Enter your name: ");

    // Read the name input from the user and store it in the 'name' variable
    scanf("%s", name);

    // Print a personalized greeting using the entered name
    printf("Hello, %s!\n", name);

    return 0;
}