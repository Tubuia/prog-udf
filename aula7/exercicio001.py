def funcao(a, b, c, d):
    count = 0
    for i in range(a, b):
        if count == c:
            print(d)
            count = 0
        else:
            print(i)
            count += 1

funcao(1, 11, 2, 'DOIS')
