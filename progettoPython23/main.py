from collections import defaultdict, deque
from itertools import chain


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


def shortened_words(word):
    for i in range(len(word)):
        yield word[:i] + word[i + 1:], i


def make_graph(d):
    g = defaultdict(list)
    for word in d:
        for short in shortened_words(word):
            g[short].append(word)
    return g


def walk_graph(g, d, start, end):
    todo = deque([start])
    seen = {start: None}
    while todo:
        word = todo.popleft()
        if word == end:  # end is reachable
            break

        same_length = chain(*(g[short] for short in shortened_words(word)))
        one_longer = chain(*(g[word, i] for i in range(len(word) + 1)))
        one_shorter = (w for w, i in shortened_words(word) if w in d)
        for next_word in chain(same_length, one_longer, one_shorter):
            if next_word not in seen:
                seen[next_word] = word
                todo.append(next_word)
    else:  # no break, i.e. not reachable
        return None  # not reachable

    path = [end]
    while path[-1] != start:
        path.append(seen[path[-1]])
    return path[::-1]


dictionary = get_dictionary_word_list()  # list of words
graph = make_graph(dictionary)
print(" -> ".join(walk_graph(graph, dictionary, "pr", "porro")))
