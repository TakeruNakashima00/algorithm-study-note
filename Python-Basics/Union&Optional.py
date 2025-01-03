from typing import Union, Optional

# in python
# by using mypy cli, we can check type is safe or not.
# python dont throw error, when executing python script.
"""
    mypy file_name
"""

"""
(base) takeru@macbookairm2 algorithm-study-note % mypy Python-Basics/Union&Optional.py

Python-Basics/Union&Optional.py:6: error: Argument 1 to "getNumber" has incompatible type "None"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
"""
def getNumber(num: int) -> int:
    return num

print(getNumber(None))



"""
(base) takeru@macbookairm2 algorithm-study-note % mypy Python-Basics/Union\&Optional.py
Success: no issues found in 1 source file
"""
def getNumber(num: Optional[int]) -> Optional[int]:
    return num

print(getNumber(None))



"""
(base) takeru@macbookairm2 algorithm-study-note % mypy Python-Basics/Union\&Optional.py
Success: no issues found in 1 source file
"""
def getNumber(num: int|None) -> int|None:
    return num

print(getNumber(None))



"""
(base) takeru@macbookairm2 algorithm-study-note % mypy Python-Basics/Union\&Optional.py
Success: no issues found in 1 source file
"""
def getNumberOrText(num: Union[int,str]) -> Union[int,str]:
    return num

print(getNumberOrText(1))
print(getNumberOrText("1"))