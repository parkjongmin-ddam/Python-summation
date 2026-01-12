# Dictionary(딕셔너리) 자료형
# Dictionary는 Python에서 사용하는 Key(키)와 Value(값)의 쌍을 저장하는 자료형이다.
# Dictionary는 중괄호 {} 를 사용하여 표현한다.
# Dictionary는 아래와 같은 특징을 가지고 있다:
# 키-값 쌍 구조: 각 키에는 값이 연결되어 있으며, 키를 통해 값을 빠르게 찾을 수 있다.
# 가변성(Mutable): Dictionary는 요소의 추가, 수정, 삭제가 가능하다.
# 키의 고유성: Dictionary 내에서 각 키는 고유해야 하며, 동일한 키가 중복될 수 없다.
# 키의 불변성: 키는 불변(immutable) 객체만 가능하다 (문자열, 숫자, 튜플 등).
# 값의 유연성: 값은 중복될 수 있으며, 다양한 데이터 타입일 수 있다.

# ============================================================================
# Dictionary vs List vs Tuple 비교표
# ============================================================================
# | 특징          | Dictionary                | List                        | Tuple                      |
# |--------------|--------------------------|----------------------------|---------------------------|
# | 문법          | 중괄호 {} 사용             | 대괄호 [] 사용              | 소괄호 () 사용              |
# | 구조          | 키-값 쌍                  | 순서 있는 요소 나열          | 순서 있는 요소 나열        |
# | 접근 방법      | 키로 접근 (dict[key])      | 인덱스로 접근 (list[0])      | 인덱스로 접근 (tuple[0])   |
# | 가변성        | 가변 (Mutable)            | 가변 (Mutable)              | 불변 (Immutable)           |
# | 요소 수정     | 가능                      | 가능                        | 불가능                     |
# | 요소 추가     | 가능                      | 가능                        | 불가능                     |
# | 요소 삭제     | 가능                      | 가능                        | 불가능                     |
# | 키/인덱스     | 키는 고유해야 함           | 인덱스는 0부터 시작          | 인덱스는 0부터 시작        |
# | 검색 속도     | 매우 빠름 (O(1))          | 느림 (O(n))                | 느림 (O(n))                |
# | 사용 시나리오  | 키-값 매핑, JSON 데이터    | 변경 가능한 데이터 모음      | 고정된 데이터, 딕셔너리 키   |
# ============================================================================

# ============================================================================
# Dictionary 생성 방법
# ============================================================================

# 빈 Dictionary 생성
empty_dict = {}
#print(empty_dict) # {}

# 또는 dict() 함수 사용
empty_dict2 = dict()
#print(empty_dict2) # {}

# 기본적인 Dictionary 생성
# Dictionary는 중괄호 안에 Key(키)-Value(값) 쌍을 콤마로 구분하여 생성한다.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
#print(my_dict) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 다양한 데이터 타입을 값으로 사용
datatypes_dict = {
    "name": "Python",
    "age": 30,
    "price": 99.99,
    "is_active": True,
    "tags": ["programming", "language"],
    "metadata": None
}
#print(datatypes_dict)

# dict() 함수를 사용한 생성
dict_from_function = dict(name="Alice", age=25, city="New York")
#print(dict_from_function) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 리스트의 튜플 쌍으로부터 생성
dict_from_list = dict([("name", "Alice"), ("age", 25), ("city", "New York")])
#print(dict_from_list) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# zip() 함수를 사용한 생성
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
dict_from_zip = dict(zip(keys, values))
#print(dict_from_zip) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Dictionary Comprehension을 사용한 생성
dict_comprehension = {x: x**2 for x in range(1, 6)}
#print(dict_comprehension) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ============================================================================
# Dictionary 요소 접근하기
# ============================================================================
# Dictionary에서 특정 키를 사용하여 해당 값을 조회할 수 있다.

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 방법 1: 대괄호를 사용한 접근
name = my_dict["name"] # "name" 키에 해당하는 값을 가져온다.
#print(name) # Alice

age = my_dict["age"] # "age" 키에 해당하는 값을 가져온다.
#print(age) # 25

# 존재하지 않는 키에 접근하면 KeyError가 발생한다.
# value = my_dict["email"] # KeyError: 'email'

# 방법 2: get() 메서드를 사용한 접근 (안전한 방법)
name = my_dict.get("name") # "name" 키에 해당하는 값을 가져온다.
#print(name) # Alice

email = my_dict.get("email") # 존재하지 않는 키는 None을 반환한다.
#print(email) # None

# 기본값 지정 가능
email = my_dict.get("email", "Not found") # 키가 없으면 기본값 반환
#print(email) # "Not found"

# 방법 3: setdefault() 메서드 (키가 없으면 기본값 설정 후 반환)
city = my_dict.setdefault("city", "Unknown") # 키가 있으면 값 반환, 없으면 기본값 설정
#print(city) # "New York"

country = my_dict.setdefault("country", "USA") # 키가 없으면 기본값 설정 후 반환
#print(country) # "USA"
#print(my_dict) # {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

