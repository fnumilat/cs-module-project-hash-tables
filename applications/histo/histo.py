# Your code here

# Create a method for this to function
def histogram(string):
    # Create a method to open the file and to be able to read it
    with open(string) as file:
        w = file.read()

    # Create a var for words and make the output in lowercase and 
    # split the words
    words = [x.lower() for x in w.split()]

    # Create a dictionary to store the counted words
    word_count = dict()

    # Loop through the length of the words
    for index in range(len(words)):
        # Create a string for the new words
        new_word = ""
        # Loop throgh each word in the words
        for character in words[index]:
            # and if the character is a aplhanumeric
            # then add that character to the new word string
            if character.isalnum():
                new_word += character
        # also see if the new word is in the word count dictionary
        # then increase the count by one
        # otherwise leave the count by its original number = 1
        if new_word in word_count:
            word_count[new_word] += 1
        else:
            word_count[new_word] = 1
    
    # Create a sorted dictionary
    sorted_dict = {k:v for k,v in sorted(word_count.items(), key=lambda item:item[1], reverse=True)}

    # Loop through the sorted dictionary
    # and set each key to be equaled to # 
    # and multiply by the number its occurance
    for key in sorted_dict:
        sorted_dict[key] = "#" * sorted_dict[key]
        # Print the keys and give a length of 20 for the keys plus the space
        print(key.ljust(20, " ") + sorted_dict[key])
    
histogram('robin.txt')
