#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            // Get the pixel
            RGBTRIPLE *pixel = &image[i][j];

            // Calculate the average of red, green, and blue values
            int average = round((pixel->rgbtRed + pixel->rgbtGreen + pixel->rgbtBlue) / 3.0);

            // Set the red, gree, and blue values to the average
            pixel->rgbtRed = average;
            pixel->rgbtGreen = average;
            pixel->rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get the original pixel
            RGBTRIPLE pixel = image[i][j];

            // Calculate the sepia values
            int sepiaRed = round(0.393 * pixel.rgbtRed + 0.769 * pixel.rgbtGreen + 0.189 * pixel.rgbtBlue);
            int sepiaGreen = round(0.349 * pixel.rgbtRed + 0.686 * pixel.rgbtGreen + 0.168 * pixel.rgbtBlue);
            int sepiaBlue = round(0.272 * pixel.rgbtRed + 0.534 * pixel.rgbtGreen + 0.131 * pixel.rgbtBlue);

            // Make sure they are not greater than 255
            sepiaRed = sepiaRed > 255 ? 255 : sepiaRed;
            sepiaGreen = sepiaGreen > 255 ? 255 : sepiaGreen;
            sepiaBlue = sepiaBlue > 255 ? 255 : sepiaBlue;

            // Set the new pixel values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels on the left and right side of the image
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;

            // Calculate the sum of colors in the neighboring pixels
            for (int k = -distance; k <= distance; k++)
            {
                for (int l = -distance; l <= distance; l++)
                {
                    int row = i + k;
                    int col = j + l;

                    // Check if the neighboring pixel is within the image boundaries
                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        sumRed += temp[row][col].rgbtRed;
                        sumGreen += temp[row][col].rgbtGreen;
                        sumBlue += temp[row][col].rgbtBlue;
                        count++;
                    }
                }
            }

            // Calculate the average color
            image[i][j].rgbtRed = round((float)sumRed / count);
            image[i][j].rgbtGreen = round((float)sumGreen / count);
            image[i][j].rgbtBlue = round((float)sumBlue / count);
        }
    }
    return;
}
