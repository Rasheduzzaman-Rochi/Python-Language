b = [1, 2, 3, 4, 5]

# for i in b:
#     if i % 2 == 0:
#         i**2
#     else:
#         i

b_new = [i**2 if i%2 == 0 else i for i in b]
print(b_new)