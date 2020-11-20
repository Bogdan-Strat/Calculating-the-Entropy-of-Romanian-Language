import math
s=input()
d={}
s = s.replace(",", "").replace("!", "").replace("?", "").replace(".", "").replace(":", "").replace(";", "").replace("(","").replace(")","")
s = s.replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6","").replace("7", "").replace("8", "").replace("9", "")
s = s.replace("-", " ")
for i in s:
    a=i.lower()
    #print(a)
    for y in range(len(a)):
            d[a[y:y + 1]] = d.get(a[y:y + 1], 0) + 1
H=0
nr=0
for (k,v) in d.items():
    print(k,v)
for v in d.values():
    nr=nr+v
print(nr)
for v in d.values():
    H=H+  (v/nr)*math.log((1/(v/nr)),2)
print(H)
