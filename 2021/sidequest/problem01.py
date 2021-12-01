sum([x for x in range(1,1000) if not x % 3 or not x % 5])

# or
sum([x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0])
