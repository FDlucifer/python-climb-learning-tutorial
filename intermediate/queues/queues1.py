import queue

#q = queue.LifoQueue()
q = queue.PriorityQueue()

numbers = [1,2,3,4,5,6,7]
for x in numbers:
    q.put(x)

print(q.get())
print(q.get())
print(q.get())
print(q.get())