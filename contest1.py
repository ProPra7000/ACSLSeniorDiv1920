import math
for a in range(5):
    def factors(x):
        result = []
        i = 1
        while i * i <= x:
            if x % i == 0:
                result.append(i)
                if x // i != i:
                    result.append(x // i)
            i += 1
        return result
    def is_prime(n):
        if n == 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    inputt = str(input("Enter your Input: "))
    inputarray = list(map(str, inputt.split()))
    num = int(inputarray[0])
    array = []
    primefactors = []
    nopf = 0
    newarray = []
    final = " "
    pos = len(inputarray[0]) - int(inputarray[1])
    x = 2
    for i in inputarray[0]:
        array.append(int(i))
    factors = factors(num)
    factors.pop(0)
    factors.pop(0)
    for e in factors:
        if is_prime(e) == True:
            primefactors.append(e)
    posofnum = array[len(array) - int(inputarray[1])]
    nopf = len(primefactors)
    pos = len(inputarray[0]) - int(inputarray[1])
    num = str(num)
    for i in range(0, pos):
        newarray.append(int(num[i]) + int(num[pos]))
    newarray.append(nopf)
    for i in range(pos + 1, len(num)):
        newarray.append(int(math.fabs(int(num[i]) - int(num[pos]))))
    for i in newarray:
        final += str(i)
    print(final[1:len(final)])