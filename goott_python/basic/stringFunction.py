print()

...
# 문자열 내장 함수 : 문자열 자료형이 자체적으로 가진 함수
# 사용 : 문자열 변수 이름 뒤에 dot(.)을 붙인 다음 적절한 함수 이름을 호출
...

# 문자 개수 세기 : count
str = 'apple'
#print(str.count)

print(str.count('p'))


# 위치 알려주기 : find
str = '오늘은 화요일, 내일은 수요일'
print(str.find('내일은'))


...
# 찾는 문자의 첫번째 글자가 처음으로 나온 위치를 반환
# 문자열이므로 인덱스 번호임에 유의
...

print(str.find('금요일'))
# 찾는 문자나 문자열이 존재하지 않으면 -1을 반환

#index와 find 차이점: index() 는 찾고자 하는 문자가 없으면 에러를 발생시킴

print('----------------------------------------------')
# 문자열 삽입 : join
str1 = ','
str2 = 'abcdefg'
print(str1.join(str2)) # 문자열의 각각의 문자 사이에 지정된 값(.)를 각각 삽입

print('------------------------------------------------')

# 소문자를 대문자로 바꾸기
str='hello python'
print(str.upper())

# 대문자를 소문자로 바꾸기 : lower
str = 'Hello PYTHON'
print(str.lower())


print('--------------------------------------------------')

# 공백 지우기 : strip
# 왼쪽 공백 지우기 : lstrip
str = '    hello.'
print(str.lstrip())

#오른쪽 공백 지우기 : rstrip
print(str.rstrip())

# 양쪽 공백 지우기 : strip
print(str.strip())

print('---------------------------------------')
# 문자열 바꾸기 : replace
str = 'today is month'
str_mod = str.replace('month','sat')
print(str_mod)
# 문자열 나누기 : split
str = '오늘은 화요일, 내일은 수요일'
print(str.split()) # 구분자가 없으면 공백을 기준으로 문자열을 나눠줌
print(str.split(','))


# 실습 - 아이디만 추출해보세요
email = 'goottacademy@goott.co.kr'
print(email.split('@'))
at = email.find('@')
print(email[0:at])
