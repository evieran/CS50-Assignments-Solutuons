#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 3) {
        fprintf(stderr, "Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // TODO #2: Open input file for reading
    FILE *input == fopen(argv[1], "r");
    if (input == NULL) {
        fprintf(stderr, "Could not open file %s.\n", argv[1]);
        return 1;
    }

    // TODO #3: Read header
    WAVEHEADER header;
    if (fread(&header, sizeof(WAVEHEADER), 1, input) != 1) {
        fprintf(stderr, "Could not read header from %s. \n", argv[1]);
        fclose(input);
        return 1;
    }

    // Use check_format to ensure WAV format
    // TODO #4

    // Open output file for writing
    // TODO #5

    // Write header to file
    // TODO #6

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8
}

int check_format(WAVHEADER header)
{
    // TODO #4
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return 0;
}