print()
# 1부터 사용자가 입력한 숫자까지만 출력 (단, 1000이하)
'''
for i in range(1, 100) :
    print(i)

# 숫자를 입력하세요. (1000이하의 숫자)
value=input('숫자를 입력하세요 (단, 1000이하) :')
num = int(value)

for i in range(1, num+1) :
    if i >= num+1:
        break
    print(i)
'''

print('-----------------------------------------')
# break : break 붙어 있는 가장 가까운 반복문을 탈출
# continue : 이번만 생략
for i in range(1, 5) :
    for j in range(1, 5) :
        if(i==j) :
            #break # 그 조건에 일치하는 경우가 나왔을때 부터 잘림
            continue   # 그 조건에 일치하는 경우만 생략한다
        print(i, ' : ' , j)
