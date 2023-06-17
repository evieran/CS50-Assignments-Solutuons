#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start;
    printf("Enter the starting populatipn size (minimum 9): ");
    scanf("%d", &start);

    while (start < 9) {
        printf("Starting population size must be at least 9. Please enter again: ");
        scanf("%d", &start_population);
    }

    printf("Enter the ending population size (must be greater than or equal to starting point size): ");
    scanf("%d", &end);

    while (end < start) {
        printf("Ending population size must be greater than or equal to starting population size. Please enter again: ");
        scanf("%d", &end);
    }

    while (start < end) {
        
    }

    int years = 0;

    while (start < end)
    {
        start = start + (start / 3) - (start / 4);
        years++;
    }

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
    print("Years: %i\n", years);
}
