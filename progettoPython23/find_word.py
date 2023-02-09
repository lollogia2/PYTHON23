from tkinter import *
from collections import defaultdict, deque
from itertools import chain, permutations
import errors

# --------------------------------definizione funzioni utili--------------------------------
loop_counter = 0


def reset_counter():
    global loop_counter
    loop_counter = 0


def make_anagrams(word, d):
    all_anagram = [''.join(element) for element in list(permutations(word))]
    make_sense = []
    for elemento in all_anagram:
        if elemento in d:
            make_sense.append(elemento)

    return make_sense


def get_dictionary_word_list():
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


# ritorna tutte le abbreviazioni (di una lettera) di una data 'word'
def shortened_words(word):
    # print(loop_counter)
    for i in range(len(word)):
        yield word[:i] + word[i + 1:], i


# crea un dizionario che ha come chiave la paerola abbreviata e come elemento la parola intera
def make_graph(d):
    g = defaultdict(list)
    for word in d:
        for short in shortened_words(word):
            g[short].append(word)
    print(g)
    return g


# to-do = lista di parole utilizzabili seguendo le 3 regole
# seen  = dizionario contenente tutte le parole comprese le sue radici
def walk_graph(g, d, start, end):
    global loop_counter
    todo = deque([start])
    seen = {start: None}
    while todo:
        # print(to-do)
        if loop_counter < 600:
            # print(loop_counter)
            word = todo.popleft()
            if word == end:
                break

            same_length = chain(*(g[short] for short in shortened_words(word)))  # * print the list separated by spaces
            one_longer = chain(*(g[word, i] for i in range(len(word) + 1)))
            one_shorter = (w for w, i in shortened_words(word) if w in d)
            anagram = make_anagrams(word, d)
            for next_word in chain(same_length, one_longer, one_shorter, anagram):
                if next_word not in seen:
                    seen[next_word] = word
                    # print(seen)
                    todo.append(next_word)
            loop_counter = loop_counter + 1
        else:
            typeError: SystemError
            return None

    else:  # no break, i.e. not reachable
        return None  # not reachable

    path = [end]
    # print(seen)
    while path[-1] != start:
        path.append(seen[path[-1]])
    return path[::-1]
