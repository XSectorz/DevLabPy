
n = int(input())

data = []
dataSizeByIndex = []

for i in range(n):
    dataInput = input()
    data.append(dataInput)
    dataSizeByIndex.append(len(dataInput))

#for i in range(len(data)):
#    print(data[i] + " LEN " + str(dataSizeByIndex[i]))

#Bubble Sort
for i in range(len(data)-1):
    for j in range(len(data)-i-1):
        
        if(dataSizeByIndex[j] > dataSizeByIndex[j+1]):
            dataSizeByIndex[j],dataSizeByIndex[j+1] = dataSizeByIndex[j+1],dataSizeByIndex[j]
            data[j],data[j+1] = data[j+1],data[j]
            

#print("AFTER SORT")
for i in range(len(data)):
    #print(data[i] + " LEN " + str(dataSizeByIndex[i]))
    print(data[i])

