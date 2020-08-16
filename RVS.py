def RVS():
    string = "hello"

    lst = list(string)

    vowels = ['a', 'e', 'i', 'o', 'u']

    left = 0

    right = len(string)-1

    while left < right :
        if lst[left] in vowels and lst[right] in vowels:
            lst[left],lst[right] = lst[right],lst[left]
            left += 1
            right -= 1
        elif lst[left] in vowels and lst[right] not in vowels:
            right -=1
        elif lst[left] not in vowels and lst[right] in vowels:
            left +=1
        else:
             if lst[left] not in vowels and lst[right] not in vowels:
                left +=1
                right -=1
    print("".join(lst))


RVS()
