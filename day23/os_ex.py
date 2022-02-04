#os 모듈 - 환병변수나 디렉터리, 파일 등의 OS 자원들 제어하는 모듈

import os

os.chdir('c:/pyworks/day20')  #경로 이동

dir = os.popen('dir')         #dir 명령 실행 popen = 프로그램오픈(program open)

print(dir.read())