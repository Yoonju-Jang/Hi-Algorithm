#1157
s = input().upper()
ss = ''.join(sorted(s))
sss = sorted(set(s))
cnt = []
for i in sss:
    cnt.append(ss.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(sss[cnt.index(max(cnt))])