factorial_memo = {}
zeros_memo = {}


def find_factorial(n):
    factorial = 1
    search_in_memo = factorial_memo.get(n, 0)
    if search_in_memo == 0:
        for i in range(1, n + 1):
            factorial *= i
        factorial_memo[n] = factorial
        return factorial
    return search_in_memo


def get_zeros(n):
    search_in_zeros = zeros_memo.get(n, 0)
    if search_in_zeros == 0:
        factorial = str(find_factorial(n))
        j = len(factorial) - 1
        count = 0
        while int(factorial[j]) == 0:
            count += 1
            j -= 1
        zeros_memo[n] = count
        return count
    return search_in_zeros


print(get_zeros(5))

print(get_zeros(12))
