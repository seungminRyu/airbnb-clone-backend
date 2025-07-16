class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        print(f"{brand} {model} 교통수단이 생성되었습니다.")

    def start_engine(self):
        return "이동수단의 엔진이 시동되었습니다."

    def drive(self, distance):
        self.mileage += distance
        return f"{distance}km 주행했습니다. 총 주행거리: {self.mileage}km"

    def get_info(self):
        return f"{self.year}년 {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
        print(f"승용차가 생성되었습니다. 문 개수: {doors}개")

    def start_engine(self):
        return "자동차 엔진이 부드럽게 시동되었습니다!"

    def open_trunk(self):
        return f"{self.brand} {self.model}의 트렁크를 열었습니다."


class Truck(Vehicle):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

        print(f"트럭이 생성되었습니다. 적재량: {load_capacity}톤")

    def start_engine(self):
        parent_message = super().start_engine()
        return parent_message + " (트럭의 큰 엔진소리!)"

    def load_cargo(self, weight):
        if weight <= self.load_capacity:
            return f"{weight}톤 화물을 적재했습니다."
        else:
            return f"적재량 초과! 최대 {self.load_capacity}톤 까지 가능합니다."


car = Car("현대", "소나타", 2023, 4)
truck = Truck("볼보", "Test", 2011, 25)


print(car.start_engine())
print(truck.start_engine())


class A:
    def do(self):
        print("A의 Do")


class B(A):
    def do(self):
        print("B의 Do")
        super().do()


class C(A):
    def do(self):
        print("C의 Do")
        super().do()


class D(B, C):
    def do(self):
        print("D의 Do")
        super().do()


d = D()
d.do()

print("현재 스코프의 이름들:", dir())

s = "string"
print("문자열 s의 속성/메서드:", dir(s))


lst = [1, 2, 3]
print("리스트:", dir(lst))

print("클래스:", dir(car))
