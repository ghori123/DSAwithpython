def Bubble(data):
    for i in range(len(data)):
        for j in range(0,(len(data)-1-i)):
            if data[j] > data[j+1]:# for incriment order > // and decrition order <
                data[j+1], data[j] = data[j], data[j+1]
    return data


R_data = Bubble([64,32,25,45,20,15])
print(R_data)
