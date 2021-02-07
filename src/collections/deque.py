from collections import deque


'''
#######
Deque
#######

Note:

append(x)
appendleft(x)
clear()
copy()
count(x) == len(x)


pop()  #right side
popleft() # leftside

remove(x) # if not found, exception

reverse()

extend(iterable)
extendLeft(iterable)

'''

arr = deque()
arr.append(None)
val = arr.popleft()

print(val) ## possible to deque a None value
#deque.popleft() CANNOT pop an empty deque

first = deque([1,2,3,4])
second = [5,6,7,8]

first.extend(second)
print(first) #[1,2,3,4,5,6,7,8]


'''
note: extendleft will append items in reverse order of 'second' array
'''
first = deque([1,2,3,4])
second = [5,6,7,8]
first.extendleft(second)
print(first) # [8,7,6,5   1,2,3,4]


'''
Tree Example
'''

def buildTree():
    root = Node(5)
    node_3 = Node(3)
    node_10 = Node(10)
    node_4 = Node(4)
    node_7 = Node(7)
    node_12 = Node(12)

    root.left = node_3
    root.right = node_10
    node_3.left = node_4
    node_3.right = node_7
    node_10.right = node_12

    return root


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
       5
   3      10 
 4  7        12

'''
root = buildTree()
queue = deque([root])

level = 0
result = []
while queue:
    numSize = len(queue)
    currLevel = []
    for i in range(numSize):
        currNode = queue.popleft()
        currLevel.append(currNode.val)
        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)
    result.append(currLevel)
    level += 1
print(result)