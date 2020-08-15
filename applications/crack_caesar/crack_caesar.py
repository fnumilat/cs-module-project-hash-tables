# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

from os import path

# Create a dictionary called lookup
lookup = dict()

# Create an array of E to Z called enLookup
enLookup = [
    'E',
    'T',
    'A',
    'O',
    'H',
    'N',
    'R',
    'I',
    'S',
    'D',
    'L',
    'W',
    'U',
    'G',
    'F',
    'B',
    'M',
    'Y',
    'C',
    'P',
    'K',
    'V',
    'Q',
    'J',
    'X',
    'Z']

# Create a method called findFrequency
# then create a method to open the file when its requested
# and make it read the file
def findFrequency(file):
    text = ''
    with open(path.abspath('{}'.format(file))) as f:
        text = f.read()
    
    # Loop through the file and looking for char
    for char in text:
        # See if char is a space then continue
        if char == ' ':
            continue
        # and if char is the enLookup array 
        # and see for the char in the dictionary
        # and increase it by one 
        # otherwise leave it 
        if char in enLookup:
            if char in lookup:
                lookup[char] += 1
            else:
                lookup[char] = 1

    # Sort the dictionary items and call it srotedArr
    sortedArr = sorted(lookup.items(), key=lambda x: x[1], reverse=True)
    
    # Create another dictionary called anotherLook
    anotherLook = dict()
    
    # Set the index at zero
    i = 0

    # Loop through the sorted array for item
    # if the first item in the new dictionary is equal
    # to the index in the enLookup array
    # then increase the index by one
    for item in sortedArr:
        anotherLook[item[0]] = enLookup[i]
        i += 1

    # Create a string called newText
    newText = ''

    # Loop through the text file for char
    # and if the char is in the lookup dictionary
    # then add the new text to the char in the anotherLook dictionary
    # otherwise add the new text to the char
    for char in text:
        if char in lookup:
            newText += anotherLook[char]
        else:
            newText += char

    # Print the new text
    print(newText)



# Call the findFrequency method and pass the text file in
findFrequency('ciphertext.txt')