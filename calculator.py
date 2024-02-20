while True:
    
    print("Do more equations!\n")


    number = int(input("The first number: "))
    number2 = int(input("The second: "))
    calculation = int(input("What do you want to do with these numbers? Choose: addition(1), subtraction(2), multiplication(3), division(4)\n")) 

    if calculation == 0:
        break
  
    if calculation == 1:
        print(number + number2)
    elif calculation == 2:
        print(number - number2)
    elif calculation == 3:
        print(number * number2)
    elif calculation == 4:
        if number2 != 0:
            print(number / number2)
        else:
            print("You cannot divide by zero!\n")


