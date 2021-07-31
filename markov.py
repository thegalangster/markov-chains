"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_object = open(file_path)
    file_as_string = file_object.read()

    return file_as_string.replace("\n", " ").rstrip()


def make_chains(text_string ):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    value_list = ["text"]
    words = text_string.split()

    # iterate through each index in words until the length of index minus 2
    # (value at index, value at index + 1): append to list value at index + 2

    for index in range(0, len(words)-2):
        # chains.get([(words[index], words[index+1])]) = words[index+2]
        key = (words[index], words[index+1])
        value = words[index+2]

        existing_value = chains.get(key, [])
        existing_value.append(value)
        chains[key] = existing_value

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #pick random key

    selected_key = choice(list(chains.keys()))
    words.append(selected_key[0])
    words.append(selected_key[1])
    
    #pick random value from that key
    #loop until error
    while True:
        #from that key, pick random value
        if chains.get(selected_key) is not None:
            random_word = choice(chains[selected_key])
            words.append(random_word)
        else:
            return ' '.join(words)

        #from the string that's created, pick the last two words - find that key in the dictionary
        selected_key = (words[-2], words[-1])

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
