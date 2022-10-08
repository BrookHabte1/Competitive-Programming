    import math
    inputs = input()
    inputsArray = list(map(int,inputs.split()))
    x=0
    y=0
    x = math.ceil(inputsArray[0]/inputsArray[2])
    y = math.ceil(inputsArray[1]/inputsArray[2])
    if inputsArray[0]%inputsArray[2]!=0:
      X =x + 1
    elif inputsArray[1]%inputsArray[2]!=0:
      y+=1
    sums= x+y
    print(sums)
    