# main.py


# 아래 클래스를 수정하시오.
class Shape: 
    def __init__(self,가로,세로):
        self.가로 = 가로
        self.세로 = 세로

        
shape1 = Shape(5, 3)
print(shape1.가로, shape1.세로)


# 문제
# Shape 클래스를 작성하시오. 
# 이 클래스는 초기화 메서드를 가지며 가로와 세로 길이를 인자로 받아 속성으로 저장한다. 
# 인스턴스를 생성하고 속성에 접근하여 값을 출력하시오.