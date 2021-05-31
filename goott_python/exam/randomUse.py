list = ['빨', '주', '노', '초', '파', '남', '보']



'''
# 1. 공식문서에서 random 모듈을 검색하여 list 중 하나를 랜덤하게 갖도록 만들어보기
# 2. 공식문서에서 random 모듈을 검색하여 random_number 가 2이상 10이하의 랜덤한 정수를 갖도록 해보기
# 3. 공식문서에서 random 모듈을 검색하여 list를 모두 섞어보세요
# 4. lotto 6자리 구현해보세요.

'''
print('---------------------------------')
#HW 01
import random

random_element = random.choice(list)
print(random_element)

print(random.choice(list))




print('---------------------------------')
#HW 02
import random
for i in range(10):
    print(random.randint(2,10))


print('---------------------------------')
#HW 03
import random
random.shuffle(list)
print(list)



print('---------------------------------')
#HW 04
import random
print(random.sample(range(1,45),6))

print('---------------------------------')
import random


print(random.randint(1,45))
print(random.randint(1,45))
print(random.randint(1,45))
print(random.randint(1,45))
print(random.randint(1,45))
print(random.randint(1,45))
print('---------------------------------')

'''
for i in range(100):
    first = math.floor(random.random()*45)
    second = math.floor(random.random()*45)

    temp = 0

    temp = rnd[first]
    rnd[first] = rnd[second]
    rnd[second] = temp

for j in range(6):
    print(rnd[j], end  = " ")
'''
lotto = []
while len(lotto) < 6 :
    num = random.randint(1,45)
    if num not in lotto:
        lotto.append(num)

lotto.sort()
print(lotto)

