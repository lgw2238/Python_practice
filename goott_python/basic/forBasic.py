'''
# 반복문
# for 반복문
for 변수 in range() :
    수행해야할 문장 1
    수행해야할 문장 2
    .
    .

'''

# range():숫자 리스트를 자동으로 만들어 주는 함수
list = range(10)
print(list)  # 0부터 10 미만의 정수를 자동으로 생성

# 시작, 끝 숫자를 지정하려면 콤마로 구분
list = range(1,11)
print(list)

# 끝 숫자가 미만임에 유의
for i in range(1,11) :
    print('for 반복문', i)

print('---------------------------')
for i in range(1, 10) :
    print(i, ' 번째 ', '3 * ', i, ' = ', (3*i))

print('--------------------------')

# 사용자로부터 숫자를 하나 입력받아 해당 구구단을 출력 - 5단

dan = input('숫자를 입력해주세요 :')
print(dan)

list= int(dan)

for i in range(1,10) :
    print(dan, ' * ', i , ' = ' , list*i)

# 다중반복문
# 19단 출력
for dan in range(2, 20) :
    for j in range(1, 20):
        print(dan, ' * ', i , ' = ' , (dan*i))
    print()

print('-----------------------------------------')
# 1 ~ 16까지 짝수 출력
for i in range(1, 17):
    if i%2==0 :
        print(i)

print('----------------------------------')
# 1부터 10까지 출력 - 옆으로 출력
for i in range(1, 11):
    print(i, end=" ") # end : 입력 인수

print('\n')
print('------------------------------------')

# 1부터 10까지의 합을 출력

#list=range(10)
sum = 0
for i in range(1, 11) :
    sum += i
print(sum)

