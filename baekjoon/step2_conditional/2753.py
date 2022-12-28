#2753
year = int(input())
if (year%4==0) & (year%100!=0):
    print('1')
elif (year%400==0):
    print('1')
else:
    print('0')

#모범답안
a = int(input())
if (a%4==0 and a%100!=0) or a%400==0: print(1)
else: print(0)    