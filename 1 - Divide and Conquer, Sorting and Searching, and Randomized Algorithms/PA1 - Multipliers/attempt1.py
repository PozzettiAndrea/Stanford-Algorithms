
def thirdgrademultiplier(x,y):
    """takes in two values, x and y, and multiplies them according to the most commonly taught algorithm
    for multiplication, creating rows digit by digit and then summing them to give the final result"""
    sx = str(x)
    sy = str(y)
    rows = []
    count = 0
    for a in sx[::-1]:
        row = []
        for m in range(count):
            row.append(0)
        for b in sy[::-1]:
            tot = (int(a)*int(b))
            row.append(tot)
        for i in range(len(row)):
            if row[i]>9:
                try:
                    row[i+1] += row[i]//10
                    row[i] = row[i]%10
                except:
                    row.append(row[i]//10)
                    row[i] = row[i]%10
        rows.append(row)
        count +=1
        result = 
    print(rows)



thirdgrademultiplier(14,260)
ad = 10
bc = 10
meh = str(ad%bc)
print(meh)
def karatsubamultiplier(x,y):
    sx = str(x)
    sy = str(y)
    lenx = len(sx)
    leny = len(sy)
    s1x = sx[:lenx//2]
    s2x = sx[lenx//2:]
    s1y = sy[:leny//2]
    s2y = sy[leny//2:]
    print(s1x,"\n",s2x,"\n",s1y,"\n",s2y,"\n")
    
karatsubamultiplier(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)