# ============================================================================
# Dictionary 요소 추가 및 수정하기
# ============================================================================
# Dictionary에 새로운 키-값 쌍을 추가하거나, 기존 키의 값을 수정할 수 있다.

my_dict = {"name": "Alice", "age": 25}

# 새로운 키-값 추가
my_dict["city"] = "New York" # "city" 키와 값을 추가한다.
#print(my_dict) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 기존 값 수정
my_dict["age"] = 26 # "age" 키의 값을 26으로 수정한다.
#print(my_dict) # {'name': 'Alice', 'age': 26, 'city': 'New York'}

# 여러 키-값 쌍을 한 번에 추가/수정
my_dict.update({"age": 30, "country": "USA"}) # 여러 키-값 쌍을 한 번에 업데이트한다.
#print(my_dict) # {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# ============================================================================
# Dictionary 요소 삭제하기
# ============================================================================
# del 키워드나 pop() 메서드를 사용하여 Dictionary에서 특정 키-값 쌍을 삭제할 수 있다.

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 방법 1: del 키워드 사용
del my_dict["age"] # "age" 키-값 쌍을 삭제한다.
#print(my_dict) # {'name': 'Alice', 'city': 'New York'}

# 방법 2: pop() 메서드 사용 (값을 반환하면서 삭제)
city = my_dict.pop("city") # "city" 키의 값을 반환하고 삭제한다.
#print(city) # "New York"
#print(my_dict) # {'name': 'Alice'}

# pop() 메서드에 기본값 지정 (키가 없을 때 에러 방지)
value = my_dict.pop("email", "Not found") # 키가 없으면 기본값 반환
#print(value) # "Not found"

# 방법 3: popitem() 메서드 (마지막 키-값 쌍을 반환하고 삭제)
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
key, value = my_dict.popitem() # 마지막 키-값 쌍을 반환하고 삭제한다.
#print(key, value) # 'city', 'New York'
#print(my_dict) # {'name': 'Alice', 'age': 25}

# 방법 4: clear() 메서드 (모든 키-값 쌍 삭제)
my_dict.clear() # Dictionary의 모든 키-값 쌍을 삭제한다.
#print(my_dict) # {}

# ============================================================================
# Dictionary 주요 메서드 및 함수
# ============================================================================
# ============================================================================
# Dictionary 메서드 정리표
# ============================================================================
# | 메서드/함수     | 설명                          | 예제                        | 반환값              |
# |---------------|------------------------------|---------------------------|-------------------|
# | keys()        | 모든 키 반환                   | dict.keys()                | dict_keys 객체     |
# | values()      | 모든 값 반환                   | dict.values()              | dict_values 객체   |
# | items()       | 모든 키-값 쌍 반환              | dict.items()               | dict_items 객체    |
# | get()         | 키로 값 가져오기 (안전)         | dict.get(key, default)      | 값 또는 기본값      |
# | setdefault()  | 키로 값 가져오기 (없으면 설정)   | dict.setdefault(key, val)   | 값                 |
# | pop()         | 키로 값 가져오고 삭제           | dict.pop(key, default)      | 값 또는 기본값      |
# | popitem()     | 마지막 키-값 쌍 가져오고 삭제    | dict.popitem()              | (키, 값) 튜플      |
# | update()      | 다른 딕셔너리로 업데이트         | dict.update(other)          | None               |
# | clear()       | 모든 키-값 쌍 삭제              | dict.clear()                | None               |
# | copy()        | 딕셔너리 복사                   | dict.copy()                 | 새로운 딕셔너리     |
# | len()         | 키-값 쌍의 개수                 | len(dict)                   | 정수               |
# | in            | 키 존재 여부 확인                | key in dict                 | True/False         |
# ============================================================================

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# keys(): 모든 키를 가져오기
keys = my_dict.keys() # 모든 키를 dict_keys 객체로 반환한다.
#print(keys) # dict_keys(['name', 'age', 'city'])
#print(list(keys)) # ['name', 'age', 'city'] (리스트로 변환)

# values(): 모든 값을 가져오기
values = my_dict.values() # 모든 값을 dict_values 객체로 반환한다.
#print(values) # dict_values(['Alice', 25, 'New York'])
#print(list(values)) # ['Alice', 25, 'New York'] (리스트로 변환)

# items(): 모든 키-값 쌍을 가져오기
items = my_dict.items() # 모든 키-값 쌍을 dict_items 객체로 반환한다.
#print(items) # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])
#print(list(items)) # [('name', 'Alice'), ('age', 25), ('city', 'New York')] (리스트로 변환)

# get(): 키로 값 가져오기 (안전한 방법)
age = my_dict.get("age") # "age" 키에 해당하는 값을 가져온다.
#print(age) # 25

email = my_dict.get("email") # 존재하지 않는 키는 None을 반환한다.
#print(email) # None

email = my_dict.get("email", "Not found") # 기본값 지정 가능
#print(email) # "Not found"

# copy(): Dictionary 복사
copied_dict = my_dict.copy() # my_dict를 복사하여 새로운 Dictionary를 생성한다.
#print(copied_dict) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# len(): Dictionary의 키-값 쌍 개수
length = len(my_dict) # my_dict의 키-값 쌍 개수를 반환한다.
#print(length) # 3

