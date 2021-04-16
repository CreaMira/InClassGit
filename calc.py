def calc(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    mylist = [sum, sub, mul,div]
    sum_of_list = mylist[0] + mylist[1] + mylist[2] + mylist[3]
    print("sum = ", sum )
    print("sub  = ", sub )
    print("mul  = ", mul )
    print("div = ", div)
    print("sum_of_list = ", sum_of_list)

calc (3,4)