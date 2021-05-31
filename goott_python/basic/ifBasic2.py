print()
'''
if<조건> :
    <코드블록>
elif <조건> :
    <코드블록>
else :
    <코드블록>
       
    
    
'''
#score = input('숫자를 입력하세요: ')
'''
value = input('숫자를 입력하세요 : ')
print(score)
'''
# 프롬프트에 알리고 입력받기
# input() 은 입력되는 모든 데이터를 문자열로 취급 %중요!
value = input('숫자를 입력하세요 : ')
print(value)

score = int(value)
# 조건(분기)문
if score >= 90 :
    print('당신의 학점은 A입니다.')
elif score >= 80 :
    print('당신의 학점은 B입니다.')
elif score >= 70 :
    print('당신의 학점은 C입니다.')
elif score >= 60 :
    print('당신의 학점은 D입니다.')
else :
    print('당신은 F')

print('---------------------------------------')
# 태어난 년도 4자리 입력받아서 화면에 당신은 ~~ 띠 입니다 출력

# 자축인묘 진사오미 신유술해
# 쥐소호토 용뱀말양 원닭개돼
# 4 5 6 7 8 9 10 11 12 1 2 3

value = input('태어난 년도를 입력해주세요 :')
print(value)

answer = int(value)

if answer % 12 == 0 :
    print('당신은 원숭이 띠 입니다.')
elif answer % 12 == 1 :
    print('당신은 닭 띠 입니다.')
elif answer % 12 == 2 :
    print('당신은 개 띠 입니다.')
elif answer % 12 == 3 :
    print('당신은 돼지 띠 입니다.')
elif answer % 12 == 4 :
    print('당신은 쥐 띠 입니다.')
elif answer % 12 == 5 :
    print('당신은 소 띠 입니다.')
elif answer % 12 == 6 :
    print('당신은 호랑이 띠 입니다.')
elif answer % 12 == 7 :
    print('당신은 토끼 띠 입니다.')
elif answer % 12 == 9 :
    print('당신은 뱀 띠 입니다.')
elif answer % 12 == 10 :
    print('당신은 용 띠 입니다.')
elif answer % 12 == 11 :
    print('당신은 말 띠 입니다.')
else :
    print("당신은 양 띠 입니다.")



