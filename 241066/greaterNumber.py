
data = []

for i in range(3):
    temp = int(input())

    data.append(temp)

maxNum = -9999999
for i in range(3):
    maxNum = max(data[i],maxNum)

print("MAX : " + maxNum)