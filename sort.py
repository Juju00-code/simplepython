def height_checker():
    height = [1,1,4,2,1,3]
    n = len(height)
    lis = sorted(height)

    x = 0
    for i in range(n):
        if height[i]!= lis[i]:
            x += 1
    print(lis)
    print(x)

height_checker()


























