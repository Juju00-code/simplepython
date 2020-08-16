def String_Compression():
    uncompressed  = ['a','a','b','b','c','c','c']

    tes = set(uncompressed)

    compressed = list(sorted(tes))

    length = len(compressed)

    x = [0]*length

    dex = 0
    for i in compressed:
        for j in uncompressed :
            if i==j:
                x[dex]+=1
        dex += 1

    print(compressed)
    print(x)

String_Compression()



