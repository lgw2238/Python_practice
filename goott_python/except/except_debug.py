print()
'''
# 다른 코드에서 쓸 함수나 모듈을 생성 시 디버깅을 먼저 해보기 위해서 오류를 일으켜 볼 수도 있음


'''
# ex) 가위, 바위, 보 함수체크 - / 묵, 찌, 빠 와 같은 다른 값이 들어오는 것은 막고 싶음
def rsp(x, y):
    allowed = ['가위','바위','보']
    if x not in allowed:
        raise ValueError
    if y not in allowed:
        raise ValueError
# rsp('가위', '바위') - 에러 발생 x
# rsp('묵', '찌') - 에러 발생 => 에러 처리가 필요

try:
    rsp('묵', '가위')
except:
    print('잘못된 값을 입력하셨습니다.') # 프로그램이 멈추지 않도록  오류처리를 해줘야함 .

print('-------------------------------------------------------------------')
# 예외처리 말고도 오류를 활용하는 다른 방법도 존재
# : 중첩된 반복문에서 예외를 발생시켜 전체 반복문 밖으로 빠져 나가기
'''
# ex) KBL 농구 구단 2개
# ( 조건: 3M를 넘는 선수가 있으면 그 구단 정보를 출력하고 구단활동을 정지)
# 두 구단 중 먼저 3M 넘는 선수가 있는 구단을 찾는 순간 다 정지
'''
kbl = {'A구단' :[178, 188, 190, 198, 302], 'B구단':[199,192,189,301,208]}

for id, heights in kbl.items():
    for height in heights:
        if height > 300:
            print(id, ' 3M를 넘는 선수가 있습니다.')
            break

print('-------------------------------------------------------')
# for id, heights in kbl.items():
#     for height in heights:
#         if height > 300:
#             print(id, ' 3M를 넘는 선수가 있습니다.')
#             raise StopIteration

try :
    for id, heights in kbl.items():
        for height in heights:
            if height > 300:
                print(id, ' 3M를 넘는 선수가 있습니다.')
                break
except StopIteration:
    print('협회 차원에서 처리...')