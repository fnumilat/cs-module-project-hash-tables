def word_count(s):
    # Your code here

    # create a dictionary
    dic = {}

    # loop through string and separate them
    for word in s.split():
        # create a var for the lowered case word
        word = word.lower()
        # create a var for the panctuation
        punctuation = '":;,.-+=/\\|[]{}()*^&'

        # loop through each element in the word
        for ele in word:
            # and see if each element is in the panctuation
            if ele in punctuation:
                # then replace each element in the word with string
                word = word.replace(ele, "")
        # if the word is in dictionary
        if word in dic:
            # then increase the counter by 1
            dic[word] += 1

        # and if the word is not equal to string
        # update the dictionary with the word and number 1
        elif word != '':
            dic.update({ word: 1 })
    # return the dictionary
    return dic



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))