# 문자형(열) : 문자, 단어 등으로 구성된 문자들의 집합

# 문자열 만드는 방법
#1. 큰 따옴표로 둘러싸기
string1 = "Hello Python"

#2. 작은 따옴표로 둘러싸기
string2 = "Hello Python2"

#3. 큰 따옴표 3개로 둘러싸기
string3 = """ Funny Python """

#4. 작은 따옴표 3개로 둘러싸기
string4 = ''' Funny Python2 '''

print(string1, string2, string3, string4)

# 문자열 안에 작은 따옴표, 큰 따옴표를 모두 출력하고 싶다면

# print('Jack's favorite food is burger') #systax error
print("Jack's favorite food is burger")


#print("많이 생각하는 모든 것들은 문제가 된다." - "프리드리히 니체") #systax error
print('"많이 생각하는 모든 것들은 문제가 된다." - "프리드리히 니체"')


# 특별한 의미를 가진 이스케이프 코드 : 미리 정의해둔 문자 조합 
# \n : 개행(줄바꿈), \t : tab, \\ : \ 출력, \b : backspace,

# " 많이 생각하는 모든 것들은 문제가 된다."
# "프리드리히 니체"
print(' " 많이 생각하는 모든 것들은 문제가 된다. " \n " 프리드리히 니체 " ')

print('-------------------------------------')
#문자열 연산 - 사람 (개발자) 생각을 그대로 반영해주는 파이썬의 장점

# 문자열 더해서 연결하기 (concatenation)
head = 'Python'

body = 'wow'

tail = 'fantastic'

print(head + body + tail) #+: 연결 연산자

# 문자열을 반복
name = '홍길동'
print(name*2) # * : 반복하라는 의미

# 실습 - 다음처럼 출력해보세요

''' 
===============================
이것이 파이썬 
================================
'''

print('='*30)
print('이것이 파이선')
print('='*30)

print('------------------------------------------------')
print('=========================== \n 이것이 파이썬 \n===========================')\
    
