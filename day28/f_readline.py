
# 파일 읽기
f = open("c:/pyfile/season.txt", 'r')
#season = f.read()
#print(season)
count = 0
while True:
    line = f.readline()
    if not line:        #Line 이 없으면
        break
    count += 1
    print(line, end='')


print(count)
f.close()