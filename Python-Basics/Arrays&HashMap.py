## List
### add value to list
stack = []
stack.append("math")
stack.append("science")
print(stack)

# pop
# stack.pop()
# print(stack)

# delete
stack.remove("math")
print(stack)

### access list last value
fruits = ["apple", "banana", "grape"]
print(fruits[-1])

for fruit in fruits:
    if "apple" in fruits:
        print("apple is exist in")

## Dict
### access hashmap
hashmap = {"name":"take", "age": 25, "job": "Developer"}

for key in hashmap:
    print(key)


for index, key in enumerate(hashmap):
    # print(index, key, hashmap.get(key))
    print(index, key, hashmap[key])

    # how to get value.
    # difference: if not exist key in hashmap 「hashmap[key]」happen error
    print(hashmap[key])
    print(hashmap.get(key))


## explain object method
hashmap = {"name":"take", "age": 25, "job": "Developer"}
# help(hashmap)