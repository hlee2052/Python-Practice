from collections import Counter

'''
#############
Python Counter
#############
'''

'''
initializations
'''

p = "donkeyduck"
pCounter = Counter(p[:len(p)-1])


word = "pen pineapple apple pen"

counter = Counter(word)
print(counter) #notice " " is also a key

counter = Counter(cat = 4, dog = 2)
print(counter)
'''
Addition and subtraction
'''
alphabets = "aaaaabbbb" # a:5, b:4
subAlphabets = "aaabc" # a:3, b:1, c:1

alphabets = Counter(alphabets)
subAlphabets = Counter(subAlphabets)

subtraction = alphabets - subAlphabets

# The following will update alphabets
#alphabets.subtract(subAlphabets)


print(subtraction) # a:2, b:3
addition = alphabets + subAlphabets
print(addition)  # 'a': 8, 'b': 5, 'c': 1


'''
Delete
'''
animalCounts = Counter({'dog':4, 'cat':12, 'buffalo':50})
del animalCounts['buffalo'] # delete entry from counter
print(animalCounts)


