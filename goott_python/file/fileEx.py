print()
'''
# open(file, mode, , ...)
# 첫번째 파라미터(file) : 파일의 상대경로
# 두번째 파라미터(mode) : 파일을 여는 모드 옵션
 - r : 기본값. 읽기 전용
 - w : 파일 쓰기. 파일이 이미 존재한다면 해당 파일을 비움
 - x : 배타적 생성. 파일이 이미 존재한다면 open() 실패
 - a : 파일 쓰기. 파일이 이미 존재한다면 파일의 끝에 내용을 덧붙임
 - b : 바이너리 모드로 열기
 - t : 텍스트 모드로 열기
 - + : 읽기와 쓰기를 모두 다 

'''
# f = open('good.txt', 'r', encoding='UTF8')

# 파일 전체 읽기
# read = f.read()

# 파일 한 행 읽기
#read = f.readline()

# 파일 전체를 읽은 후 리스트로 리턴
#read = f.readlines()

# 파일을 읽고 닫지 않으면 화면에 출력이 안되었으나 지금은 출력을 해줌 - 닫는게 권장사항
#f.close()
#print(read)
#print(read[2]) # 인덱싱도 가능

# file 객체는 순회가능(iterator) 하므로 for문에 리스트 대신 바로 file 객체를 넣을 수 있음
#for line in f:
#    print(line)


# ---------------------------------------------------------
# 파일을 열고 닫는 과정을 자동으로 해주고 그 과정에서 오류가 발생하면 알아서 처리
# with 구문
with open('good.txt', encoding="UTF8") as f:
    print(f.readline())