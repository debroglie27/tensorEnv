
w = list(map(int, input("Enter the Weights: ").split()))
v = list(map(int, input("Enter the Values: ").split()))
max_w = int(input("Enter the Max Weight: "))

a = [[] for y in range(len(w))]

dict_list = {w[i]: v[i] for i in range(0, len(w))}

w.sort()
v = [dict_list[w[i]] for i in range(0, len(w))]

for i in range(0, len(w)):
    for j in range(0, max_w+1):
        if i == 0:
            if w[i] > j:
                a[i].append(0)
            else:
                a[i].append(v[i])
        else:
            if w[i] > j:
                a[i].append(a[i-1][j])
            else:
                a[i].append(max(v[i]+a[i-1][j-w[i]], a[i-1][j]))

print(a)
