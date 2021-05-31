print()
'''
# 파이썬 논리값 : True, False
# 파이썬에서는 True와 False로 최종 평가할 수 있는 것은 모두 논리 연산으로 쓸 수 있음
# 최종평가 확인은 bool()에 값을 넣어 호출해보면 확인할 수 있다
'''

# 숫자 확인
print(bool(0), bool(1), bool(-1), bool(-2384))

# 0만 false이고 나머지는 True로 평가

print('---------------------------------------------')

# 리스트 확인
# 비어있는 리스트는 False로 평가
# 채워져있는 (값이 하나라도 있는) 리스트는 True로 평가
print(bool([]), bool([3]), bool([-1]))

print('---------------------------------------------')

# 딕셔너리
# 비어있는 딕셔너리는 False로 평가
# 채워져있는 (값이 하나라도 있는) 딕셔너리는 True로 평가
print(bool({}), bool({'key1', 'value1'}))

print('---------------------------------------------')

# 문자열
# 비어있는 문자열은 False로 평가
# 채워져있는 (값이 하나라도 있는) 문자열은 True로 평가
print(bool(None), bool(''), bool('hihi'))

print('---------------------------------------------')
# 최종평가 특성을 이용하는 예
if 'hihi' :
    print('hello')

if '' :
    print('None')

print('---------------------------------------------')

if '':
    print('None')

print('---------------------------------------')
if []:
    print('[] is True') # NO
if [1,2,3]:
    print('true')       # YES
if {}:
    print('True')       # NO
if {'key1', 'value1'}:
    print('True')       # YES
if 0 :
    print('True')       # NO
if 1:
    print('True')       # YES

print('-------------------------------------')

value = input('입력하세요 : ') and '입력하지 않으셨습니다'

print('입력값 : ' + value)

print('-------------------------------------')

value = input('입력하세요 : ') or '입력하지 않으셨습니다'

print('입력값 : ' + value)






