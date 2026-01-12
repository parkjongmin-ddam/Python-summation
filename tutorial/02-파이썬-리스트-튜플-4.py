# Tuple(튜플) 자료형
# Tuple은 여러 개의 값을 하나의 변수에 저장할 수 있는 순서가 있는 자료형이다.
# Tuple은 소괄호 () 를 사용하여 표현한다.
# Tuple은 아래와 같은 특징을 가지고 있다:
# 불변성(Immutable): Tuple은 요소의 추가, 삭제, 변경이 불가능하다 (생성 후 수정 불가)
# 인덱싱(Indexing): Tuple의 각 요소는 Index를 통해 접근할 수 있다 (첫번째 요소는 0번 Index, 두번째 요소는 1번 Index, ...)
# 슬라이싱(Slicing): Tuple의 일부분을 추출하기 위해 Slicing을 사용할 수 있으며, Slicing은 Tuple의 일부를 새로운 Tuple로 생성한다.
# 순서 보장: Tuple은 요소의 순서가 보장된다.

# ============================================================================
# Tuple vs List 비교표
# ============================================================================
# | 특징          | Tuple                      | List                        |
# |--------------|---------------------------|----------------------------|
# | 문법          | 소괄호 () 사용              | 대괄호 [] 사용              |
# | 불변성        | 불변 (Immutable)           | 가변 (Mutable)              |
# | 요소 수정     | 불가능                     | 가능                        |
# | 요소 추가     | 불가능                     | 가능                        |
# | 요소 삭제     | 불가능                     | 가능                        |
# | 메모리 효율   | 더 효율적 (작은 메모리 사용) | 상대적으로 더 많은 메모리 사용 |
# | 속도          | 더 빠름                    | 상대적으로 느림              |
# | 사용 시나리오  | 고정된 데이터, 딕셔너리 키   | 변경 가능한 데이터 모음      |
# ============================================================================

# ============================================================================
# Tuple 생성 방법
# ============================================================================

# 빈 Tuple 생성
empty_tuple = ()
#print(empty_tuple) # ()
#print(type(empty_tuple)) # <class 'tuple'>

# 기본적인 Tuple 생성
basic_tuple = (1, 2, 3, 4, 5)
#print(basic_tuple) # (1, 2, 3, 4, 5)
#print(type(basic_tuple)) # <class 'tuple'>

# 다양한 데이터 타입을 포함하는 Tuple 생성
datatypes_tuple = (1, "apple", 3.14, True, None)
#print(datatypes_tuple) # (1, 'apple', 3.14, True, None)

# Tuple 내 Tuple(중첩 Tuple) 생성
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#print(nested_tuple) # ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# 하나의 요소를 가진 Tuple 생성
# 주의: 하나의 요소만 있을 때는 반드시 쉼표(,)를 붙여야 한다.
single_tuple = (1,) # 쉼표가 있으면 Tuple
#print(single_tuple) # (1,)
#print(type(single_tuple)) # <class 'tuple'>

not_tuple = (1) # 쉼표가 없으면 정수형
#print(not_tuple) # 1
#print(type(not_tuple)) # <class 'int'>

# 쉼표만으로 Tuple 생성 (소괄호 생략 가능)
comma_tuple = 1, 2, 3, 4, 5 # 소괄호 없이도 Tuple 생성 가능
#print(comma_tuple) # (1, 2, 3, 4, 5)
#print(type(comma_tuple)) # <class 'tuple'>

# 하나의 요소를 가진 Tuple도 쉼표만으로 생성 가능
single_comma = 1, # 쉼표만으로도 단일 요소 Tuple 생성
#print(single_comma) # (1,)
#print(type(single_comma)) # <class 'tuple'>

# Tuple 생성자를 사용하여 Tuple 생성
tuple_from_list = tuple([1, 2, 3, 4, 5]) # 리스트를 Tuple로 변환
#print(tuple_from_list) # (1, 2, 3, 4, 5)

