import heapq

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap_data = []

for num in numbers:
    heapq.heappush(heap_data, num)
while heap_data:
    print(heapq.heappop(heap_data))


heapq.heapify(numbers)
print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(3, numbers))


# heapq
# heapq.heapqpush
# heapq.heappop
# heapq.nlargest
# heapq.nsmallest