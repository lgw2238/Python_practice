seasons = ['봄','여름','가을','겨울']


for s in seasons:
    print(s)

print('---------------------------------------------------------')
result = {'java':80, 'jsp':90, 'spring':80}
print(result)
for r in result:
    print(r)



print('---------------------------------------------------------')
# key , value 각각 호출 가능
for key in result.keys():
    print(key)

for value in result.values():
    print(value)

print('---------------------------------------------------------')
# 과목과 점수 모두를 출력 - key를 가져오는게 우선
for key in result.keys(): # 당연히 키로 불러온다는 것을 파이선도 알고 있으므로 keys()를 삭제해도 인식함
    print('{} 점수는 {} 입니다.' .format(key,result[key]))
print('---------------------------------------------------------')
# 리스트도 인덱스번호를 통해서 값을 구하는 방식 - enumrate()를 통해 두가지 정보를 처리
# 딕셔너리도 위와 같은 역할을 하는 함수가 존재 : items()
for key, value in result.items():
    print('{} 점수는 {} 입니다'.format(key,value))


'''
# 출력순서가 다를 수 있음.
# 리스트와 달리 딕셔너리는 순서를 지켜서 리턴해주지 않음 - key로 찾으므로 순서를 지킬 필요가 없음 - 무법자
# 순서가 중요한 경우라면 딕셔너리가 아닌 리스트를 사용하면 됨 
'''
