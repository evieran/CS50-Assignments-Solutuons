// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Number of words in the dictionary
unsigned int word_count = 0;

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long hash_value = 5381;
    int c;

//Iterate over the characters in the word
    while ((c = *word++))
    {
        // Convert the character to lowercase
        c = tolower(c);

        // Hash * 33 + c
        hash_value = ((hash_value << 5) + hash_value) + c;
    }

// Use modulo to make sure it's within range
    return hash_value % N;
}

// Loads dictionary into memory, returning true if succeessful else false
bool load(const char *dictionary)
{
// Initialize hash table
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Load each word from the dictionary
    while (fscanf(file, "%s", word) != EOF)
    {
        // Create a new node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
           fclose(file);
            return false;
        }

        // Copy word into node
        strcpy(new_node->word, word);

        // Get the hash value for the word
        int index = hash(word);

        // Insert the node into the hash table
        new_node->next = table[index];
        table[index] = new_node;

        // Increment the word count
        word_count++;
    }

    // Close dictionary file
    fclose(file);

    // Indicate success
    return true;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to obtain a hash value
    unsigned int index = hash(word);

    // Search the linked list at that index in the hash table
    for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
    {
        // Compare words case-insensitive
        if (strcasecmp(cursor->word, word) == 0)
        {
            // The word is found in the dictionary
            return true;
        }
    }

    // The word was not found in the dictionary
    return false;
}

// Return number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Iterate through each bucket in the hash table
    for (int i = 0; i < N; i++)
    {
        // Set cursor to point to the start of the linked list
        node *cursor = table[i];

        // Traverse the linked list and free memory
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }

    return true;
}
