# import collections
# читерсий способ без списка

a = 'A2'
b = 'C4F'

sum = hex(int(a, 16) + int(b, 16))
mult = hex(int(a, 16) * int(b, 16))

print(sum[2:].upper().split())
print(mult[2:].upper().split())
