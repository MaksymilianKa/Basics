def reminder_division(a,b):
    if b==0:
        raise Exception("Divisor cannot be 0")
    result = a//b
    remainder = a%b
    print(a, "/", b, "is", result, "remainder", remainder)

#main program
reminder_division(10,0)