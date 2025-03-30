import random
from enigma import PlugBoard, ALPHABET, Rotor, Reflector, EnigmaMachine

if __name__ == '__main__':

    get_random_alphabet = lambda : ''.join(
        random.sample(ALPHABET, len(ALPHABET))
    )
    print(get_random_alphabet())

    p = PlugBoard(get_random_alphabet())
    r1 = Rotor(get_random_alphabet(), 3)
    r2 = Rotor(get_random_alphabet(), 2)
    r3 = Rotor(get_random_alphabet(), 1)

    r = list(ALPHABET)
    indexes = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(indexes)/2)):
        x = indexes.pop(random.randint(0, len(indexes)-1))
        y = indexes.pop(random.randint(0, len(indexes)-1))
        r[x], r[y] = r[y], r[x]
    print(''.join(r))
    reflector = Reflector(''.join(r))

    machine = EnigmaMachine(
        p, [r1,r2,r3], reflector
    )
    s = 'ATTACK SILICON VALLEY'
    e = machine.encypt(s)
    print(e)
    d = machine.decypt(e)
    print(d)