N = int(input())
f = 1
for i in range(1, N+1):
   f *= i
   f %= 1000000000000
   while f % 10 == 0:
        f /= 10
print(int(f % 10))