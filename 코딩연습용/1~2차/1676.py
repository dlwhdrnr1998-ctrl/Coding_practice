information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]


information[authors[0]] = books[1] 
information[authors[1]] = books[3] 
information[authors[2]] = books[4]
information[authors[3]] = books[0] 
information[authors[4]] = books[2] 

for author, book_list in information.items():
    print(f"{author}: {book_list}")


""" 파이썬의 딕셔너리를 활용하여 올바른 작가의 key 값에 올바른 도서 목록 리스트가 
value로 할당 될 수 있도록 코드를 작성하시오. 
단, 작가 이름과 책 이름은 모두 authors, books 리스트에서 인덱스로 접근하여 
information dict에 할당 한다.
			
요구사항
작가와 작품 목록 참고
허균 : 홍길동전, 장생전, 도문대작
임제 : 수성지, 백호집, 원생몽유록
남영로 :옥루몽, 옥련몽
김시습 : 금오신화, 이생규장전, 만복자서포기
작자 미상 : 장화홍련전, 가락국 신화, 온달 설화"""