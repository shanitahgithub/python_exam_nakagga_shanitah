# a) i)Grades that the students will be receiving
mark=int(input('Enter student mark:'))
def grade_students(mark):
    
    if mark >=90 and mark <=100:
        print('Grade A')
    elif mark >=80 and mark <=89:
        print('Grade B')
    elif mark >=70 and mark <=79:
        print('Grade C')
    elif mark >=60 and mark <=69:
        print('Grade D')
    elif mark >=50 and mark <=59:
        print('Grade E')
    else:
        print('Grade F')
grade_students(mark)

# ii) Convert temperatures to and from Celcius and Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    print(fahrenheit)
celsius_to_fahrenheit(25)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    print( celsius)
fahrenheit_to_celsius(25)


# b) i) Area of a triangle
def calculate_area(base,height):
    area_of_the_triangle=1/2*(base * height)
    print(area_of_the_triangle)
calculate_area(2,3)

# ii) Suming up all numbers in a list
numbers=[9,2,3,5,8]
def sum(numbers):
    total=0
    for x in numbers:
        total+=x
    return total
sum(numbers)
print(f'The sum of numbers is {sum(numbers)}')



