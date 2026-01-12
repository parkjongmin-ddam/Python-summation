# List는 가변적인 크기를 가지며, 여러가지 타입의 요소를 포함시킬 수 있는 데이터 구조
# List는 대괄호 [] 를 사용하여 표현한다.
# List는 아래와 같은 특징을 가지고 있음
# 가변성(Mutable): List는 요소의 추가,삭제,변경이 가능하다
# 인덱싱(indexing): List의 각 요소는 Index를 통해 접근할 수 있다 (첫번째 요소는 0번 Index, 두번째 요소는 1번 Index, ...)
# Ex.)mylist[0]은 List의 첫번째 요소를 반환하고, mylist[-1]은 List의 마지막 요소를 반환한다.
# 슬라이싱(Slicing): List의 일부분을 추출하기 위해 Slicing을 사용할 수 있으며, Slicing은 List의 일부를 새로운 List로 생성한다.
# 다양한 메서드와 함수: List는 다양한 메서드와 함수를 제공하여 요소를 추가, 제거, 정렬, 반전 등의 작업을 수행할 수 있습니다.

# List 생성 방법

# 빈 List 생성
my_list = []

# 기본적인 List 생성
basic_list = [1, 2, 3, 4, 5]
# 다양한 데이터 타입을 포함하는 List 생성
datatypes_list = [1, "apple", 3.14, True, None]

# List 내 List(중첩 List) 생성
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List에 요소 추가하기 : append() 메서드를 사용하여 List 마지막에 요소를 추가할 수 있다.
basic_list = [1, 2, 3, 4, 5]
basic_list.append(6) # basic_list에 6을 추가한다.
#print(basic_list) # [1, 2, 3, 4, 5, 6]

# insert 메서드를 사용하여 특정 위치에 요소를 추가할 수 있다.
datatypes_list = [1, "apple", 3.14, True, None]
datatypes_list.insert(1, "banana") # datatypes_list의 1번 인덱스에 "banana"을 추가한다.
#print(datatypes_list) # [1, "banana", "apple", 3.14, True, None]

# List 병합 : extend() 메서드를 사용하여 List를 병합할 수 있다.
basic_list = [1, 2, 3, 4, 5]
datatypes_list = [1, "apple", 3.14, True, None]
basic_list.extend(datatypes_list) # basic_list에 datatypes_list를 병합한다.
#print(basic_list) # [1, 2, 3, 4, 5, 1, "apple", 3.14, True, None]

# List 내 요소 삭제하기 : remove() 메서드를 사용하여 List에서 요소를 삭제할 수 있다.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list.remove([4, 5, 6]) # nested_list에서 [4, 5, 6]을 삭제한다.
#print(nested_list) # [[1, 2, 3], [7, 8, 9]]

# pop() 메서드를 사용하여 List에서 요소를 삭제할 수 있다.
basic_list = [1, 2, 3, 4, 5]
basic_list.pop(2) # basic_list에서 2번 인덱스의 요소를 삭제한다.
#print(basic_list) # [1, 2, 4, 5]

# Clear() 메서드를 사용하여 List를 초기화할 수 있다.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list.clear() # nested_list를 초기화한다.
#print(nested_list) # []

# List 내 요소 개수 세기 : count() 메서드를 사용하여 특정 요소의 개수를 셀 수 있다.
basic_list = [1, 2, 3, 2, 4, 2, 5]
count_result = basic_list.count(2) # basic_list에서 2의 개수를 반환한다.
#print(count_result) # 3

# List 내 요소 인덱스 찾기 : index() 메서드를 사용하여 특정 요소의 인덱스를 찾을 수 있다.
basic_list = [1, 2, 3, 4, 5]
index_result = basic_list.index(3) # basic_list에서 3의 인덱스를 반환한다.
#print(index_result) # 2

# List 정렬하기 : sort() 메서드를 사용하여 List를 정렬할 수 있다.
basic_list = [3, 1, 4, 1, 5, 9, 2, 6]
basic_list.sort() # basic_list를 오름차순으로 정렬한다.
#print(basic_list) # [1, 1, 2, 3, 4, 5, 6, 9]

# 내림차순 정렬
basic_list = [3, 1, 4, 1, 5, 9, 2, 6]
basic_list.sort(reverse=True) # basic_list를 내림차순으로 정렬한다.
#print(basic_list) # [9, 6, 5, 4, 3, 2, 1, 1]

# List 역순 정렬하기 : reverse() 메서드를 사용하여 List의 순서를 역순으로 변경할 수 있다.
basic_list = [1, 2, 3, 4, 5]
basic_list.reverse() # basic_list의 순서를 역순으로 변경한다.
#print(basic_list) # [5, 4, 3, 2, 1]

# List 복사하기 : copy() 메서드를 사용하여 List를 복사할 수 있다.
basic_list = [1, 2, 3, 4, 5]
copied_list = basic_list.copy() # basic_list를 복사하여 새로운 List를 생성한다.
#print(copied_list) # [1, 2, 3, 4, 5]

# List 길이 확인하기 : len() 함수를 사용하여 List의 길이를 확인할 수 있다.
basic_list = [1, 2, 3, 4, 5]
length = len(basic_list) # basic_list의 길이를 반환한다.
#print(length) # 5

# List 내 요소 포함 여부 확인하기 : in 연산자를 사용하여 List에 특정 요소가 포함되어 있는지 확인할 수 있다.
basic_list = [1, 2, 3, 4, 5]
is_in_list = 3 in basic_list # basic_list에 3이 포함되어 있는지 확인한다.
#print(is_in_list) # True

# List 최대값, 최소값, 합계 구하기 : max(), min(), sum() 함수를 사용할 수 있다.
basic_list = [1, 2, 3, 4, 5]
max_value = max(basic_list) # basic_list의 최대값을 반환한다.
min_value = min(basic_list) # basic_list의 최소값을 반환한다.
sum_value = sum(basic_list) # basic_list의 합계를 반환한다.
#print(f"최대값: {max_value}") # 5
#print(f"최소값: {min_value}") # 1
#print(f"합계: {sum_value}") # 15