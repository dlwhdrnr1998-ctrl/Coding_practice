number_of_book = 100

#number는 대여하는 책의 수
def decrease_book(number):
    global number_of_book
    number_of_book = number_of_book - number
    print(f"남은 책의 수 : {number_of_book}")


#name은 대여자 이름
def rental_book(name,number):
    decrease_book(number)
    print(f"{name}님이 {number}권의 책을 대여하였습니다.")

rental_book('홍길동',3)

'''
decrease_book 함수는 한 번에 대여하는 책의 수를 정수로 넘겨 받는다.
넘겨받은 값만큼 number_of_book의 수를 감소시키고,
현재 남은 책의 수를 출력한다.
rental_book 함수는 대여자의 이름과, 대여하는 책의 수를 인자로 넘겨 받는다.
rental_book 함수가 실행 될 때, decrease_book 함수를 호출한다.
이후, '{name}님이 {number}권의 책을 대여하였습니다.' 문구를 출력한다.
'''