import datetime

# print(datetime.date.today())

print('-----------------------------------')
import calendar
# print(calendar.calendar(2021))

'''
# calendar 모듈 : 파이선에서 달력을 표시해주는 모듈
calendar.calendar(해당 년도) : 해당년도의 전체 달력을 출력
calendar.prcal(해당 년도): 해당년도의 전체 달력을 출력
calendar.prmonth(년도, 월) : 해당년도의 월만 출력
calendar.weekday(년도, 월, 일) : 입력받은 날짜의 요일을 반환
calendar.monthrange(년도, 월 ) : 입력받은 달의 1일이 무슨 요일인지를 출력하고
                                그 달의 마지막 일자를 반환 (튜플로 반환)
                                
'''
#calendar.calendar(2021)
#calendar.prcal(2021)
#calendar.prmonth(2021, 8)
#print(calendar.weekday(2021,4,14))
#print(calendar.monthrange(2021, 4))

print('-------------------------------------------------')
import random #난수 발생 모듈
print(random.random()) # 0.0 ~ 1.0 사이의 실수 값
#
# for i in range(10):
#     print(random.random())

print('-------------------------------------------------')
import webbrowser
import urllib.request


# webbrowser : 자신의 시스템에서 사용하는 기본 웹브라우저가 자동으로 실행되게 하는 모듈
# webbrowser.open("http:/example.com")
# webbrowser.open_new_tab('http:/example.com')
#
# def web_info(url):
#     result = urllib.request.urlopen(url)
#     data = result.read()
#     encode = data.decode('utf-8')
#     return encode
#
# url = input('웹페에지 주소를 입력하세요 :')
# context = web_info(url)
# print(context)





