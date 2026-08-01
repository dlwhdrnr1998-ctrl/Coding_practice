# 문제
# 자연수 N을 입력받아 출력예와 같이 N행 N열의 숫자사각형을 출력하는 프로그램을 작성하시오.
# (출력하는 부분은 함수로 작성한다.)

# 입력 3 
# 출력 1 2 3
#     4 5 6
#     7 8 9

#내답
def print_table():
    N = int(input("숫자를 입력하쇼: "))
    for i in range(1,N**2+1):
        if i % N == 0 :
            print (i, end = " ")
            print ("")
        else: 
            print (i, end = " ")

print_table()

#모범답안(이중 for문)
def print_table():
    N = int(input("숫자를 입력하쇼: "))
    num = 1  # 1부터 시작할 카운터 변수
    
    for row in range(N):        # N줄 반복
        for col in range(N):    # 한 줄에 N칸 반복
            print(num, end=" ")
            num += 1            # 숫자 1 증가
        print()                 # 한 줄 다 출력했으면 줄 바꿈

print_table()
