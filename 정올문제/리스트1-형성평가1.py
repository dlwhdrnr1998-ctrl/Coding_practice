#<문제>
# 최대 100개의 정수를 차례로 입력받다가 -1이 입력되면 입력을 중단하고
#  -1을 제외한 마지막 세 개의 정수를 출력하는 프로그램을 작성하시오.
# (입력받은 정수가 3개 미만일 경우에는 모두 출력한다.)

#내답
list_1 = []
count = 0

while True: 
    num = int(input("숫자를 입력하세요 : "))
    list_1.append(num)
    count += 1
    if count > 100 : 
        break
    if num == -1:
        print (list_1[-4:-1])
        break


#모범답안1
list_1 = []

while len(list_1) < 100:  # 최대 100개까지만 받음
    num = int(input())
    
    if num == -1:
        break  # -1이면 리스트에 넣지 않고 탈출!
        
    list_1.append(num)

# *list_1[-3:] : 대괄호 [] 없이 알맹이만 띄어쓰기로 출력 (언패킹)
print(*list_1[-3:])

#모범답안2
list_1 = []

for _ in range(100):
    num = int(input())
    if num == -1:
        break
    list_1.append(num)

# 뒤에서 3개 출력
print(*list_1[-3:])