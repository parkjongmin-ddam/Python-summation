# 매개변수와 인자
# 함수의 매개변수와 인자에 대한 상세 설명

# ============================================================================
# 위치 인자 (Positional Arguments)
# ============================================================================

def greet(name, age):
    """위치 인자를 받는 함수"""
    #print(f"{name} is {age} years old")
    pass

greet("Alice", 25) # 위치에 따라 name="Alice", age=25

# ============================================================================
# 키워드 인자 (Keyword Arguments)
# ============================================================================

def greet(name, age):
    """키워드 인자를 받는 함수"""
    #print(f"{name} is {age} years old")
    pass

greet(name="Alice", age=25) # 키워드로 명시
greet(age=25, name="Alice") # 순서 무관

# ============================================================================
# 기본값이 있는 매개변수 (Default Parameters)
# ============================================================================

def greet(name="World", age=0):
    """기본값이 있는 매개변수"""
    #print(f"{name} is {age} years old")
    pass

greet() # name="World", age=0
greet("Alice") # name="Alice", age=0
greet("Alice", 25) # name="Alice", age=25
greet(age=25) # name="World", age=25

# ============================================================================
# 가변 위치 인자 (*args)
# ============================================================================

def sum_all(*args):
    """임의의 개수의 인자를 받는 함수"""
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
#print(result) # 15

# 리스트 언패킹
numbers = [1, 2, 3, 4, 5]
result = sum_all(*numbers) # * 연산자로 언패킹
#print(result) # 15

# ============================================================================
# 가변 키워드 인자 (**kwargs)
# ============================================================================

def print_info(**kwargs):
    """임의의 개수의 키워드 인자를 받는 함수"""
    for key, value in kwargs.items():
        #print(f"{key}: {value}")
        pass

print_info(name="Alice", age=25, city="New York")

# 딕셔너리 언패킹
info = {"name": "Alice", "age": 25, "city": "New York"}
print_info(**info) # ** 연산자로 언패킹

# ============================================================================
# 매개변수 순서 규칙
# ============================================================================
# 1. 일반 매개변수
# 2. *args
# 3. 키워드 전용 매개변수 (기본값 있음)
# 4. **kwargs

def example_function(pos1, pos2, *args, keyword1="default", keyword2="default", **kwargs):
    """매개변수 순서 예제"""
    #print(f"pos1: {pos1}, pos2: {pos2}")
    #print(f"args: {args}")
    #print(f"keyword1: {keyword1}, keyword2: {keyword2}")
    #print(f"kwargs: {kwargs}")
    pass

example_function(1, 2, 3, 4, keyword1="value1", extra="value2")
# pos1: 1, pos2: 2
# args: (3, 4)
# keyword1: value1, keyword2: default
# kwargs: {'extra': 'value2'}

# ============================================================================
# 키워드 전용 매개변수 (* 이후의 매개변수)
# ============================================================================

def example_function(pos, *, keyword_only):
    """키워드 전용 매개변수"""
    #print(f"pos: {pos}, keyword_only: {keyword_only}")
    pass

example_function(1, keyword_only=2) # 올바른 사용
# example_function(1, 2) # TypeError: 키워드 전용 매개변수는 키워드로 전달해야 함

# ============================================================================
# 가변 기본값 주의사항
# ============================================================================
# 가변 객체(리스트, 딕셔너리)를 기본값으로 사용하면 안 된다.

# 잘못된 예
def add_item(item, items=[]): # 주의: 가변 기본값
    items.append(item)
    return items

# 올바른 예
def add_item_correct(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# ============================================================================
# 매개변수 타입 힌트
# ============================================================================

def add(a: int, b: int) -> int:
    """타입 힌트가 있는 함수"""
    return a + b

from typing import List, Dict, Optional

def process_data(numbers: List[int], config: Optional[Dict[str, str]] = None) -> List[int]:
    """타입 힌트 예제"""
    if config is None:
        config = {}
    return [n * 2 for n in numbers]

# ============================================================================
# 주의사항
# ============================================================================
# 1. 기본값이 있는 매개변수는 기본값이 없는 매개변수 뒤에 와야 한다.
# 2. 가변 객체를 기본값으로 사용하지 않는다.
# 3. *args와 **kwargs는 관례적인 이름이며, 다른 이름을 사용할 수 있다.
# 4. 키워드 전용 매개변수는 * 이후에 정의한다.
# ============================================================================
