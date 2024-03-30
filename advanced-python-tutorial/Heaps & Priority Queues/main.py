import heapq

data = [10,20,43,1,2,65,17,44,2,3,1]
data = [-x for x in data]

print(sorted(data))

heapq.heapify(data)
print(data)

print(heapq.heappop(data))
print(data)

copy = data[:]
print(copy.pop(0))

print(data)
print(copy)

heapq.heappush(data, 2)
heapq.heappush(data, 19)
heapq.heappush(data, 21)

heapq._heapify_max(data)
print(heapq._heappop_max(data))

print(data)

l1 = [10,20,30,40,50]
l2 = [15,25,35,45,55]

l3 = heapq.merge(l1, l2)

print(list(l3))