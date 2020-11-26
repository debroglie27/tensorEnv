
s1 = input("Enter the first Sequence: ").split()
s2 = input("Enter the second Sequence: ").split()

a = [[0] for y in range(len(s2)+1)]
for i in range(len(s1)):
    a[0].append(0)

for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s2[i-1] == s1[j-1]:
            a[i].append(a[i-1][j-1]+1)
        else:
            a[i].append(max(a[i-1][j], a[i][j-1]))

print(a)
