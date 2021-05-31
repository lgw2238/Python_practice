print()
'''
#형식
for pattern in patterns :
    print(pattern)


#for in : in 뒤에 쓰인 리스트 크기에 관계없이 항상 모든 리스트에 대해 코드를 실행할 수 있음
'''
scissors = ['가위','바위','보','보','가위','바위','보']

for scissor in scissors:
    print(scissor)
print('-----------------------------')
# 1,2,3,4,5 를 출력
list = [1,2,3,4,5]

print('----------------------------------')
# 1부터 100까지 출력
for i in range(100):
    print(i)
'''
#for in list : 이미 내가 사용할 값이 정해져 있고, 그 목록에서 값을 하나씩 꺼내서 쓰기만 하면 될 때 유용
#for in range : 횟수가 정해져 있거나 1씩 증가하는 숫자를 써야 할 때 유용


'''
print('----------------------------------')

names = ['봄','여름','가을','겨울']
# 각 계절에 숫자를 붙이기
for i in range(4):
    name = names[i]
    print('{}번 : {}'.format(i+1,name))
print('----------------------------------')
# 그러나 뜻하지 않게 계절이 늘어났다고 가정
names = ['봄','여름','가을','겨울','봄봄']
for i in range(5):
    name = names[i]
    print('{}번 : {}'.format(i + 1, name))
print('----------------------------------')
# 데이터가 변동이 있을 경우 이에 따라 range()에 숫자를 변경하는 것은 불편
# len()
for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i + 1, name))

print('----------------------------------')
# enumrate : 순서와 리스트 안의 값을 한번에 처리 할 수 있도록 해주는 함수

#for i, name in enumerate(names) :
# print('{}번' :{}.format(i+1, name))


