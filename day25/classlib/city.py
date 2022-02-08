# City 클래스 생성

class City:
    a=['Seoul', 'Incheon', 'Daejeon', 'Jeju', 'Dokdo']

str1 = ''
for c in City.a:
    #print(c)
    #print(c[0])
    str1 += c[0]

print(str1)