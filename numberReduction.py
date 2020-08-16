def reduce_number():
    number = int(input("Enter a number"))
    i = 0
    while number > 0:
        if number % 2 == 0:
            number = number / 2



        else :
            number = number - 1

        i+=1




    print(i)

reduce_number()


