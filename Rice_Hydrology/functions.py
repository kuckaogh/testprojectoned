def zeros(size):
    output = ['NA']
    for i in range(0,size):
        output.append(0)
    return output   

def zeros_2D(sizeX, sizeY):
    output = [['NA']]
    for i in range(0,sizeX):
        output.append(zeros(sizeY))
    return output    


        
    