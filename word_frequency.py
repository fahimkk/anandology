# Write a program to count frequency of characters in a given file. 
# Can you use character frequency to tell whether the given file 
# is a Python program file, C program file or a text file?

def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
    return open(filename).read().split()

def main(filename):
    frequency = word_frequency(read_words(filename))
    frequency_sorted_list = sorted(frequency.keys(),\
        key=lambda x: frequency[x], reverse=True)
    for word in frequency_sorted_list:
        print(word, frequency[word])




""" if __name__ == "__main__":
    import sys
    main(sys.argv[1])
 """