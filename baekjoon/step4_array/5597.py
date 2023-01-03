#5597
student = list(range(1,31))
for _ in range(28):
    student.remove(int(input()))
print('%d\n%d' %(min(student),max(student)))