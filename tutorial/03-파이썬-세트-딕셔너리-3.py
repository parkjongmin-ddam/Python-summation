# Dictionary(딕셔너리) 생성 방법
# Dictionary는 여러 가지 방법으로 생성할 수 있다.
# 각 방법은 상황에 따라 적합한 경우가 다르므로, 목적에 맞는 방법을 선택하는 것이 중요하다.

# ============================================================================
# Dictionary 생성 방법 비교표
# ============================================================================
# | 생성 방법                    | 문법 예시                          | 특징                          | 사용 시나리오              |
# |----------------------------|-----------------------------------|------------------------------|--------------------------|
# | 중괄호 {} 사용               | {"key": "value"}                  | 가장 간단하고 직관적            | 일반적인 Dictionary 생성   |
# | dict() 함수 (키워드 인자)     | dict(key="value")                 | 키가 문자열이고 유효한 식별자일 때 | 동적 생성, 함수 인자 전달  |
# | dict() 함수 (리스트/튜플)     | dict([("key", "value")])          | 기존 데이터 구조에서 변환        | 리스트/튜플 데이터 변환     |
# | zip() 함수                  | dict(zip(keys, values))           | 두 리스트를 키-값 쌍으로 결합     | 별도의 키/값 리스트 결합    |
# | Dictionary Comprehension   | {k: v for k, v in items}          | 조건부 생성, 변형 가능           | 복잡한 조건이나 변형 필요   |
# | fromkeys() 메서드           | dict.fromkeys(keys, value)        | 동일한 값으로 여러 키 생성        | 기본값으로 초기화          |
# ============================================================================

# ============================================================================
# 방법 1: 중괄호 {}를 사용한 Dictionary 생성
# ============================================================================
# 가장 기본적이고 가장 많이 사용하는 방법이다.

# 빈 Dictionary 생성
empty_dict1 = {} # 중괄호를 사용하여 빈 Dictionary를 생성한다.
#print(empty_dict1) # {}

# 기본적인 Dictionary 생성
# Dictionary는 중괄호 안에 Key(키)-Value(값) 쌍을 콤마로 구분하여 생성한다.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
#print(my_dict) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 여러 줄로 작성 (가독성 향상)
multi_line_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "country": "USA"
}
#print(multi_line_dict)

# 다양한 데이터 타입을 값으로 사용
datatypes_dict = {
    "name": "Python",           # 문자열
    "age": 30,                  # 정수
    "price": 99.99,             # 실수
    "is_active": True,          # 불린
    "tags": ["programming", "language"],  # 리스트
    "metadata": None,           # None
    "coordinates": (10, 20),    # 튜플
    "nested": {"key": "value"}  # 중첩 Dictionary
}
#print(datatypes_dict)

# ============================================================================
# 방법 2: dict() 함수를 사용한 Dictionary 생성
# ============================================================================

# 방법 2-1: 빈 Dictionary 생성
empty_dict2 = dict() # dict() 함수를 사용하여 빈 Dictionary를 생성한다.
#print(empty_dict2) # {}

# 방법 2-2: 키워드 인자를 사용한 생성
# 키가 문자열이고 유효한 Python 식별자일 때 사용할 수 있다.
dict_from_keywords = dict(name="Alice", age=25, city="New York")
#print(dict_from_keywords) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 주의: 키워드 인자 방식은 키가 문자열이고 유효한 식별자여야 한다.
# dict(1="one") # SyntaxError: 키워드 인자는 숫자로 시작할 수 없다.
# dict("first name"="John") # SyntaxError: 공백이 있는 키는 사용할 수 없다.

# 방법 2-3: 리스트의 튜플 쌍으로부터 생성
# 리스트나 튜플의 리스트/튜플을 사용하여 Dictionary를 생성할 수 있다.
dict_from_list = dict([("name", "Alice"), ("age", 25), ("city", "New York")])
#print(dict_from_list) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 튜플의 튜플로부터 생성
dict_from_tuple = dict((("name", "Bob"), ("age", 30), ("city", "London")))
#print(dict_from_tuple) # {'name': 'Bob', 'age': 30, 'city': 'London'}

