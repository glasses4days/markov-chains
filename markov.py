from random import choice



def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    the_file = file_path
    contents = open(the_file).read()
    
    return contents




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
    words = text_string.split()
    
    
    for i in range(len(words) - 1):
        two_words = words[i], words[i + 1]
        #options =  []
        print words[i], words[i + 2]
        #this puts the tuples into the dictionary as keys
        chains[two_words] = [] # this empty list was for the list of values
        #how do we get them in there? i+2 gives us "out of range error"
    
    # words_list_value = []
    # for i in range(len(words) - 1):
    #     words_list_value = words[i + 2]

    print chains

    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
py = make_text(chains)

#print random_text
