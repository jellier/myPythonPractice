# Array 常用方法
# array.count(x)---Return the number of occurrences of x in the array.
# array.index(x)---Return the smallest i such that i is the index of the first occurrence of x in the array.
# array.sort() --- 排序
# array.reverse()--- Reverse the order of the items in the array.
# array.pop(i) --- Removes the item with the index i from the array and returns it.
# array.remove(x)--- Remove the first occurrence of x from the array.

testIntArray = [11, 77, 22, 33, 44, 44, 55, 66]
# print(testIntArray.count(33)) # return 1
# print(testIntArray.count(44))  # return 2
#
# print(testIntArray.index(11))  # return 0
# testIntArray.sort()  # [11, 22, 33, 44, 44, 55, 66, 77]
# print(testIntArray)
# testIntArray.reverse()
# print(testIntArray)   # [77, 66, 55, 44, 44, 33, 22, 11]
# testIntArray.pop(0)
# print(testIntArray)
# testIntArray.remove(33)
# print(testIntArray)

# # practise
# # 让用户输入3个名字，放到一个列表中
# nameArray = []
# print("Please input 3 names :")
# for i in range(3):
#     tip= "第" + str(i+1) + "个："
#     name = input(tip)
#     nameArray.append(name)
# # 然后打印出来
# print(nameArray)
#
# # 显示排序后的列表
# newArray= sorted(nameArray)
# print('The sorted names are : %s ' % newArray)
#
# # 让用户选择一个名字，并输入一个新名字替换掉
# target = input("Please choose one name you want to change.Which one?")
# if target in nameArray:
#     # 得到要删除元素的位置
#     # a.index(target), 其中a是目标list，target是需要的下标对应的值。
#     replaceIndex = (nameArray.index(target))
#     # remove()会从
#     nameArray.remove(target)
#
#     newOne = input('Please input the new name: ')
#     nameArray.insert(replaceIndex,newOne)
#
# print(nameArray)

print('======================================================')
# # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# print(list(enumerate( nameArray)))

# 打印一个列表的元素和索引值
# 普通for 循环方法：
seqList = ["Amy", "Tom", "Sam","Tod"]
i = 0
for elem in seqList:
    print('%s %s' %(i, elem))
    i+=1

for j,elem in enumerate(seqList):
    print(j,elem)
