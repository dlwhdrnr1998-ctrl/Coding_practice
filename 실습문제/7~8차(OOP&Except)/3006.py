# 새로운 모델 클래스 ExtendedModel을 만든다.
# ExtendedModel은 Novel과 Other 클래스를 다중 상속받아야 한다.
# ExtendedModel은 새로운 속성 extended_type을 가져야 한다.

# ExtendedModel 클래스를 이용하여 새로운 모델 인스턴스 extended_instance를 생성한다.

# ExtendedModel 클래스에 display_info 메서드를 추가한다.
# 이 메서드는 클래스 변수 PK와 클래스 변수 TYPE, 그리고 인스턴스 변수 extended_type을 출력한다.
# ExtendedModel의 save 메서드 호출시 "데이터를 확장해서 저장합니다."를 출력하도록 수정한다.

# extended_instance의 display_info 메서드를 호출하여 정보를 출력한다.
# extended_instance의 save 메서드를 호출하여 저장 메시지를 출력한다.

# 모든 모델 클래스의 인스턴스 생성과 메서드 호출 결과를 확인하여 적절한 출력을 한다.

#<답안> : 3005 소스코드에서 출발
class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel):
    TYPE = 'Other Model'

#3006 답안 시작
class ExtendedModel(Novel,Other):
    def __init__(self, data_type, title, content, created_at, updated_at, author,extended_type):
        super().__init__(data_type, title, content, created_at, updated_at,author)
        self.extended_type = extended_type

    def display_info(self):
        print(f"PK : {self.PK},TYPE : {self.TYPE}, Extended Type : {self.extended_type}")

    def save(self):
        print("데이터를 확장해서 저장합니다.")



extended_instance = ExtendedModel('소설', '홍길동', '고전 소설', 1618, 1692, '허균','추가 타입')
extended_instance.display_info()
extended_instance.save()

        




