print()

list1 = list(range(20))

print(list1)

# 5 ~ 15 까지 출력
print(list1[5:16])

print('----------------------------------------------------')

# 값을 건너뛰면서 가져오려면? step
# 시작 : 끝 : step
print(list1[5:16:2])
print(list1[5:18:3])

print('----------------------------------------------------')

# 실습 : list1 이 5, 8, 11, 14 값을 가지도록 슬라이스 하시오
print(list1[5:15:3])

print('----------------------------------------------------')

# 실습 : list1 이 5, 9, 13, 17 값을 가지도록 슬라이스 하시오
print(list1[5:18:4])

print('----------------------------------------------------')

list2 = list(range(10))
print(list2)

print('----------------------------------------------------')

# 특정 영역값을 바꾸기
print(list2[1:3])
list2[1:3] = [55,66]
print("변경된 list2 입니다.",list2)

print('----------------------------------------------------')

# 기존 값의 개수와 바꾸려는 값의 개수가 똑같아야 하는 것은 아니다
list2[1:3] = [77, 88, 99]
print(list2)

print('----------------------------------------------------')

# 바꾸는 수는 반드시 리스트 형으로 써야 함에 유의 !!!!!!!!!! (갯수와 무관)
# list2[1:3] = 5        # 일반형으로 넣으면 에러 !!!!!!!!!
list2[1:3] = [5]
print(list2)

print('----------------------------------------------------')

list3 = list(range(5))

print(list3)

# 최종 출력 : [0, 11, 22, 33, 4]

list3[1:] = [11, 22, 33, 4]
print(list3)


