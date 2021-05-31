print()

'''
# 파이선은 조건식을 사용할 때 and 연산과 or 연산을 적극적으로 활용한다.
'''

# ex) 항상 False 만을 반환하는 함수
def always_false() :
    print('언제나 False')
    return False

# ex) 항상 True 만을 반환하는 함수
def always_True() :
    print('언제나 True')
    return True

result1 = always_false()
result2 = always_True()

print(result1, result2)

if result1 and result2 :
    print(True)
else:
    print(False)

print('------------------------------')

# 변수에 담지 않고 바로 함수를 호출해서 조건식을 사용하기
if always_false() and always_True() :
    print(True)
else:
    print(False)

'''
# 파이썬은 and 나 or 연산을 할 때 첫번째 값을 보고 더이상 실행할 필요가 없으면 두번째 값을 실행하지 않음
  => 이런 활용을 단락 평가 (short-circuit)이라고 함
'''

print('------------------------------')
print(always_false() and always_True())

print('------------------------------')

# 단락 평가는 복잡한 코드를 단순하게 하는데 유용함
dic = {'key2', 'value1'}

# key1에 value1이 대입되어있는지 확인
if 'key1' in dic : 
    if dic['key1'] == 'value1' :
        print('dic의 key1에 value1이 대입되어있다')
    else : 
        print('dic의 key1이 있으나 value1이 대입되어있지는 않다')
else : 
    print('dic에 key1이 없다')

print('------------------------------')

if 'key1' in dic and dic['key1'] == 'value1' :
    print('dic에는 key1에 value1이 대입되어있다')
else :
    print('key1이 없어요')

print('------------------------------')

if dic['key1'] == 'value1' and 'key1' in dic :
    print('dic에는 key1에 value1이 대입되어있다')
else :
    print('key1이 없어요')











