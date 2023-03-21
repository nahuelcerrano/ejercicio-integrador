def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a%b)

print(f'El MCD es: {mcd(16, 20)}')
