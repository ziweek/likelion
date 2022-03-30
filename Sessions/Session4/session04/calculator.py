class Calculator:
    # 여기에 코드를 작성해보세요!
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    def mul(self, num):
        self.result *= num
        return self.result
    def div(self, num):
        self.result /= num
        return self.result

calculator1 = Calculator('짱구', 5)
calculator2 = Calculator('맹구', 5)

print(calculator1.name)
print(calculator1.age)