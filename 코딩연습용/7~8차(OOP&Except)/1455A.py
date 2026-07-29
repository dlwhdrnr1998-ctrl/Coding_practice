# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,가로,세로):
        self.가로 = 가로
        self.세로 = 세로

    def calculate_area(self):
        return (self.가로)*(self.세로)


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)

#Shape 클래스에 calculate_area 메서드를 추가하여 사각형의 넓이를 계산하여 반환하시오. 

