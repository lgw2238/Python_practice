print()
'''
#함수
# : 코드 조각에 기능별로 이름을 붙인 것으로 해당 기능을 쉽게 쓸 수 있도록 도와주는 역할
# : 반복되는 부분이 있을 경우, 추후에 호출될 가능성이 있을 경우 새엇ㅇ

'''
'''
#함수 구조 - 결과값이 없는 함수
def 함수명(입력 인수): #def (define 약자)
    <수행할 문장1>
    <수행할 문장2>
    ...

'''

def function():
    print('Hello Python Function')

function()

print('--------------------------------')
# 입력값이 없는 함수 - 매개변수 없는 함수

a=10
b=20
def sum():
    result = a + b
    print(result)

sum()

# c 와 d를 더하는 sum 함수를 만들어서 결과를 출력해보세요
c=20
d=30
def sum2():
    result = c + d
    print(result)
sum2()

'''
# 함수 구조 2 - 결과 값이 있는 함수 (return)
def 함수이름 (입력인수) :
    <수행 할 문장> ...
    return 결과값 
'''

# 결과값이 있는 매개 변수가 없는 함수
def hello():
    return 'hi python function'

# 결과값을 받을 변수 = 함수명 ()
hello = hello()
print(hello)

# 매개 변수가 있는 결과값이 있는 함수
e = 100
f = 200
def add(e,f):
    result = e+f
    return result

add = add(e,f)
print(add)

# 실습 : 3000만원 연봉을 받는 신입사원 연봉을 10% 인상한 값으로 돌려주는 함수를 생성해서 구현해보세요
annual = 30000000

def upsal(annual):
    return annual*1.10

unannual = upsal(annual)
print(unannual)

print('-----------------------------------')
# return을 이용해서 어떤 상황이 되어서 함수를 빠져나가고자 할 때도 자주 쓰임
def return_a():
    for i in range(100):
        return i
result = return_a()
print(result) # return 구문은 오직 한개의 객체만 반환하도록 설계되어 있음

print('-------------------------------------')

def avoid(num) :
    if num == 5 :
        return
    print(num)
avoid(10)
avoid(5)