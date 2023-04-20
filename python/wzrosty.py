def wzrost(tablica:list, liczbag:int):
    dl1 = len(tablica)//liczbag
    tablica.sort()
    lista = []
    dl = dl1
    zero = 0
    for a in range(liczbag):
        lista.append(tablica[zero:dl])
        zero +=dl1
        if a == liczbag-2:
            dl = len(tablica) - dl1
        dl +=dl1
    return lista
print(wzrost([2,4,7,8,1,2,4,3,4,5,6],3))