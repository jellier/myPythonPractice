#Get a message to encode or decode
message= input("Enter a message to encode or decode: ")
#upper letter
message = message.upper()
code = ""
#print(message)
for letter in message:
    if letter.isupper():
        letter = ord(letter)+13
        # if letter > 90:  超出90则不再是字母，需将Z返回A
        # 或使用 :  
        if not chr(letter).isupper():  # 只有大写字母.isupper()返回True
            letter -=26
        newletter = chr(letter)
        code += newletter
print("out input is :" + code)
        
        
