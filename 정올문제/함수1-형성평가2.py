#<문제>
# 1부터 전달받은 수까지의 합을 출력하는 함수를 작성하고
# 1000 이하의 자연수를 입력받아 작성한 함수로 전달하여 출력하는 프로그램을 작성하시오.

#<내답안>
def random_sum():
    num = int(input("숫자를 입력하세요 : "))
    if num <= 1000:
        total = 0
        list1 = list(range(1,num+1))

        for i in list1:
            total += i
        return total
        
    else : 
        message = "말귀를 못알아 쳐먹냐"
        return message

print(random_sum())

#<모범답안>: 내장함수 sum활용
def random_sum():
    num = int(input("1000 이하의 숫자를 입력하세요: "))
    
    if num <= 1000:
        return sum(range(1, num + 1))  # 메모리 사용 최소화 & 코드 간결
    else:
        print("1000 이하의 숫자만 입력하세요.")

print(random_sum())

#<모범답안2>: 가우스 공식 활용
def random_sum():
    num = int(input("1000 이하의 숫자를 입력하세요: "))
    
    if num <= 1000:
        return num * (num + 1) // 2  # //는 정수 나눗셈
    else:
        print("1000 이하의 숫자만 입력하세요.")

print(random_sum())
