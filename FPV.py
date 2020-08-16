def pivot_value():
    nums  = [1, 7, 3, 6, 5, 6,]

    midpoint = len(nums)/2

    con = int(midpoint)

    pointer = con + 1

    left = sum(nums[0:con])

    right = sum(nums[pointer:])

    if left == right:
        print(con)
    else:
        print(-1)

pivot_value()