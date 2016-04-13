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
    
    #this sets our range to end at the second to last item 
    #this is important because we need to avoid IndexError: list out of range
    for i in range(len(words) - 2):
        two_words = words[i], words[i + 1]
        third_words = words[i + 2]
        
        if two_words not in chains:
            #this puts the tuples into the dictionary as keys and 
            #initial third words as values
            chains[two_words] = [third_words]
        else:
            #if key exists, appends additional values to third_words list
            chains[two_words].append(third_words)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    #text = empty string to put all our text in eventually
    text = ""
    #the initial key is a random choice (see import random choice at top of program)
    initial_key = choice(chains.keys())

    

    
    initial_value = choice(chains(initial_key.values(i)))

    #this puts the tuples into the dictionary as keys
    while initial_key is in dictionary
        choice(chains.values[from the list that goes with that key])

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
py = make_text(chains)

#print random_text
