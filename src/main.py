import datetime

print("Name: Md. Sabbir Ahmed Siam")
print("Today's Date:", datetime.date.today())


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

from utils import add, subtract


print("Name: Md. Sabbir Ahmed Siam")
print("Today's Date:", datetime.date.today())


result_add = add(10, 5)
result_sub = subtract(10, 5)
print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")