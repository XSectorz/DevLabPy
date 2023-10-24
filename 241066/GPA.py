

data = []

currentGPA = 0

for i in range(5):
    grade = float(input())
    data.append(grade)
    currentGPA += grade


print("THAI = " + str(data[0]))
print("MATH = " + str(data[1]))
print("ENGLISH = " + str(data[2]))
print("SCIENCE = " + str(data[3]))
print("SPORT = " + str(data[4]))
print("---")
print("GPA = " + str(currentGPA/5))