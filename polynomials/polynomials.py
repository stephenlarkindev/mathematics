from functools import reduce
# Generate a simple polynomial from inputs
# Input Name => x
# coefficients => a
# degree => n


def f(x, a):
    # a[0] + a[1]*x + a[2]*x^2 + ... + a[n]*x^n   where n is the length of a - 1

    return reduce(
        (lambda a, b: a + b),
        list(map((lambda c: c[1] * (x**c[0])), enumerate(a)))
    )


print(f(2, [2, 0, 4, -1]))
