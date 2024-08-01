def knapsack01(p, wt, m, n):
    k = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, m+1):
            if wt[i] <= w:
                k[i][w] = max(p[i] + k[i-1][w-wt[i]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]

    result = [0 for _ in range(n+1)]

    i, j = n, m
    while i > 0 and j > 0:
        if k[i][j] != k[i-1][j]:
            result[i] = 1
            j -= wt[i]
        i -= 1

    return result[1:]

    # # Test Case
    # p = [0, 1, 2, 5, 6]
    # wt = [0, 2, 3, 4, 5]
    # m = 8
    # n = 4
    # print(knapsack01(p, wt, m, n))
