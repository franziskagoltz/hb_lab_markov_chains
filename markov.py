# we are importing the sys module
import sys 
# we store the second and third argument we pass on the command line as a text files to the file_name 
# and file_name2 variables. So we don't have to update this file with the text path
# so on command line markov.py is argv[0] and any text files is argv[1] argv[2]
file_name, file_name2 = sys.argv[1], sys.argv[2]     

from random import choice


#changed the function the way we can pass two text files to it
def open_and_read_file(file_name, file_name2):
    """
    Takes a string that is in each file, opens the files, and turns
    the file's contents as one string of text.
    """

    # Opens the entire file and stores it in the text variable
    text = open(file_name).read() + open(file_name2).read()

    return text 


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # creating a word list of the text_string string
    words = text_string.split()

    # we are looping through the words list by index
    for index in range(len(words)-2):
        
        # if tuple of current and the next elemet is not in dictionary 
        # create this tuple key in a dictionary and assign an empty list as a value to it
        if (words[index], words[index+1]) not in chains:
            chains[(words[index], words[index+1])] = []

        # other wise we have the tuple key in our dictionary and appending 
        # the second element following our current index to the value list
        chains[(words[index], words[index+1])].append(words[index+2])        
       
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # we are randomly choosing a key tuple from our dictionary 
    # and storing that value in the chains_key var
    chains_key = choice(chains.keys())  

    # we are initializing text as a list and assigning the second value of chains_key
    text = list(chains_key)

    # we check if the key we generated is in our dictionary 
    while chains_key in chains:

        # we update the tuple of chains_key to second element of our initial chains_key
        # and a random value from it's list value 
        chains_key = (chains_key[1], choice(chains[chains_key]))    

        # we are updating the text list by appending the second element of our 
        # newly made chains_key tuple
        text.append(chains_key[1])

    # we are joining the text list elements into a string 
    return " ".join(text)


# Open the file and turn it into one long string
input_text = open_and_read_file(file_name, file_name2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text