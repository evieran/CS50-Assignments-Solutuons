#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // Prompt for input
    string message = get_string("Enter a message: ");

    // For each character in the message
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        // Convert character to ASCII value
        int ascii = (int) message[i];

        // Convert ASCII value to binary and print bulbs
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            // Shift bits to the right and mask with 1 to get individual bits
            int bit = (ascii >> j) & 1;
            print_bulb(bit);
        }

        // Print a newline to separate characters (bytes)
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
