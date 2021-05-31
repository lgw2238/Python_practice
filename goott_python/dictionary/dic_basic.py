print()
'''
# dictionary
: {name1 : value1, name2 : value2, ...}
'''

wager = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'

}
print(wager['보'])

# 가위, 바위, 보 승패판정 함수 생성해보세요
def rsp(x,y) : # 내가 낸 것은 x, 남이 낸 것은 y

    if x == y :
        return '비김'
    elif wager[x] == y:
        return '이김'
    else:
        return '졌음'

result = rsp('가위','보')
print(result)
print('----------------------------------------------------------')
# name에는 리스트를 사용할 수 없지만 값에는 리스트를 사용할 수 있다.
dic = {
    'tag' : [1,2,3]

}
print(dic)




print('----------------------------------------------------------')
import random
# while True:
#     user=input("가위바위보를 하세요:")
#     if user=='가위':
#         if random.choice(["가위","바위","보"])=="가위":
#             print("무승부")
#         elif random.choice(["가위","바위","보"])=="바위":
#             print("패")
#         else:
#             print("승")
#     if user=='바위':
#         if random.choice(["가위","바위","보"])=="가위":
#             print("승")
#         elif random.choice(["가위","바위","보"])=="바위":
#             print("무승부")
#         else:
#             print("패")
#     if user=='보':
#         if random.choice(["가위","바위","보"])=="가위":
#             print("패")
#         elif random.choice(["가위","바위","보"])=="바위":
#             print("승")
#         else:
#             print("무승부")
print('----------------------------------------------------------')

