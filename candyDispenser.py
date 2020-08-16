def candies():
    candy = [2, 3, 1, 5, 4]
    maxFigure  = max(candy)
    extraCandy = 3
    for i in candy:
         addele = i + extraCandy
         if addele > maxFigure:
             print("True")

         else :
             print("false")



print(candies())