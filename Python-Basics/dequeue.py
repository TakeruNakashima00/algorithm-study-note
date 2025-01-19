from collections import deque

# create empty list
d = deque()

# create empty list with default value
d = deque([1, 2, 3])

d.append(4)
d.appendleft(0)
d.popleft()
print(d)
