
# call by value
a = 1
b = 2
a = b
print(a) # 2

b = 3
print(a) # 2 or 3 ? A. 2


# call by reference
class Person():
    def __init__(self, name) -> None:
        self.name = name

person = Person("take")
print(person.name)

person2 = person
person.name = "take2"
print(person2.name)

print(person.name) # take or take2 ? A.take2
