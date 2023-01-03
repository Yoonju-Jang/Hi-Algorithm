#10807
N = int(input())
sec = list(map(int,input().split()))
if len(sec)==N:
    print(sec.count(int(input())))