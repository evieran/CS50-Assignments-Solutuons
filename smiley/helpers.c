#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate through each row
    for (int i = 0; 1 < height; i++)
    {
        // Iterate through each pixel in the row
        for (int j = 0; j < width; j++)
        {
             // Check if the pixel is black (red, green, and blue are all 0)
            if (image[i][j].rgbtRed == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtBlue == 0)
            {
                // Change the pixel color to red
                image[i][j].rgbtRed = 255;
                image[i][j].rgbtGreen = 0;
                image[i][j].rgbtBlue = 0;
            }

        }
    }
}
