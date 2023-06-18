#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Variable to stop the height of the pyramid
    int height;

    // Prompt the user for a positive integer between 1 and 8, inclusive
    do
    {
        height = get_int("Enter the height of the pyramid (1-8): ");
    }
    while (height < 1 || height > 8);

    // Build the left-aligned pyramid
    for (int row = 1; row <= height; row++)
    {
        // Print hashes; the number of hashes is equal to the row number
        for (int hashes = 1; hashes <= row; hashes++)
        {
            printf("#");
        }

    // Move to the next line after printing hashes for the current row
    printf("\n");
}

    return 0;
}