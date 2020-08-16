def seperate():
    list = [1, 12, 10, 5, 11, 34, 100]
    kist  = []
    for i in list:
        if i % 2 == 0:
            kist.insert(0,i)
        else:
            kist.append(i)

    print(kist)


seperate()




