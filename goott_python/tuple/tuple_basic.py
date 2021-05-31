print()
'''
# 튜플(tuple) : 순서가 있는 값의 집합이고 한 번 만들고 나서 변경을 최소화 하고 싶을 때 사용


'''
# 리스트는 대괄호, 딕셔너리는 중괄호, 튜플은 소괄호


tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))
print('-----------------------------------------')
# 튜플을 만들 때 핵심은 소괄호 아님. 콤마에 유의
tuple2 = 1,2,3,4,5
print(tuple2)
print(type(tuple2))

var = 1
print(type(var))

var2 = 1,
print(type(var2))

# 튜플을 리스트로도 생성 가능
list1 = [1,2,3,4,5]
tuple3 = tuple(list1)
print(tuple3)
print(type(tuple3))

# 튜플 값 가져오기
print(tuple3[0]) # 리스트처럼 인덱스번호 이용해서 인덱싱 가능

# 튜플 값 수정
#tuple3[3] = 22
# 튜플 값 삭제
#del tuple3[3]
#print(tuple3)

'''
# 튜플의 값을 변경하려고 하면 타입 TypeError가 발생함
# 투플은 순서와 값을 모두 고정하고 있기 때문에
# 수정, 삭제(del, pop) 모두 쓸 수 없음

# 이렇게 제약이 있음에도 튜플을 사용하는 이유
1) 두 변수의 값을 맞바꿀 때 사용
2) 여러 개의 값을 한꺼번에 전달하고 싶을 때
3) 딕셔너리는 key에 따라 value 를 찾아오므로 key가 매번 바뀌면 곤란
 - key에도 값을 여러개 넣고 싶다면? key를 고정할 수 있으면 가능 
'''

print('--------------------------------------')
# 튜플 출력
tuple4 = (11,22,33)
for i in tuple4:
    print(i)