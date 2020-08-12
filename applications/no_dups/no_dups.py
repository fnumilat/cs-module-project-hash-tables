def no_dups(s):
    # Your code here

    # create a dictionary
    dic = {}
    # create a var for string
    result = ""

    # loop through the string and separate them
    for word in s.split():
        # see if a word is not in the dictionary
        # and if it's not equal to a string
        if word not in dic and word != "":
            # then inrease the result with the word
            result += f'{word} '
            # and return the word in the dictionary once
            dic[word] = 1
    # return the result and remove the extra spaces
    return result.rstrip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))