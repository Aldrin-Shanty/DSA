def matrix_multiplication_chain(n, p):
    # Initialize matrices m and s
    m = [[float('inf') for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    # Cost of multiplying one matrix is zero
    for i in range(n):
        m[i][i] = 0

    # L is the chain length
    for L in range(2, n):  # Chain length ranges from 2 to n-1
        for i in range(1, n-L+1):
            j = i + L - 1
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    # Helper function to construct the parenthesization
    def print_optimal_parens(s, i, j):
        if i == j:
            return f"A{i+1}"
        else:
            k = s[i][j]
            left_part = print_optimal_parens(s, i, k)
            right_part = print_optimal_parens(s, k+1, j)
            return f"({left_part} x {right_part})"

    # Compute the result and parenthesization
    min_cost = m[1][n-1]
    parenthesization = print_optimal_parens(s, 1, n-1)
    return min_cost, parenthesization

# # Test Case
# n = 5
# p = [5, 4, 6, 2, 7]
# min_cost, parenthesization = matrix_multiplication_chain(n, p)
# print(f"Minimum cost: {min_cost}")
# print(f"Optimal parenthesization: {parenthesization}")
