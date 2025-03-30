import string

ALPHABET = string.ascii_uppercase


class PlugBoard(object):

    def __init__(self, map_alphabet):
        self.alphabet = ALPHABET
        self.forward_map = {}
        self.backward_map = {}
        self.mapping(map_alphabet)

    def mapping(self, map_alphabet):
        # 'ABCD'
        # 'BADC'
        # '{'A': 'B', 'B': 'A,
        self.forward_map = dict(zip(self.alphabet, map_alphabet))
        self.backward_map = {v: k for k, v in self.forward_map.items()}

    def forward(self, index_num):
        char = self.alphabet[index_num]
        char = self.forward_map[char]
        return self.alphabet.index(char)

    def backward(self, index_num):
        char = self.alphabet[index_num]
        char = self.backward_map[char]
        return self.alphabet.index(char)


"""
PlugBoard
forward: {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'}
backward: {'B': 'A', 'A': 'B', 'D': 'C', 'C': 'D'}
forward 'A' => 'B'
backward 'B' => 'A'

forward logic
1. 'A' => 0: alphabet.index('A')
2.  0  => 'A' => 'B': x[alphabet[alphabet.index('A')]]
3. 'B' => 1: alphabet.index(x[alphabet[alphabet.index('A')]])
"""

class Rotor(PlugBoard):

    def __init__(self, map_alphabet, offset=0):
        super().__init__(map_alphabet)
        self.offset = offset
        self.rotations = 0

    def rotate(self, offset=None):
        if not offset:
            offset = self.offset
        # ['A','B','C'...'Z'] => ['Z','A','B','C'...'Y'] ex, offset=1
        self.alphabet = self.alphabet[offset:] + self.alphabet[:offset]
        self.rotations += offset
        return self.rotations

    def reset(self):
        self.rotations = 0
        self.alphabet = ALPHABET

class Reflector(object):

    def __init__(self, map_alphabet) -> None:
        self.map = dict(zip(ALPHABET, map_alphabet))

        for x, y in self.map.items():
            if x != self.map[y]:
                raise ValueError(x,y)

    def reflect(self, index_num):
        reflected_char = self.map[ALPHABET[index_num]]
        return ALPHABET.index(reflected_char)

class EnigmaMachine(object):

    def __init__(self, plug_board, rotors, reflector) -> None:
        self.plug_board = plug_board
        self.rotors = rotors
        self.reflector = reflector

    def encypt(self, text):
        return ''.join(self.go_through(c) for c in list(text))

    def decypt(self, text):
        for rotor in self.rotors:
            rotor.reset()
        return ''.join(self.go_through(c) for c in list(text))

    def go_through(self, char):
        char = char.upper()
        if char not in ALPHABET:
            return char

        index_num = ALPHABET.index(char)
        index_num = self.plug_board.forward(index_num)

        for rotor in self.rotors:
            index_num = rotor.forward(index_num)

        index_num = self.reflector.reflect(index_num)

        for rotor in reversed(self.rotors):
            index_num = rotor.backward(index_num)

        index_num = self.plug_board.backward(index_num)
        char = ALPHABET[index_num]

        for rotor in reversed(self.rotors):
            if rotor.rotate() % len(ALPHABET) != 0:
                break

        return char