print()
'''
# 튜플을 이용해서 변수 하나에 여러 값을 여러 개 대입할 수 있음
# 패킹 - 하나의 변수에 여러 개의 값을 대입
# 언패킹 - 패킹된 변수에서 여러 개의 값을 꺼내오는 것

'''


a, b = 1, 2
print(a,b) # 튜플이 이루어진 상태 : a = 1, b = 2

c = (3, 4) # 변수 c에 튜플로 3, 4 를 대입

print(c)
#언패킹
d, e = c # 변수 d와 e에 c를 각각 대입

print(d,e) # c를 언패킹해서 d와 e 에 대입했다.

# 패킹
f = d, e

print(f) # 변수 d, e 를 f에 패킹했다.

print('----------------------------------------------------')
# 데이터 맞바꿈
x = 5

y = 10

temp = x # x 값을 temp라는 변수를 만들어서 하나 만들어주면 x = y , y= temp 성립

x = y
y = temp
print(x,y)

print('----------------------------------------------------')
# 튜플로 맞바꿈
x, y = y, x

print(x,y)
print('----------------------------------------------------')
# 여러 개의 값을 반환할 때 유용
def tulple_fun():
    return 1, 2

num1, num2 = tulple_fun()
print(num1, num2)
print(type(tulple_fun()))

print('----------------------------------------------------')
list = [1,2,3,4,5]  # 기본적으로 리스트와 튜플은 비슷함 순서와 값을 가지고 있음
for i, v in enumerate(list):
    print('{}번째 값 : {}'.format(i, v))

# 튜플로 인식
for j in enumerate(list):   # 하나의 값을 받기 위해서는 tuple로 작업해야함.
    print('{}번째 값 : {}'.format(j[0],j[1]))

print('-------------------------------------------------------')
for k in enumerate(list):
    print('{}번째 값: {}'.format(*k))
print('-------------------------------------------------------')
# 딕셔너리
result = {'java':100, 'jsp':80, 'spring':80}

for key, value in result.items():
    print('{} 과목 점수는 {} 입니다.'.format(key,value))
print('-------------------------------------------------------')
for i in result.items(): # tuple : 인덱스와 값을 고정
    print('{} 과목 점수는 {} 입니다.'.format(i[0],i[1]))
print('-------------------------------------------------------')
for i in result.items():
    print('{} 과목 점수는 {} 입니다.'.format(*i))













