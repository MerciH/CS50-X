// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 50000;

// Hash table
node *table[N];

//counter of size of the dic
unsigned int counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int index = hash(word);
    node *cursor;
    cursor = table[index];
    while(cursor != NULL)
    {
        if(strcasecmp(cursor->word, word) != 0)
        {
            cursor = cursor->next;
        }
        else
        {
            return true;
        }

    }
    free(cursor);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    unsigned int hash = 0;
    char wordcopy[LENGTH+1];
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        wordcopy[i]=tolower(word[i]);
        hash = (hash << 2) ^ wordcopy[i];
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    char words[LENGTH+1];
    FILE *file;
    file = fopen(dictionary, "r");
    if(file == NULL)
    {
        return false;
    }

    while (fscanf(file, "%s", words) != EOF)
    {
        counter++;
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            unload();
            return 1;
        }
        //copy the word from the dic to the node
        strcpy (n->word, words);

        //hash the ward for the index to be used
        unsigned int index = hash(n->word);

        //initialize a head to point to the hashtable index/bucket
        node *head = table[index];

        //instert in the list
        if(head==NULL)
        {
            table[index] = n;
        }
        else
        {
            node *temp = malloc(sizeof(node));
            if (temp == NULL)
            {
                return 1;
            }
            temp = table[index];
            n = temp->next;
            table[index]=n;
        }


    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // free the memory

    for(int i = 0; i<N; i++)
    {
        node *head = NULL;
        head = table[i];
        if (head != NULL)
        {
            node *cursor = NULL;

            cursor = table[i];

            node *temp = NULL;

            temp = cursor;
            cursor = cursor->next;
            free(temp);

        }
    }
    return true;
}
