list = []


print('------------------------------------')

# text = 'abc'
#
# number = int(text)
#
# print(number)

print('------------------------------------')

'''
[예외처리]
- 예외 : 프로그램에서 벌어지는 예외적인 상황(에러)을 의미
- ex) FileNotFoundError(파일이 없을 때)
      ZeroDivisionError(숫자를 0으로 나눌 때 에러)
      IndexError(리스트에서 얻어 올 수 없는 값일 경우 에러)
      SyntaxError(구문 오류)
      EOFError(파일의 끝일 경우, 읽을 내용이 없는 경우)
      ValueError(캐스팅 오류, type error)
      TypeError
      ...
      
 -기본 형식
 try:
    <수행 명령>
except [발생에러[as 에러메시지 변수]] :
    <수행 명령>      
      
'''
text = '100%'

try :
    number = int(text)
except ValueError:
    print('{} 는 숫자가 아닙니다.'.format(text))


print('-----------------------------------------------------')
def pop(list, index):
    try:
        print(list.pop(index))
        print(list)
    except IndexError:
        print('{} index 값이 없습니다.'.format(index))

pop([1,2,3],1)
pop([1,2,3], 4) # 에러 처리

print('-----------------------------------------------------')
# 위 pop과 같은 결과를 얻고 싶으나, try~exception이 없다면 ? if구문으로도 해결 가능
def list_pop(list,index):
    if index < len(list):
        print(list.pop(index))
        print(list)
    else:
        print('{} index 값이 없습니다.'.format(index))

list_pop([1,2,3], 1)
list_pop([1,2,3], 5)
print('-----------------------------------------------------')
# try :
#     str = input('문자를 입력하세요 :   ')
#     print('try :' + str)
# except EOFError:
#     print('읽은 내용이 없습니다.')
# except KeyboardInterrupt:
#     print('입력 취소되었습니다.')
# else:
#     print('except가 아닌 나머지 -{}'.format(str))
# print('-----------------------------------------------------')
# try:
#     str = input('문자를 입력하세요 :   ')
#     print('try :' + str)
# except EOFError:
#     print('읽은 내용이 없습니다.')
# except KeyboardInterrupt:
#      print('입력 취소되었습니다.')
# else:
#     print('except가 아닌 나머지 -{}'.format(str))
# finally:
#     print('try-else 아닌 나머지? - {}'.format(str))

print('------------------------------------------------')
# pass 구문 : 특정 에러가 발생할 경우 통과시키기 위한 구문
try:
    f = open('nofile.txt','r')
except FileNotFoundError:
    pass
    print('에러없이 수행되었음')




