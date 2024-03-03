pi = 3,14159
def calculate_circle_area(radius):
    return pi*radius**2
    
r = int(input('Enter the radius of the circle: '))
area = calculate_circle_area(r)
print (area)
