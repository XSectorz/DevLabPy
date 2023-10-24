score = int(input())

if score > 100:
    print("Error : Value must be less than or equal to 100.")
elif score>=90:
    print("A")
elif score >= 85:
    print("B+")
elif score >= 80:
    print("B")
elif score >= 75:
    print("C+")
elif score >= 70:
    print("C")
elif score >= 65:
    print("D+")
elif score >= 60:
    print("D")
elif score >= 0:
    print("F")
else:
    print("Error : Value must be greater than or equal to 0.")