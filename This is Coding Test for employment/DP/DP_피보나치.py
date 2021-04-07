def fibo(n):
    if n <= 2:
        return 1
    if data[n] != 0:
        return data[n]

    data[n] = fibo(n - 1) + fibo(n - 2)
    return data[n]
data = [0] * 20

print(fibo(10))
print(data)