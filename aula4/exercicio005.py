for i in range(1, 100):
    if i %3 == 0 and i %5 == 0:
        print(f'{i} fuzzbuzz')
    elif i %3 == 0:
        print(f'{i} fuzz')
    elif i %5 == 0:
        print(f'{i} buzz')
    else:
        print(i)