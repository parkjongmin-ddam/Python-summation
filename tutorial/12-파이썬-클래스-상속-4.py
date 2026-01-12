# 캡슐화 (Encapsulation)
# 캡슐화는 데이터와 메서드를 하나의 단위로 묶고, 외부에서 직접 접근을 제한하는 것이다.

# ============================================================================
# 접근 제어 (관례)
# ============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name  # public
        self._age = age  # protected (관례)
        self.__secret = "secret"  # private (name mangling)

person = Person("Alice", 25)
#print(person.name) # 접근 가능
#print(person._age) # 접근 가능하지만 관례상 사용하지 않음
# print(person.__secret) # AttributeError

# ============================================================================
# Property를 사용한 캡슐화
# ============================================================================

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """name getter"""
        return self._name
    
    @name.setter
    def name(self, value):
        """name setter"""
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def age(self):
        """age getter"""
        return self._age
    
    @age.setter
    def age(self, value):
        """age setter"""
        if isinstance(value, int) and 0 <= value <= 150:
            self._age = value
        else:
            raise ValueError("Age must be between 0 and 150")

person = Person("Alice", 25)
#print(person.name) # "Alice"
person.name = "Bob"
#print(person.name) # "Bob"

# ============================================================================
# 읽기 전용 속성
# ============================================================================

class Person:
    def __init__(self, name, birth_year):
        self._name = name
        self._birth_year = birth_year
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        from datetime import datetime
        return datetime.now().year - self._birth_year

person = Person("Alice", 1990)
#print(person.name) # "Alice"
#print(person.age) # 현재 연도 - 1990
# person.age = 30 # AttributeError: can't set attribute

# ============================================================================
# 주의사항
# ============================================================================
# 1. Python은 진짜 private을 지원하지 않지만, 관례와 name mangling을 사용한다.
# 2. Property를 사용하여 속성 접근을 제어할 수 있다.
# 3. 캡슐화는 데이터 무결성을 보장하고 코드를 더 안전하게 만든다.
# ============================================================================
