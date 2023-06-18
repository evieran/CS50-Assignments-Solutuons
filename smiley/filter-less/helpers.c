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
    for (int i = 0; i < height: i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Apply the sepia algorithm to each pixel's red, green, and blue values
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = o; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels on the left and right side of the image
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
            // For each pixel, average the colors of pixels that are within a certain distance.
        }
    }
    return;
}