# ============================================================================
# Dictionary 순회하기
# ============================================================================
# Dictionary의 모든 키, 값, 또는 키-값 쌍을 순회할 수 있다.

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 키만 순회 (기본 동작)
for key in my_dict:
    #print(key) # name, age, city를 순차적으로 출력
    pass

# keys() 메서드를 사용한 명시적 키 순회
for key in my_dict.keys():
    #print(key) # name, age, city를 순차적으로 출력
    pass

# 값만 순회
for value in my_dict.values():
    #print(value) # Alice, 25, New York을 순차적으로 출력
    pass

# 키-값 쌍 순회 (가장 유용함)
for key, value in my_dict.items():
    #print(f"{key}: {value}") # name: Alice, age: 25, city: New York을 순차적으로 출력
    pass

# enumerate()와 함께 사용
for index, (key, value) in enumerate(my_dict.items()):
    #print(f"인덱스 {index}: {key} = {value}")
    pass

# ============================================================================
# Dictionary 키 존재 여부 확인하기
# ============================================================================
# in 연산자를 사용하여 특정 키가 Dictionary에 있는지 확인할 수 있다.

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# in 연산자 사용
is_name = "name" in my_dict # "name" 키가 my_dict에 있는지 확인한다.
#print(is_name) # True

is_email = "email" in my_dict # "email" 키가 my_dict에 있는지 확인한다.
#print(is_email) # False

# not in 연산자 사용
is_not_name = "name" not in my_dict # "name" 키가 my_dict에 없는지 확인한다.
#print(is_not_name) # False

# ============================================================================
# Dictionary 병합하기
# ============================================================================
# update() 메서드나 ** 연산자를 사용하여 Dictionary를 병합할 수 있다.

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}

# 방법 1: update() 메서드 사용
dict1.update(dict2) # dict1에 dict2의 키-값 쌍을 병합한다.
#print(dict1) # {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

# 방법 2: ** 연산자 사용 (Python 3.5+)
dict3 = {"name": "Alice", "age": 25}
dict4 = {"city": "New York", "country": "USA"}
merged_dict = {**dict3, **dict4} # 두 Dictionary를 병합하여 새로운 Dictionary 생성
#print(merged_dict) # {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

# 중복된 키가 있으면 나중 값이 이전 값을 덮어쓴다
dict5 = {"name": "Alice", "age": 25}
dict6 = {"age": 30, "city": "New York"}
dict5.update(dict6) # "age" 키의 값이 30으로 덮어씌워진다.
#print(dict5) # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# ============================================================================
# Dictionary Comprehension
# ============================================================================
# Dictionary Comprehension을 사용하면 간결하게 Dictionary를 생성할 수 있다.

# 기본 Dictionary Comprehension
squared_dict = {x: x**2 for x in range(1, 6)} # 1부터 5까지의 제곱 Dictionary
#print(squared_dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 조건부 Dictionary Comprehension
even_squared = {x: x**2 for x in range(1, 11) if x % 2 == 0} # 짝수만 제곱
#print(even_squared) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 기존 Dictionary에서 새 Dictionary 생성
original = {"a": 1, "b": 2, "c": 3, "d": 4}
doubled = {k: v * 2 for k, v in original.items()} # 모든 값을 2배
#print(doubled) # {'a': 2, 'b': 4, 'c': 6, 'd': 8}

# 키와 값을 바꾸기
swapped = {v: k for k, v in original.items()} # 키와 값을 바꾼다.
#print(swapped) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# ============================================================================
# 중첩 Dictionary
# ============================================================================
# Dictionary 안에 Dictionary를 포함할 수 있다.

nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
    "person3": {"name": "Charlie", "age": 35}
}

# 중첩 Dictionary 접근
person1_name = nested_dict["person1"]["name"] # 중첩 Dictionary의 값에 접근한다.
#print(person1_name) # "Alice"

# 중첩 Dictionary 수정
nested_dict["person1"]["age"] = 26 # 중첩 Dictionary의 값을 수정한다.
#print(nested_dict["person1"]) # {'name': 'Alice', 'age': 26}

# ============================================================================
# 주의사항
# ============================================================================
# 1. Dictionary의 키는 불변 객체만 가능하다 (문자열, 숫자, 튜플 등).
#    List는 키로 사용할 수 없다: invalid_dict = {[1, 2]: "error"} # TypeError
#
# 2. 동일한 키가 여러 번 사용되면 마지막 값이 이전 값을 덮어쓴다.
#    my_dict = {"a": 1, "a": 2} # {"a": 2} (마지막 값만 유지)
#
# 3. Dictionary는 Python 3.7+ 부터 삽입 순서를 보장한다.
#
# 4. get() 메서드는 키가 없을 때 None을 반환하지만, 대괄호 접근은 KeyError를 발생시킨다.
#
# 5. keys(), values(), items()는 뷰 객체를 반환하므로, 원본 Dictionary가 변경되면 뷰도 변경된다.
# ============================================================================

