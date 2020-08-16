def ci():
    hers = ["IN-N-OUT", "88 SPORTS BAR", "TREE AND GRILL","POLO CLUB", "BLUEFROG"]
    his = ["ADAM CHICKEN", "PORTIONS BAR", "IN-N-OUT", "POLO CLUB", "BLUEFROG"]
    fav = []

    for i in hers:
        for j in his:
            if i == j :
                fav.append(i)

    print(fav)

ci()
