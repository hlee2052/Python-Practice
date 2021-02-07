import heapq

'''
###########
Python heap
###########
https://github.com/python/cpython/blob/3.9/Lib/heapq.py
'''

arr = [4,2,1,3,5,6,9,15]

#in-place transformation

heapq.heapify(arr)

print(arr) #[1, 2, 4, 3, 5, 6, 9, 15]

heapq.heappop(arr)
print(arr) # first element popped

heapq.heappush(arr, 100)
print(arr) # 100 added to heap

# return n largest element in reverse order
largest = heapq.nlargest(2, arr)
print(largest)  # [100, 15]

smallest = heapq.nsmallest(2, arr)
print(smallest) #[2,3]


heapq._heapify_max(arr)
print(arr) # maxheap

'''
heap on tuple
- first element is what heap order is based on
'''
class Animal():
    def __init__(self, name, numLegs, weight):
        self.numLegs = numLegs
        self.weight = weight
        self.name = name


dog = Animal('dog', 4, 120)
cat = Animal('cat', 4, 100)
spider = Animal('spider', 8, 15)
snake = Animal('snake',0, 30)
monkey = Animal('monkey', 2, 140)

animals = [dog, cat, spider, snake, monkey]

animalHeap = []
# heap based on weight
for animal in animals:
    heapq.heappush(animalHeap, (animal.weight, animal.name, animal.numLegs))

print(animalHeap)

# heap based on numLegs
animalHeap = []
for animal in animals:
    heapq.heappush(animalHeap, (animal.numLegs, animal.weight, animal.name))

print(animalHeap)
