
'''
List

'''

list = ['a', 'b', 'c', 'd', 'e']

print(list[-1]) # e

print(list[:-1]) # [a b c d]
print(list[:-2]) # [a b c]


print(list[:0]) # []
print(list[:1]) #a
print(list[:2]) #ab

print(list[:-100]) # []
print(list[:100]) # [a,b,c,d,e]