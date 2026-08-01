# 주어진 딕셔너리에서 특정 키에 해당하는 값을 가져오는 get_value_from_dict 함수를 작성하시오. 
# 요구사항
# 딕셔너리와 키를 인자로 받아 해당 키에 대응하는 값을 반환해야 한다.
# 조회하고자 하는 키가 딕셔너리에 존재하지 않는 경우, 'Unknown' 값을 반환해야 한다.

#<문제>
def get_value_from_dict():
    pass


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

result = get_value_from_dict(my_dict, 'gender')
print(result)  # Unknown


#<solve1> : if in 활용 
def get_value_from_dict(my_dict,key):
    if key in my_dict:
        value = my_dict[key]
        return value
    else :
        return "Unknown"

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

result = get_value_from_dict(my_dict, 'gender')
print(result)  # Unknown



#<solve2> : .get 메서드 활용
def get_value_from_dict(my_dict, key):
    # key가 없으면 두 번째 인자인 'Unknown'을 반환함
    return my_dict.get(key, 'Unknown')

my_dict = {'name': 'Alice', 'age': 25}

print(get_value_from_dict(my_dict, 'name'))    # Alice
print(get_value_from_dict(my_dict, 'gender'))  # Unknown



