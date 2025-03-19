from typing import List

"""
"hello" -> ["h","e","l","l","o"]
"""
def convertStrIntoList(char: str) -> List:
    helloList = [s for s in char]
    return helloList

print(convertStrIntoList("hello"))


"""
["h","e","l","l","o"] -> "hello"
"""
def convertListIntoStr(list: List) -> str:
   str = ''.join(list)
   return str

print(convertListIntoStr(["h","e","l","l","o"]))


"""
['', '', '']
"""
def createEmptyList():
    return [''] * 3

print(createEmptyList())

"""
[[''], [''], ['']]
"""
def createEmptyListInList():
    return [['']] * 3

print(createEmptyListInList())


NUM_ALPHABET_MAPPING = {
    0: '+',
    1: '@',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}


"[9, 7]"
def mappingList(list: List):
    return NUM_ALPHABET_MAPPING[list[1]]

print(mappingList([9,7]))
