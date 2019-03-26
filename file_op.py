#对文件的操作
# # mode = 'w' 代表写入，会覆盖原有的内容，如果是追加，使用'a'
# file1 = open('testFile.txt', 'w')
# file1.write('王葫芦')
# file1.close()
#
# # 把刚刚写入的文件读取出来
# file2 = open('testFile.txt', 'r')
# print(file2.read())
# file2.close()

# 给文件追加内容
file3 = open('testFile.txt', 'w')
file3.write('王小林')
# 如何在'a'模式下使用read?
# print(file3.read())   w或a模式下不可read,读写模式不可同时存在

# 将文件逐行打印需要使用下面的循环
# for line in file3:
#     print(line, end='')

file3.close()

# seek的使用
# seek的参数，第一个代表偏移量，第二个可使用0、1、2。0代表从头开始，1代表从当前指针开始，2代表从结尾开始
file4 = open('testFile.txt','rb+')
file4.write(b'0123456789abcdef')
print(file4.seek(4))
print(file4.seek(-8,2))
