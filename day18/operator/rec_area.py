#사각형의 넓이를 계산하는 프로그램
#변수 이름 -width, height
#입력 받아서 계산
'''
width = int(input("첫째 수 입력 : "))
height = int(input("두째 수 입력 : "))

area = width * height

print("가로의 길이 : ", width,"cm")
print("세로의 길이 : ", height,"cm")
print(width * height)
          
'''

width = int(input("가로의 길이 : "))
height = int(input("세로의 길이 : "))

area = width * height

print("가로의 길이 : "+ str(width) +"cm")
print("세로의 길이 : "+ str(height) +"cm")
print("면적 : "+ str(area) +"cm")

