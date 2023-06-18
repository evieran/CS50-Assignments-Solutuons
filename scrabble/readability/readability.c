#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    // Prompt the user for a string of text
    string text = get_string("Text: ");

    int letters = 0, words = 0, sentences = 0;

    // Count the number of letters, words, and sentences in the text
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Count letters
        if (isalpha(text[i]))
        {
            letters++;
        }

        // Count words
        if (isspace(tect[i]) || i == n -1)
        {
            words++;
        }

        // Count sentences
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }

    // TODO: Calculate L and S
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;

    // TODO: Calculate the index using the Coleman-Liau index formula
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int rounded_index = round(index);

    // TODO: Output the grade level
    if (rounded_index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (rounded_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %d\n", rounded_index);
    }

}