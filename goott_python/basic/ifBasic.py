print()
'''
# 조건문 (분기문)
if 조건 :
    수행할 문장 1
    수행할 문장 2
    .
    .
'''

people = 1

if people:
    print('사람이 한 명 들어있어요')

'''
# 들여쓰기 중요: 코드 블록을 구분해 주는 역할
# 탭, 스페이스바 4칸을 이용하여 들여쓰기 수행하면 됨 (cf.python 2.x라면 혼용 안됨)
'''

if people:
    print('사람이 한 명 있습니다')
    # print('사람이 두 명 들어있을지도 몰라요')

# 조건 참 / 거짓을 구분 할 때는 연산자(비교, 논리) 사용

# 비교연산자
x = 3
y = 2

if x != y:
    print('x와  y는 같지 않다')

'''
# 블록  - 콜론(:) 다음에 들여쓴 코드 블록
        - 같은 실행 흐름에서 순서대로 실행되는 코드 덩어리
        - 여러 줄로 작성이 가능. 단, 여러 줄일 경우 들여쓰기 칸 수가 모두 같아야 함!
'''

# 논리 연산자 : True, False
if True:
    print('블록 코드')
    print('같은 블록')
    print('여러 줄 가능')

'''
# 블록을 끝내려면 들여쓰기를 끝내줘야 함 - 내어쓰기
# 한번이라도 내어 쓴 블록은 끝난 블록이 되고, 다시 열 수 없습니다.     
'''
print('-------------------------------')
print('바깥에 있는 코드')

if True:
    print('첫번째 블록 코드')
    # 블록 안에는 또 다른 블록이 들어갈 수 있음
    if False :
        print('실행되지 않을 코드')
    if True :
        print('첫번째 - 안쪽 블록 코드')

    print('첫번째 블록 끝 코드')
print('바깥 코드')

print('------------------------------------------------------')
if False:
    print('첫번째 블록 코드')

    if False:
        print('실행되지 않을 코드')

    if True:
        print('첫번째-안쪽 블록 코드')

    print('첫번째 블록 끝 코드')
print('바깥코드')

print('-------------------------------')
'''
# 분기
if <조건> :
    <코드 블록>
else :
    <코드 블록>

# 조건이 True이면 if 코드 블록을 실행
# 조건이 False이면 else 코드 블록을 실행
'''

num1 = 50
num2 = 100

# 둘 중 큰 수 구하기 
if num1>num2 :
    big =num1
    print(big)
else :
    big = num2
    print(big)

# 절대값 구하기
if num1>num2 :
    dif = num1-num2
    print(big1)
else :
    dif = num2-num1
    print(dif)

