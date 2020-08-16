def split():
    letters = ['a','b','c','d','e','f','g','h','i','j','k',
               'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    str = 'py1th0on'

    left = 0
    right = len(str)-1
    while left < right:
        if str[left] not in letters:
            str[left]++1
        elif str[right] not in letters:
            str[right]--1
        else :
            str[left],str[right] = str[right],str[left]

    print(str)

split()