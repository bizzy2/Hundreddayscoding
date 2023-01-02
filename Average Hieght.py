
heights = (input('Input a list of student heights: ')).split()
print(heights)
a = []
for i in heights:
    a.append(int(i))

# to get total number of students
totalhights = 0
for i in a:
    totalhights += i
print(f'total students {totalhights}')
# to get number of students
number_of_students = 0
for i in heights:
    number_of_students += 1
print(f'total number of students {number_of_students}')

avrgh = round(totalhights/number_of_students)
print(f'Average height rounded to the nearest whole number = {avrgh}')
