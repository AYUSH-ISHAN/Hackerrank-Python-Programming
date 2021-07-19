if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr = set(arr)
    arr = list(arr)

    great = max(arr)
    # print(arr)
    diff = []
    for i in arr:
        diff.append(great - i)

    diff = set(diff)
    diff = list(diff)

    for i in diff:
        if i == 0:
            diff.remove(i)
    great1 = min(diff)
    for m in arr:
        if great1 == (great - m):
            print(m)

