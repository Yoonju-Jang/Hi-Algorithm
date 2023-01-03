#3052
l = [int(input()) for _ in range(10)]
na = [i%42 for i in l]
print(len(set(na)))

# Best
s = set()
for _ in range(10):
    s.add(int(input())%42)
print(len(s))