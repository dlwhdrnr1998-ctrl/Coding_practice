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

    def save(self):
            print('데이터를 다른 장소에 저장합니다.')


# TYPE 클래스 변수의 값을 'Other Model'으로 변경한다.
# save 메서드의 출력 내용을 변경한다.

hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
print('Novel 모델 인스턴스의 PK와 save 메서드')
print(hong.PK)
print(chun.PK)
hong.save()
chun.save()
print(hong.author)
print(chun.author)
print('---')

company = Other('회사', '회사명', '회사 설명', 2000, 2023)
print('Other 모델 인스턴스의 PK와 save 메서드')
print(company.PK)
company.save()

print('---')
print('모델 별 타입')
print(Novel.TYPE)
print(Other.TYPE)


# BaseModel class를 상속받는 Novel과 Other 클래스를 정의한다.
# Novel class는 BaseModel와 동일한 생성자를 사용하되, author 인자를 추가로 받는다.
# 내장함수 super를 사용한다.
# Other class에 다음 내용을 추가한다.

# 코드를 실행하고 출력 결과를 확인한다.