tuple_from_string = tuple("Python") # 문자열을 Tuple로 변환 (각 문자가 요소가 됨)
#print(tuple_from_string) # ('P', 'y', 't', 'h', 'o', 'n')

tuple_from_range = tuple(range(5)) # range를 Tuple로 변환
#print(tuple_from_range) # (0, 1, 2, 3, 4)

# ============================================================================
# Tuple 인덱싱과 슬라이싱
# ============================================================================
# Tuple도 List와 동일하게 인덱싱과 슬라이싱을 사용할 수 있다.

my_tuple = (1, 2, 3, 4, 5)

# 인덱싱: 특정 위치의 요소에 접근
first_element = my_tuple[0] # 첫 번째 요소
#print(first_element) # 1

last_element = my_tuple[-1] # 마지막 요소 (음수 인덱스 사용)
#print(last_element) # 5

# 슬라이싱: 일부분 추출
sub_tuple = my_tuple[1:4] # 1번 인덱스부터 3번 인덱스까지
#print(sub_tuple) # (2, 3, 4)

# ============================================================================
# Tuple Unpacking (튜플 언패킹)
# ============================================================================
# Tuple의 요소를 여러 변수에 한 번에 할당할 수 있다.

# 기본 언패킹
coordinates = (10, 20)
x, y = coordinates # Tuple의 요소를 각각 x, y에 할당
#print(x) # 10
#print(y) # 20

# 여러 값 반환 (함수에서 여러 값을 반환할 때 유용)
def get_name_age():
    return "Python", 30

name, age = get_name_age() # 함수가 반환한 Tuple을 언패킹
#print(name) # Python
#print(age) # 30

# 변수 교환 (임시 변수 없이 가능)
a, b = 1, 2
a, b = b, a # a와 b의 값을 교환
#print(a) # 2
#print(b) # 1

# 일부만 언패킹 (나머지는 *로 처리)
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers # 첫 번째 요소와 나머지
#print(first) # 1
#print(rest) # [2, 3, 4, 5] (리스트로 반환됨)

first, *middle, last = numbers # 첫 번째, 중간, 마지막 요소
#print(first) # 1
#print(middle) # [2, 3, 4]
#print(last) # 5

# ============================================================================
# Tuple의 불변성 (Immutable)
# ============================================================================
# Tuple은 생성 후 수정할 수 없다. 이는 Tuple의 가장 중요한 특징이다.

immutable_tuple = (1, 2, 3, 4, 5)

# 다음 코드들은 모두 에러가 발생한다:
# immutable_tuple[0] = 100 # TypeError: 'tuple' object does not support item assignment
# immutable_tuple.append(6) # AttributeError: 'tuple' object has no attribute 'append'
# immutable_tuple.remove(1) # AttributeError: 'tuple' object has no attribute 'remove'

# 하지만 Tuple 내부에 가변 객체(List 등)가 있으면, 그 객체는 수정 가능하다
mixed_tuple = (1, 2, [3, 4], 5)
mixed_tuple[2][0] = 100 # 내부 리스트는 수정 가능
#print(mixed_tuple) # (1, 2, [100, 4], 5)

# ============================================================================
# Tuple의 장점
# ============================================================================
# 1. 불변성: 데이터가 실수로 변경되는 것을 방지
# 2. 딕셔너리 키로 사용 가능: 불변 객체만 딕셔너리 키가 될 수 있음
# 3. 메모리 효율: List보다 메모리를 적게 사용
# 4. 성능: List보다 빠른 접근 속도
# 5. 함수 반환값: 여러 값을 한 번에 반환할 때 유용

# 딕셔너리 키로 사용 예제
coordinates_dict = {
    (0, 0): "원점",
    (1, 1): "대각선",
    (2, 2): "대각선"
}
#print(coordinates_dict[(0, 0)]) # "원점"

# List는 딕셔너리 키로 사용할 수 없음 (에러 발생)
# invalid_dict = {[1, 2]: "error"} # TypeError: unhashable type: 'list'