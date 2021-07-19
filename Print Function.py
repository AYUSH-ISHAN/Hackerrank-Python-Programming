if __name__ == '__main__':
    n = int(input())
    # n digits in the number
    # n=5
    num = 0
    if n < 10:
        for i in range(1, n + 1, 1):
            num += i * (10 ** (n - i))
    if 10 <= n <= 99:

        for i in range(1, 10):
            num += i * (10 ** (10 - i - 1))
            # print(num, i)
            # print("+")

        for j in range(10, n + 1):
            num = num * 100 + j
            # print(num, j)
            # print("*")

    if 100 <= n <= 150:
        for i in range(1, 10):
            num += i * (10 ** (10 - i - 1))
            # print(num, i)

        for j in range(10, 100):
            num = num * 100 + j

        for k in range(100, n + 1):
            num = num * 1000 + k

    print(num)

