'''
bigO for arrays (data structures)
lookup O(1)
push O(1)
insert O(n)
delete O(n)
'''

# Python Lists are Dynamic Arrays
strings = ['a', 'b', 'c', 'd']
# 4*4 = 16 bytes of storage

strings[2] # O(1)

# push
strings.append('e') # O(1), can be O(n)

# pop
strings.pop() # O(1)
strings.pop() # O(1)

# unshift/insert
strings.insert(0, 'x') # O(n)

# insert/splice
strings.insert(2, 'alien') # O(n)

print(strings)

# creating my own array
# class MyArray:
#     def __init__(self, length, data):
#         self.length = length
#         self.data = data
#
#
# newArray = MyArray()
# print(newArray)


''' Reversing a string in python '''

string = "Hi my name is Kyle"

print(string[::-1])

x = "Reverse a string in Python without using str.reverse()"
print("".join([x[j] for j in range(len(x)-1, -1, -1)]))
print(x[::-1])


''' MERGING TWO ARRAYS '''


def merge_sorted_arrays(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1


print(merge_sorted_arrays([0, 3, 4, 31], [3, 4, 6, 30]))

joinedlist = [0, 3, 4, 31] + [3, 4, 6, 30]
joinedlist.sort()
print(joinedlist)


