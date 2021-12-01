def Fibonacci():
    f0, f1 = 1, 1
    while True:
        yield f0
        f0, f1 = f1, f0+f1

mmax = 4*10**6
fibs = []
for f in Fibonacci():
    if f >= mmax:
        break
    fibs.append(f)

print(sum([x for x in fibs if not x % 2]))

# A kcon optimization
# print(sum(fibs[2::3]))
