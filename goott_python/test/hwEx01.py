print
# HW 01
star = '*'
for i in range(1, 6) :
    print(star * i)
# print(star)
# print(star*2)
# print(star*3)
# print(star*4)
# print(star*5)
print('----------------------------------------')
# HW 02
for i in range(1,8):
    for j in range(1,i):
        print(j, end='')  # added end=''
    print()
print('----------------------------------------')
# HW 03 : 몇줄출력?
star = int(input('몇줄 출력하시겠습니까 ? :'))
for i in range(1, star+1) :
    print('*'*i)
print('----------------------------------------')
# HW 04 : 별을 거꾸로
for i in range(6, 0, -1):
    print('{:<5}'.format('*' * (i-1)))
print('----------------------------------------')
# HW 05 : 사용자로 부터 입력받은 값이 3의 배수인지 아닌지 출력
value = input('숫자를 입력해주세요 : ')
print(value)

third = int(value)

if third %3 == 0 :
    print('입력하신 숫자는 3의 배수입니다.')
else :
    print('입력하신 숫자는 3의 배수가 아닙니다.')
print('----------------------------------------')
# HW 06 : 두개 주사위를 던졌을때 합이 4가 되는 모든 경우의수를 출력하는 프로그램을 작성하시오.
for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        n = n1 + n2
        if n == 4 :
            print(n1, n2)
