import math

l = list(map(int, input().split()))

if len(l) <= 3:
    print(l)
    
else:
    if l[0] > l[1]:
        if l[1] > l[2]:
            a = l[0]
            b = l[1]
            c = l[2]
        else:
            a = l[0]
            b = l[2]
            c = l[1]
    else:
        if l[0] > l[2]:
            a = l[1]
            b = l[0]
            c = l[2]
        else:
            a = l[1]
            b = l[2]
            c = l[0]
            

d = c #maximalnoe po modulu otricatelnoe
e = b
f = a
for i in range(3, len(l)):
    if l[i] >= 0:
        if l[i] > a:
            c = b
            b = a
            a = l[i]
        elif l[i] > b:
            c = b
            b = l[i]
        elif l[i] > c:
            c = l[i]
    else:
        if l[i] < d:
            f = e
            e = d
            d = l[i]
        elif l[i] < e:
            f = e
            e = l[i]
        elif l[i] < f:
            f = l[i]
            
        

print(a, b, c)
print(d, e)
        
if (math.fabs(d) + math.fabs(e)) > b + c:
    print('res', a , d ,e)
else:
    print('res', a, b, c)


