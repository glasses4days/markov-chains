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
    #the only random key we will have
    initial_key = choice(chains.keys())
    #grabs an random value from the list of values for the initial key
    initial_value = choice(chains[initial_key])
    # print initial_key
    # print initial_value
    #adds the initial_key and initial_value to the text string with spaces
    #use join because initial_key is a tuple
    text = " ".join(initial_key) + " " + initial_value
    #text = text + " " + initial_value
    print text
    
    #sets up next key as a tuple made from inital_key index 1 and initial value
    next_key = (initial_key[1], initial_value)
    print next_key

    
    while True:
        current_key = next_key

        if current_key in chains:


        else:
            False
    # and then look for them as a key in the dictionary
    # then check for that new key in the chains dictionary
    # and if its there chose a random value from that key
    # and got through the above again and again....
    # code idea below
    # while initial_key in chains:  
    for new_key in chains:
            chains[new_key] = chains.get(choice([initial_key])
            (new_key) + initial_value

    each time we go throuhg the loop, if the new key is in th dictionary
    we want to choose a random value from that key and add the items to the text 
    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
py = make_text(chains)

#print random_text
