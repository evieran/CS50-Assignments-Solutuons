#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Variable to stop the height of the pyramid
    ints height;

    // Prompt the user for a positive integer between 1 and 8, inclusive
    do
    {
        height = get_int("Enter the height of the pyramid (1-8): ");
    }
    while (height < 1 || height > 8);

    // Print the value of height to confirm it's stored successfully
    printf("Stored height: %d\n", height);

    return 0;
}