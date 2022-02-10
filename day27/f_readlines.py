# readlines() - 데이터를 리스트로 반환
# 인덱싱 또는 슬라이싱 가능

# 파일 읽기
try:
    f = open("c:/pyfile/season.txt", 'r')
    """
    #한 줄 읽기
    season = f.readline() # 리스트의 한 줄만 읽음  (행이 여러개 있을 때)여러 줄 일때만 가능
    print(season)
    """

    # 리스트로 반환
    season = f.readlines()
    print(season)   #리스트 객체 출력
    print(season[0])
    print(season[-1])
    print(season[2:])


    # 전체 요소(값) 출력
    for s in season:
        #print(s, end="")
        print(s.strip()) # 공백 제거
    f.close()
except:
    print("파일을 열 수 없습니다.")