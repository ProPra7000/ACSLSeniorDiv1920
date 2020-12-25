for i in range(5):
    initialinput = str(input("Enter your Input: "))
    array = list(map(str, initialinput.split()))
    num = 0
    for i in range(0, len(array)):
        if (array[i] != "|" and array[i] != "+" and array[i] != "-" and array[i] != "-" and array[i] != "*" and array[i] != "@" and array[i] != ">"):
            array[i] = int(array[i])
    while (len(array) > 1):
        for i in range(0, len(array)):
            if (i <= len(array) - 3):
                if (array[i] == "@" and isinstance(array[i+1], int) and isinstance(array[i+2], int) and isinstance(array[i+3], int)):
                    if (array[i + 1] > 0):
                        num = array[i + 2]
                    else:
                        num = array[i + 3]
                    array[i + 3] = num
                    array.pop(i)
                    array.pop(i)
                    array.pop(i)
                if (array[i] == ">" and isinstance(array[i+1], int) and isinstance(array[i+2], int) and isinstance(array[i+3], int)):
                    array[i + 3] = max(array[i + 1], array[i + 2], array[i + 3])
                    array.pop(i)
                    array.pop(i)
                    array.pop(i)
            if (i <= len(array) - 2):
                if (array[i] == "+" and isinstance(array[i+1], int) and isinstance(array[i+2], int)):
                    array[i + 2] = array[i + 1] + array[i + 2]
                    array.pop(i)
                    array.pop(i)
                elif (array[i] == "-" and isinstance(array[i+1], int) and isinstance(array[i+2], int)):
                    array[i + 2] = array[i + 1] - array[i + 2]
                    array.pop(i)
                    array.pop(i)
                elif (array[i] == "*" and isinstance(array[i+1], int) and isinstance(array[i+2], int)):
                    array[i + 2] = array[i + 1] * array[i + 2]
                    array.pop(i)
                    array.pop(i)
            if (i <= len(array) - 1):
                if (array[i] == "|" and isinstance(array[i + 1], int)):
                    array[i + 1] = abs(array[i + 1])
                    array.pop(i)
    for i in array:
        print(i)