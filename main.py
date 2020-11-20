import math
def entropief(s,gr):
    for i in s:
        a=i.lower()
        for y in range(len(a)):
            if y != (len(a) - 1):
                d[a[y:y + gr]] = d.get(a[y:y + gr], 0) + 1 #creez primul dictionar si aflam frecventele grupurilor de cate 2 litere
                d2[a[y:y + gr+1]] = d2.get(a[y:y + gr+1], 0) + 1 #creez al doilea dictionar cu grupurile de 3 litere si frecventele grupurilor
    lista=[]
    for (k, v) in d2.items(): #mergem in al doilea dictionar
        if len(k)==(gr+1):
            lista.append([k[:gr],k[len(k)-1],v/d[k[:gr]]]) #adaugam intr-o lista: (primele 2 caractere din grupul de 3, ulitmul caracter din grupul de 3, frecventa grupului de 3/frecventa grupului de 2)
    print(lista)
    H=0
    nr=0
    for v in d.values():
        nr=nr+v
    for j in range(len(lista)):
        H=H+ (d[lista[j][0]]/nr)*(lista[j][2]*math.log((1/lista[j][2]),2))
    return H
f=open("entropie.txt","r")
s=f.read()
gr=int(input()) #gr este numarul de litere stiute, iar noi trebuie sa calculam probabilitatea de aparitie a literei urmatoare
d = {}
d2={}
s = s.replace(",", "").replace("!", "").replace("?", "").replace(".", "").replace(":", "").replace(";", "").replace("(","").replace(")","").replace("'","").replace("\n"," ")
s = s.replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6","").replace("7", "").replace("8", "").replace("9", "")
s = s.replace("-", "*")
s = s.replace(" ", "*")#codez tot ceea ce tine de spatii intre cuvinte cu *
s = s.split(" ")
print(entropief(s,gr))
f.close()



