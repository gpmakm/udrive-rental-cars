def filterEvenNums(l):
    return (x for x in l if x % 2==0)

def filterOddNums(l):
    return (m for m in l if m%2!=0)

def filterGreathan(l,num):
    return (n for n in l if n> num)

def filterLessThan(l,num):
    return (x for x in l if x<num)

def filterGreaterThanOrEqualTo(l,num):
    return (x for x in l if x>=num)

def filterLessThanOrEqualTo(l,num):
    return (x for x in l if x<=num)

