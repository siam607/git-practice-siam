import datetime
from utils import add, subtract, multiply

print("Name: Md. Sabbir Ahmed Siam")
print("Today's Date:", datetime.date.today())

# Calculator functions call
result_add = add(10, 5)
result_sub = subtract(10, 5)
result_mul = multiply(10, 5)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")