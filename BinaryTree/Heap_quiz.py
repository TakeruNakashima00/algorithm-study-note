import heapq
from collections import Counter
from typing import List


# Q. output the lists in a heap in decending of theire frequency of occurrence.

def top_n_with_dict(words: List[str]) -> List[str]:
    d = {}
    for word in words:
        # when get some word from dict, you need to get default value
        d[word] = d.get(word, 0) + 1
    print(d)


def top_n_with_counter(words: List[str], n) -> List[str]:
    counter_word = Counter(words)
    print(counter_word)

    print(counter_word.most_common(n))


def top_n_with_heap(words: List[str], n: int):
    # dict
    d = {}
    for word in words:
        d[word] = d.get(word, 0) + 1
    print(d) # {'python': 3, 'c': 2, 'java': 1, 'go': 2}

    # list
    data = [(-d[word], word) for word in d]
    print(d) # [(-3, 'python'), (-2, 'c'), (-2, 'go), (-1, 'java')]

    # heapq
    heapq.heapify(data)
    print(data) # [(-3, 'python'), (-2, 'c'), (-2, 'go), (-1, 'java')]
    return [heapq.heappop(data)[1] for _ in range(n)] # ['python', 'c', 'go]



if __name__ == '__main__':
    w = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    # top_n_with_dict(w)
    # top_n_with_counter(w, 3)
    print(top_n_with_heap(w, 3))