def divide_five_by(number):
    try:
        value = 5 / number
    except ZeroDivisionError:
        value = 1
    return value
print(divide_five_by(2))
print(divide_five_by(0))
         