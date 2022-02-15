# try ~ except ~ else
# 에러가 없으면 try ~ else
# 에러가 있으면 trt ~ except
try:
    print("1번")
    with open("c:/pyfile/season2.txt", 'r') as f:
        season = f.readlines()
        #print(season)
except FileNotFoundError:
    print("2번")
else:
    print("3번")
    for s in season:
        print(s, end='')


