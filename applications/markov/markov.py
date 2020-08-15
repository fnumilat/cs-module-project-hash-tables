import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()


# Create a var for splitting the words
split_words = words.split()

# Create a dictionary to hold the words
words_list = dict()

# Loop through the length of the words until end
# create a var for each word in the words,
# and create a var for the next word in the words
for index in range(len(split_words) -1):
    word = split_words[index]
    next_word = split_words[index + 1]

    # See if the word exists in the dictionary
    # then add the next word
    # and if not then set the next word to the current one
    if word in words_list:
        words_list[word].append(next_word)
    else:
        words_list[word] = [next_word]

# TODO: analyze which words can follow other words
# Your code here

# Create a data tuple to hold the ending panctuations
ending_panct = ('.', '?', '!')

# Create a method for generating sentences
def make_sentence(word):
    # Print each word and using the given method add space after each
    print(word, end=' ')

    # See if a word stops with any of the given ending panctuations
    # then print the new lines
    # otherwise using randomly choose words from the dictionary
    if word.endswith(ending_panct):
        print('\n')
        return
    else:
        make_sentence(random.choice(words_list[word]))


# TODO: construct 5 random sentences
# Your code here

make_sentence('One')
make_sentence('The')
make_sentence('Only')
make_sentence('But')
make_sentence('The')

