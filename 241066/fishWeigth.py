

data = []

while True:

    temp = input()

    if(temp.lower() == "max" or temp.lower() == "min"):
       
        if temp.lower() == "min":

            for i in range(len(data)):
                for j in range(len(data)-i-1):
                    if data[j] > data[j+1]:
                        data[j],data[j+1] = data[j+1],data[j]
        
        else:
            for i in range(len(data)):
                for j in range(len(data)-i-1):
                    if data[j] < data[j+1]:
                        data[j],data[j+1] = data[j+1],data[j]
        break

    else:
        if(int(temp) > 0):
            data.append(int(temp)) 
    
for n in data:
    print(n,end=" ")