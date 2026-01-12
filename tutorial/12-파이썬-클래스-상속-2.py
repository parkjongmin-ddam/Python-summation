# 상속 (Inheritance)
# 상속은 기존 클래스를 확장하여 새로운 클래스를 만드는 것이다.

# ============================================================================
# 기본 상속
# ============================================================================

class Animal:
    """동물 클래스 (부모 클래스)"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        #print(f"{self.name} makes a sound")
        pass

class Dog(Animal):
    """개 클래스 (자식 클래스)"""
    
    def speak(self):
        #print(f"{self.name} barks")
        pass

dog = Dog("Buddy")
dog.speak() # "Buddy barks"

# ============================================================================
# super() 함수
# ============================================================================

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # 부모 클래스의 __init__ 호출
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
#print(dog.name) # "Buddy"
#print(dog.breed) # "Golden Retriever"

# ============================================================================
# 메서드 오버라이딩
# ============================================================================

class Animal:
    def speak(self):
        #print("Animal makes a sound")
        pass

class Dog(Animal):
    def speak(self):
        #print("Dog barks") # 부모 클래스의 메서드를 오버라이딩
        pass

class Cat(Animal):
    def speak(self):
        #print("Cat meows") # 부모 클래스의 메서드를 오버라이딩
        pass

dog = Dog()
cat = Cat()
dog.speak() # "Dog barks"
cat.speak() # "Cat meows"

# ============================================================================
# 다중 상속
# ============================================================================

class Flyable:
    def fly(self):
        #print("Flying")
        pass

class Swimmable:
    def swim(self):
        #print("Swimming")
        pass

class Duck(Animal, Flyable, Swimmable):
    """오리 클래스: 다중 상속"""
    pass

duck = Duck("Donald")
duck.speak() # Animal의 메서드
duck.fly() # Flyable의 메서드
duck.swim() # Swimmable의 메서드

# ============================================================================
# Method Resolution Order (MRO)
# ============================================================================

class A:
    def method(self):
        #print("A")
        pass

class B(A):
    def method(self):
        #print("B")
        pass

class C(A):
    def method(self):
        #print("C")
        pass

class D(B, C):
    pass

# MRO 확인
#print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# ============================================================================
# isinstance()와 issubclass()
# ============================================================================

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# isinstance: 객체가 특정 클래스의 인스턴스인지 확인
#print(isinstance(dog, Dog)) # True
#print(isinstance(dog, Animal)) # True

# issubclass: 클래스가 다른 클래스의 서브클래스인지 확인
#print(issubclass(Dog, Animal)) # True
#print(issubclass(Animal, Dog)) # False

# ============================================================================
# 추상 클래스 (ABC)
# ============================================================================

from abc import ABC, abstractmethod

class Shape(ABC):
    """추상 클래스"""
    
    @abstractmethod
    def area(self):
        """면적을 계산하는 추상 메서드"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """둘레를 계산하는 추상 메서드"""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 3)
#print(rectangle.area()) # 15
#print(rectangle.perimeter()) # 16

# ============================================================================
# 주의사항
# ============================================================================
# 1. super()를 사용하여 부모 클래스의 메서드를 호출할 수 있다.
# 2. 다중 상속 시 MRO를 이해하는 것이 중요하다.
# 3. 추상 클래스를 사용하여 인터페이스를 정의할 수 있다.
# 4. isinstance()와 issubclass()로 타입을 확인할 수 있다.
# ============================================================================
