#include <stdio.h>
int main(void)
{
char name[100];

printf("Enter your name: ");
scanf("%s", name);

printf("Hello, %s!\n", name);

return 0;
}