# ============================================================================
# 방법 3: zip() 함수를 사용한 Dictionary 생성
# ============================================================================
# 두 개의 리스트(또는 튜플)를 키와 값으로 결합하여 Dictionary를 생성할 수 있다.

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
dict_from_zip = dict(zip(keys, values)) # zip() 함수로 키-값 쌍을 만들고 dict()로 변환한다.
#print(dict_from_zip) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 튜플을 사용한 예제
keys_tuple = ("name", "age", "city")
values_tuple = ("Bob", 30, "London")
dict_from_zip_tuple = dict(zip(keys_tuple, values_tuple))
#print(dict_from_zip_tuple) # {'name': 'Bob', 'age': 30, 'city': 'London'}

# 주의: 키와 값의 개수가 다를 경우, 짧은 쪽에 맞춰진다.
short_keys = ["a", "b"]
long_values = [1, 2, 3]
dict_unequal = dict(zip(short_keys, long_values))
#print(dict_unequal) # {'a': 1, 'b': 2} (값 3은 무시됨)

# ============================================================================
# 방법 4: fromkeys() 메서드를 사용한 Dictionary 생성
# ============================================================================
# 동일한 값으로 여러 키를 가진 Dictionary를 생성할 때 유용하다.

# 기본값이 None인 Dictionary 생성
keys = ["name", "age", "city"]
dict_fromkeys = dict.fromkeys(keys) # 모든 키의 값이 None으로 설정된다.
#print(dict_fromkeys) # {'name': None, 'age': None, 'city': None}

# 기본값을 지정한 Dictionary 생성
dict_fromkeys_default = dict.fromkeys(keys, "Unknown") # 모든 키의 값이 "Unknown"으로 설정된다.
#print(dict_fromkeys_default) # {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# 주의: fromkeys()는 모든 키에 동일한 값을 할당한다.
# 만약 가변 객체(리스트 등)를 기본값으로 사용하면, 모든 키가 같은 객체를 참조한다.
dict_list_default = dict.fromkeys(["a", "b", "c"], [])
dict_list_default["a"].append(1) # "a"의 리스트에 추가하면
#print(dict_list_default) # {'a': [1], 'b': [1], 'c': [1]} (모든 키의 리스트가 변경됨!)

# 올바른 방법: 각 키에 독립적인 리스트를 할당하려면 Dictionary Comprehension 사용
dict_list_correct = {key: [] for key in ["a", "b", "c"]}
dict_list_correct["a"].append(1)
#print(dict_list_correct) # {'a': [1], 'b': [], 'c': []} (각각 독립적)

# ============================================================================
# 방법 5: Dictionary Comprehension을 사용한 Dictionary 생성
# ============================================================================
# Dictionary Comprehension을 사용하면 조건을 적용하거나 변형을 통해 Dictionary를 생성할 수 있다.

# 기본 Dictionary Comprehension
squares = {x: x * x for x in range(6)} # 0부터 5까지의 제곱 Dictionary
#print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 조건부 Dictionary Comprehension
even_squares = {x: x * x for x in range(10) if x % 2 == 0} # 짝수만 제곱
#print(even_squares) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 기존 Dictionary에서 새 Dictionary 생성
original = {"a": 1, "b": 2, "c": 3, "d": 4}
doubled = {k: v * 2 for k, v in original.items()} # 모든 값을 2배
#print(doubled) # {'a': 2, 'b': 4, 'c': 6, 'd': 8}

# 키와 값을 바꾸기
swapped = {v: k for k, v in original.items()} # 키와 값을 바꾼다.
#print(swapped) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 복잡한 조건부 Dictionary Comprehension
filtered = {k: v for k, v in original.items() if v > 2} # 값이 2보다 큰 항목만
#print(filtered) # {'c': 3, 'd': 4}

# 문자열 처리 예제
words = ["apple", "banana", "cherry"]
length_dict = {word: len(word) for word in words} # 각 단어의 길이
#print(length_dict) # {'apple': 5, 'banana': 6, 'cherry': 6}

