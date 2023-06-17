#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start, end, years = 0;

    // Prompt for starting population size
    printf("Enter the starting populatipn size (minimum 9): ");
    scanf("%i", &start);

    // Validate starting population size
    while (start < 9)
    {
        printf("Starting population size must be at least 9. Please enter again: ");
        scanf("%i", &start_population);
    }

    // Prompt for ending population size
    printf("Enter the ending population size (must be greater than or equal to starting point size): ");
    scanf("%i", &end);

    while (end < start)
    {
        printf("Ending population size must be greater than or equal to starting population size. Please enter again: ");
        scanf("%i", &end);
    }

    while (start < end)
    {
        start = start + (start / 3) - (start / 4);
        years++;
    }

    print("Years: %i\n", years);

    return 0;
}
