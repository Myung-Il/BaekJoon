class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age

# 객체 생성
p1 = Person("Alice", 20)
p2 = Person("Alice", 30)
p3 = p1

# p1과 p2는 값이 같고 동일한 클래스 인스턴스이지만,
# 별도의 객체이므로 메모리 주소는 다릅니다.
print(p1 == p2) # 출력: True (__eq__ 메서드에 의해 값 동등성 비교)
print(p1 is p2) # 출력: False

# p1과 p3는 동일한 객체를 가리키므로 메모리 주소가 같습니다.
print(p1 == p3) # 출력: True
print(p1 is p3) # 출력: True
