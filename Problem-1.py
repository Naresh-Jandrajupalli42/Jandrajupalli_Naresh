class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

# Taking user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add/subtract/multiply/divide): ").strip().lower()

# Create Calculator instance and perform operation
calc = Calculator()
if operation == "add":
    result = calc.add(a, b)
elif operation == "subtract":
    result = calc.subtract(a, b)
elif operation == "multiply":
    result = calc.multiply(a, b)
elif operation == "divide":
    result = calc.divide(a, b)
else:
    result = "Error: Invalid operation"

print("Result:", result)

