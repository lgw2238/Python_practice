import math

# 둘레 구하기 : r * 2 * 3.14
r = 10

print(r * 2 * math.pi)

# 올림 : ceil
print(math.ceil(2.4))

# 내림 : floor
print(math.floor(4.7))
# 반올림
#print(math.round(3.5))
print(round(3.5)) # round() : 자주 사용하는 함수여서 내장함수에 있음

# 이 밖에도 삼각함수, 지수, 승, 로그 등 다양한 기능이 math에 있음

print('------------------------------------------')
import sys

print(sys.argv) # 해당 파이썬 파일 경로를 보여줌
print(sys.path) # 어디서 작업하고 있는지 보여줌

print('------------------------------------------')
import os
# 시스템의 환경변수값 확인 - 시스템의 정보를 딕셔너리 객체로 리턴
print(os.environ)

# 환경변수 -인덱싱
print(os.environ['Path'])

# 현재 위치 확인
print(os.getcwd())


# 디렉토리 변경
os.chdir('c:\\windows')
print(os.getcwd())

os.system('dir')
'''
# 그외 os 모듈
os.popen : 시스템 명령어를 수행한 결과값을 읽기모드의 파일 객체로 리턴
os.mkdir(디렉토리명) : 디렉토리 생성
os.rmdir(디렉토리명) : 디렉토리 삭제(주의 - 디렉토리가 비어있어야 함)
os.unlink(파일명) : 파일 삭제 
os.rename(src, dst) : src 이름 파일을 dst 이름으로 바꿈
'''

print('-----------------------------------------')
import shutil
'''
shutil.copy(src, dst) : src라는 이름으로 
'''

#shutil.copy('moduleEx01.py', 'moduleEx01_test.py')

print('-----------------------------------------')
import time

'''
time.time() : 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 돌려주는 함수
            : UTC (Universal Time Coordinated -  세계 협정 표준시)를 이용해서 실수 형태로 반환

time.locatime() : time.time()를 통해서 얻어온 실수값을 이용해서
                년 월 일 시 분 초 형태로 바꾸어주는 함수

>struct_time 시퀀스 객체 속성
    tm_year : 년도
    tm_mon : 월 (1~12)
    tm_mday : 일
    tm_hour : 시간 ()
    tm_min : qns
    tm_sec : 초
    tm_wday : 요일을 숫자로 표현 (월요일 :  0~ 일요일 : 6)
    tm_yday : 1월 1일부터 누적된 날짜를 나타냄(1~366)
    tm_isdst : 서머타임 (일광절약 시간에 0,1,-1)
                
                
time.gmtime: UTC 기준의 현재 시간               
 
time.asctime : 알아보기 쉬운 날짜와 시간을 반환
time.ctime : asctime 과 같음            

time.strftime : 시간을 나타내는 포맷을 짖렁해서 세밀하게 표현할 수 있는 함수
> 형식 지정자 (포멧코드)

    %y 년도 축약(2021-> 21) 
    %b 월 축약, %B
    %c 날짜와 시간을 출력 (21/01/01 13:08:00)
    %d 날(day) - 01~31
    %H 24시간 표현 - 0~23
    %I 12시간 표현 - 01 ~ 12
    %j 누적날짜를 표현 - 001 ~ 366
    %m 월 - 01~12
    %M 분 - 01 ~ 59 
    %P 오전/오후 - AM/PM
    %S 초 - 00~60
    %U 누적 주 - (일요일 시작 : 00~53)
    %w 요일 - 0~6
    %W 누적 주 - (일요일 시작 : 00~53)
    %x 날짜 출력 - 21/01/01
    %X 시간 출력 -  13/01/01
    %Z 시간대 출력 - 대한민국 표준시 
    
time.sleep : 루프문 안에서 자주 사용됨, 일정한 시간 간격을 주기 위해서 사용하는 함수    
'''

#print(time.time())

t = time.time()
print(time.localtime(t))

print(time.gmtime(t))

print(time.strftime('%Y %m %d %X'))

print(time.strftime('%Y %m %d %X', time.localtime(time.time())))

for i in range(10):
    print(i)
    time.sleep(1) #초단위 실행


