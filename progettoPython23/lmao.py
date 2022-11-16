from collections import defaultdict


def get_dictionary_word_list():
    with open('words.italian.txt') as f:
        # create a  dictionary object to return
        # opening the file in read mode
        my_file = open("words.italian.txt", "r")
        # reading the file
        data = my_file.read()
        # replacing end splitting the text
        # when newline ('\n') is seen.
        data_into_list = data.split("\n")
        my_file.close()
        return data_into_list


def shortened_words(word):
    for i in range(len(word)):
        yield word[:i] + word[i + 1:], i


def make_graph(d):
    g = defaultdict(list)
    for word in d:
        for short in shortened_words(word):
            g[short].append(word)
    return g


# m = get_dictionary_word_list()
dictionary = get_dictionary_word_list()  # list of words
graph = make_graph(dictionary)
print(graph)