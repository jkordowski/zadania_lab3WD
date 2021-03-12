A = [1-x for x in range(1, 11)]
B = [4**y for y in range(8)]
C = [z for z in B if z%2 == 0]

print(A)
print(B)
print(C)