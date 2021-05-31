str = '어떤 관계는 싸움으로 시작해… 하지만, 보통 로맨틱 코미디 영화에서나 그렇지. 인생은 영화가 아니야.'

print(str)

print(str[5]) # str 의 [] 번째에있는 글씨를 출력해줌.
#
# 문자열 인덱싱(색인 연산) : 문자를 배열에 담아서 번호를 부여한 것
# 인덱스는 0 부터 시작함에 유의!

print(str[10])

# 글자 가장 마지막에 나오는 걸 출력해보세요.
print(str[54])
#
# 파이선의 특별한 기능 : 문자를 뒤에서부터 읽어 올 수 있음
print(str[-2])

# 글자 '싸움으로' 를 출력해보세요
print(str[7]+str[8]+str[9]+str[10])
print('---------------------------')
print(str[7:11]) # 문자열 슬라이싱 기법 : 처음자리수 부터 <= 변수 < 끝자리수
print(str[0:3]) # 공백도 출력되고 있음에 유의
# ' 모든 ' 과 ' 모든  '은 엄연히 다른 문자이니 유의!
#끝번호를 생략하면 그 문자열의 끝까지 돌려줌
print(str[0:])

#반대로 시작번호를 생략하면 문자열의 처음부터 지정한 끝번호자리까지 return
print(str[:11])

#시작번호, 끝번호를 모두 생략
print(str[:])

#인덱싱과 마찬가지로 - 기호 사용 가능 ( 앞에서 11 부터 뒤에서 앞으로 7번째까지 )
print(str[11: -7])


# 실습
hiredate = '20210412MON'

# year, date, day 로 구분하여 출력하세요
year = hiredate[:4]
date = hiredate[4:-3]
day = hiredate[8:]
print(year + ' : ' + date + ' : ' + day)
print('year',hiredate[:4]) + print('date',hiredate[4:-3]) + print('day', hiredate[8:])