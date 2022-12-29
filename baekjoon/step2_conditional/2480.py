# #2480 (내 풀이 - 너무 어렵게 생각함)
# dice = list(map(int,input().split()))
# rep = set(dice)

# if rep = 1:
#     print()
# elif rep = 2:
# elif rep =3:

# #도움(직관+간단)
# a, b, c = map(int,input().split())

# if a == b == c:
#     print(10000 + a*1000)
# elif a == b:
#     print(1000 + a*100)
# elif a == c:
#     print(1000 + a*100)
# elif b == c:
#     print(1000 + b*100)
# else:
#     print(100 * max(a,b,c))

#모범답안(더 축약)
a, b, c = map(int,input().split())
print(10000 + a*1000 if a==b==c else 1000+100*b 
if a==b or b==c else 1000+100*a if c==a else 100*max(a,b,c))