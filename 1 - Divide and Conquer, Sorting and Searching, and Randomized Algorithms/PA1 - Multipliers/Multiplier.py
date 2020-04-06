n1 = 3141592653589793238462643383279502884197169399375105820974944592
n2 = 2718281828459045235360287471352662497757247093699959574966967627


def thirdgrademultiplier(x,y):
    """takes in two values, x and y, and multiplies them according to the most commonly taught algorithm
    for multiplication, creating rows digit by digit and then summing them to give the final result"""
    sx = str(x)
    sy = str(y)
    rows = []
    count = 0
    for a in sx[::-1]:
        row = []
        count2 = 0
        for b in sy[::-1]:
            row.append((int(a)*int(b)))
        for i in range(len(row)):
            row[i] *= 10**(i)
        rowtotal = sum(row)
        rows.append(rowtotal)
    for i in range(len(rows)):
            rows[i] *= 10**(i)
    return sum(rows)


def karatsubamultiplier(x,y):
    """takes in two n digit numbers, x and y, and multiplies them with the karatsuba algorithm"""
    sx = str(x)
    sy = str(y)
    lenx = len(sx)
    leny = len(sy)
    off = (lenx%2) + lenx//2
    if lenx != leny:
        print("Error. Numbers x and y must have same number of digits")
    else:
        a = sx[:lenx//2]
        b = sx[lenx//2:]
        c = sy[:leny//2]
        d = sy[leny//2:]
        one = thirdgrademultiplier(int(a),int(c))
        two = thirdgrademultiplier(int(b),int(d))
        three = thirdgrademultiplier(int(a)+int(b),int(c)+int(d))
        result = one*(10**(2*off)) + two + (three-two-one)*(10**(off))
        return result