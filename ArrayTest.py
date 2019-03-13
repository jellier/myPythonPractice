# Array 常用方法
# array.count(x)---Return the number of occurrences of x in the array.
# array.index(x)---Return the smallest i such that i is the index of the first occurrence of x in the array.
# array.sort() --- 排序
# array.reverse()--- Reverse the order of the items in the array.
# array.pop(i) --- Removes the item with the index i from the array and returns it.
# array.remove(x)--- Remove the first occurrence of x from the array.

testIntArray = [11, 77, 22, 33, 44, 44, 55, 66]
# print(testIntArray.count(33)) # return 1
print(testIntArray.count(44))  # return 2

print(testIntArray.index(11))  # return 0
testIntArray.sort()  # [11, 22, 33, 44, 44, 55, 66, 77]
print(testIntArray)
testIntArray.reverse()
print(testIntArray)   # [77, 66, 55, 44, 44, 33, 22, 11]
testIntArray.pop(0)
print(testIntArray)
testIntArray.remove(33)
print(testIntArray)