# ============================================================================
# 방법 6: 기존 Dictionary를 복사하여 생성
# ============================================================================
# 기존 Dictionary를 기반으로 새로운 Dictionary를 생성할 수 있다.

original_dict = {"name": "Alice", "age": 25}

# 방법 6-1: copy() 메서드 사용
copied_dict1 = original_dict.copy() # 얕은 복사(shallow copy)
#print(copied_dict1) # {'name': 'Alice', 'age': 25}

# 방법 6-2: dict() 함수 사용
copied_dict2 = dict(original_dict) # 얕은 복사(shallow copy)
#print(copied_dict2) # {'name': 'Alice', 'age': 25}

# 방법 6-3: Dictionary Comprehension 사용
copied_dict3 = {k: v for k, v in original_dict.items()} # 얕은 복사(shallow copy)
#print(copied_dict3) # {'name': 'Alice', 'age': 25}

# 방법 6-4: ** 연산자 사용 (Python 3.5+)
copied_dict4 = {**original_dict} # 얕은 복사(shallow copy)
#print(copied_dict4) # {'name': 'Alice', 'age': 25}

# ============================================================================
# 중첩 Dictionary 생성
# ============================================================================
# Dictionary 안에 Dictionary를 포함할 수 있다.

# 중첩 Dictionary 생성
nested_dict = {
    "person1": {"name": "Alice", "age": 25, "city": "New York"},
    "person2": {"name": "Bob", "age": 30, "city": "London"},
    "person3": {"name": "Charlie", "age": 35, "city": "Paris"}
}
#print(nested_dict)

# Dictionary Comprehension으로 중첩 Dictionary 생성
nested_comprehension = {
    f"person{i}": {"name": name, "age": age}
    for i, (name, age) in enumerate([("Alice", 25), ("Bob", 30), ("Charlie", 35)], 1)
}
#print(nested_comprehension)

# ============================================================================
# Dictionary 생성 방법 선택 가이드
# ============================================================================
# | 상황                              | 권장 방법                    | 이유                          |
# |----------------------------------|----------------------------|------------------------------|
# | 간단한 Dictionary 생성              | 중괄호 {} 사용               | 가장 직관적이고 빠름            |
# | 함수 인자로 전달                    | dict() 키워드 인자            | 함수 호출 시 편리함             |
# | 리스트/튜플 데이터 변환              | dict() + 리스트/튜플          | 기존 데이터 구조 활용           |
# | 별도의 키/값 리스트 결합             | zip() + dict()               | 두 리스트를 효율적으로 결합      |
# | 동일한 값으로 여러 키 초기화          | fromkeys()                   | 간결하고 명확함                 |
# | 조건부 생성 또는 변형 필요            | Dictionary Comprehension    | 유연하고 표현력이 높음           |
# | 기존 Dictionary 복사                | copy() 또는 dict()           | 명시적이고 안전함               |
# ============================================================================

# ============================================================================
# 주의사항
# ============================================================================
# 1. Dictionary의 키는 불변 객체만 가능하다 (문자열, 숫자, 튜플 등).
#    List는 키로 사용할 수 없다: invalid_dict = {[1, 2]: "error"} # TypeError
#
# 2. 동일한 키가 여러 번 사용되면 마지막 값이 이전 값을 덮어쓴다.
#    my_dict = {"a": 1, "a": 2} # {"a": 2} (마지막 값만 유지)
#
# 3. dict() 함수의 키워드 인자 방식은 키가 문자열이고 유효한 식별자여야 한다.
#    dict(1="one") # SyntaxError
#    dict("first name"="John") # SyntaxError
#
# 4. fromkeys()로 가변 객체를 기본값으로 사용하면 모든 키가 같은 객체를 참조한다.
#    dict.fromkeys(["a", "b"], []) # 주의: 모든 키가 같은 리스트를 참조
#
# 5. zip()을 사용할 때 키와 값의 개수가 다르면 짧은 쪽에 맞춰진다.
#
# 6. Dictionary Comprehension은 복잡한 조건이나 변형이 필요할 때 유용하다.
# ============================================================================