#Q5

f1 = open("./output/test2.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("./output/test2.txt", 'r')
print(f2.read())
f2.close()


#Q6
"""
user_input = input("저장할 내용을 입력하세요 : ")
f = open("./output/test3.txt", 'a')
f.write(user_input)
f.write('\n')
f.close()
"""

#Q7
"""
with open("./output/test4.txt", 'w') as f:
    f.write("Life is too short\n you need java")

with open("./output/test4.txt", 'r') as f:
    body = f.read()

    body = body.replace("java", "python")
    print(body)

with open("./output/test4.txt", 'w') as f:
    f.write(body)
"""
