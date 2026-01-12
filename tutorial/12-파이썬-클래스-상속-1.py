# 클래스와 객체
# 클래스는 객체를 만드는 템플릿이고, 객체는 클래스의 인스턴스이다.

# ============================================================================
# 기본 클래스 정의
# ============================================================================

class Person:
    """사람을 나타내는 클래스"""
    pass

# 객체 생성
person1 = Person()
person2 = Person()

# ============================================================================
# 속성 (Attributes)
# ============================================================================

class Person:
    """사람을 나타내는 클래스"""
    pass

person = Person()
person.name = "Alice" # 동적으로 속성 추가
person.age = 25

#print(person.name) # "Alice"
#print(person.age) # 25

# ============================================================================
# __init__ 메서드 (생성자)
# ============================================================================

class Person:
    """사람을 나타내는 클래스"""
    
    def __init__(self, name, age):
        """생성자: 객체 초기화"""
        self.name = name
        self.age = age

person = Person("Alice", 25)
#print(person.name) # "Alice"
#print(person.age) # 25

# ============================================================================
# 메서드 (Methods)
# ============================================================================

class Person:
    """사람을 나타내는 클래스"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """자기소개 메서드"""
        #print(f"My name is {self.name} and I am {self.age} years old.")
        pass

person = Person("Alice", 25)
person.introduce() # "My name is Alice and I am 25 years old."

# ============================================================================
# self 키워드
# ============================================================================
# self는 객체 자신을 가리키는 참조이다.

class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

person = Person("Alice")
name = person.get_name()
#print(name) # "Alice"

# ============================================================================
# 클래스 변수와 인스턴스 변수
# ============================================================================

class Person:
    # 클래스 변수 (모든 인스턴스가 공유)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # 인스턴스 변수 (각 인스턴스마다 독립적)
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

#print(person1.species) # "Homo sapiens"
#print(person2.species) # "Homo sapiens"

# 클래스 변수 변경 (모든 인스턴스에 영향)
Person.species = "Human"
#print(person1.species) # "Human"
#print(person2.species) # "Human"

# ============================================================================
# __str__ 메서드
# ============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """문자열 표현"""
        return f"Person(name={self.name}, age={self.age})"

person = Person("Alice", 25)
#print(person) # Person(name=Alice, age=25)

# ============================================================================
# __repr__ 메서드
# ============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        """개발자용 문자열 표현"""
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 25)
#print(repr(person)) # Person('Alice', 25)

# ============================================================================
# private 속성과 메서드 (관례)
# ============================================================================
# Python은 진짜 private을 지원하지 않지만, 언더스코어로 관례를 표시한다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected (관례)
        self.__secret = "secret"  # private (name mangling)
    
    def _protected_method(self):
        """protected 메서드 (관례)"""
        pass
    
    def __private_method(self):
        """private 메서드 (name mangling)"""
        pass

person = Person("Alice", 25)
#print(person._age) # 접근 가능하지만 관례상 사용하지 않음
# print(person.__secret) # AttributeError (name mangling으로 _Person__secret로 변경됨)

# ============================================================================
# 속성 접근 제어 (Property)
# ============================================================================

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """name 속성 getter"""
        return self._name
    
    @name.setter
    def name(self, value):
        """name 속성 setter"""
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")
    
    @property
    def age(self):
        """age 속성 getter"""
        return self._age
    
    @age.setter
    def age(self, value):
        """age 속성 setter"""
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer")

person = Person("Alice", 25)
#print(person.name) # "Alice"
person.name = "Bob"
#print(person.name) # "Bob"

# ============================================================================
# 클래스 메서드와 정적 메서드
# ============================================================================

class Person:
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """클래스 메서드: 출생 연도로 객체 생성"""
        from datetime import datetime
        age = datetime.now().year - birth_year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        """정적 메서드: 나이로 성인 여부 확인"""
        return age >= 18

person1 = Person("Alice", 25)
person2 = Person.from_birth_year("Bob", 1990)

#print(Person.is_adult(20)) # True
#print(Person.is_adult(15)) # False

# ============================================================================
# 주의사항
# ============================================================================
# 1. 클래스 이름은 대문자로 시작하는 것이 관례이다 (PascalCase).
# 2. self는 메서드의 첫 번째 매개변수로 항상 필요하다.
# 3. __init__ 메서드는 생성자 역할을 하지만 실제로는 초기화 메서드이다.
# 4. 클래스 변수와 인스턴스 변수를 구분해서 사용해야 한다.
# 5. property를 사용하여 속성 접근을 제어할 수 있다.
# ============================================================================
