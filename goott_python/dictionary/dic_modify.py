
# 리스트
list= [0,1,2,3,4]

print(list)
# 3번째

list[2] =33
print(list)

# # 리스트에 새로운 값을 추가
# list[5] = 6 - 없는 인덱스에 값을 추가하면 오류
# print(list)


# append()
list.append(6)
print(list)


print('---------------------------------------------------------------------')
# 딕셔너리
dict= {'one':1, 'two':2, 'three':3}
print(dict)


# 수정 - 리스트와 비슷(다만, 인덱스가 아닌 이름을 호출해서 수정)
dict['two'] = 22

print(dict)

# 새로운 값을 추가
dict['four']=4
print(dict)

# 삭제
del(list[0])
print(list)


del(dict['one'])
print(dict)

#pop() - 삭제하면서 값을 반환해주고 있음

list.pop(0)
print(list)

dict.pop('two')
print(dict)
