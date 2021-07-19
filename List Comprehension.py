if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    final_list = []
    # inter = []
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             inter = []
    #             if i+j+k != n:
    #                 inter.append(i)
    #                 inter.append(j)
    #                 inter.append(k)
    #                 #print(inter)
    #                 final_list.append(inter)
    #                 #print(final_list)

    # i = [m for m in range(x+1)]
    # j = [n for n in range(y+1)]
    # k = [p for p in range(z+1)]

    final_list1 = [[r, t, u] for r in range(x + 1) for t in range(y + 1) for u in range(z + 1)]
    for i in final_list1:
        if sum(i) != n:
            final_list.append(i)
    print(final_list)


