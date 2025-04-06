class Calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a,b):
        return a-b
    def mult(self, a,b):
        return a*b
    def div(self, a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Error: Division by Zero")
            
calculator = Calculator()

print(calculator.add(1,5))
print(calculator.sub(1,5))
print(calculator.mult(1,5))
print(calculator.div(1,0))