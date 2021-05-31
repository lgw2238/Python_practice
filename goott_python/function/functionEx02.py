print()
'''
#함수 구조 3 - 함수 입력값(매개변수)이 몇 개 인지 모를 경우
def 함수명(*입력변수명)
    <수행할 문장> ..
    <return>
    
'''

def sum(*args):             # args (arguments) - 관례적
    sum = 0
    for i in args :
        sum += i
    return sum

result = sum(1,2,3,4,5,6,7,8,9,10)
print(result)

print('------------------------------------------------------')
# call by value 로 찾으며, 함수의 매개변수를 작성할 때는 변수명을 구분해서 적어놓는게 좋음
# ex) var 과 ranTest()안의 var
var = 1
def ranTest(var):
    var = var + 1
   # print(var)

#print(ranTest(var))
print(var)

print('------------------------------------------------------')
# 위의 함수와 대조. 변수값이 다름을 확인
var = 1
def ranTest(var2):
    var2 = var2+1
    print(var2)

ranTest(var)
'''
cf) 내장 함수 : import 하지 않고 즉시 사용 가능한 함수들
            : 주의 - 내장 함수명을 일종의 키워드로 간주하여 사용자(개발자)가 시별자 혹은 사용자 정의 함수로
                    만들어서 사용하는 것은 피해야 됨.

'''
