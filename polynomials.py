# Generate a simple polynomial from inputs
# Input Name => x
# coefficients => a
# degree => n


def f(x, a, n):
    # a[0] + a[1]*x + a[2]*x^2 + ... + a[n]*x^n
    result = 0
    for index, coefficient in enumerate(a):
        if index <= n:
            result += coefficient * (x**index)

    return result


print(f(2, [2, 0, 4, -1], 3))
