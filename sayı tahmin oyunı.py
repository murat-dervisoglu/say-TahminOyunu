n=int(input("sayı tahmin oyunu için sayı gir "))
asd= input(f"1 ile {n} arasında bir sayı tut ve 'devam' yaz   ")

if asd =="devam":
    tablo_sayisi=0
    while True:
        if n>=pow(2,tablo_sayisi):
            tablo_sayisi +=1
        else:
            break
    print(f"karşına {tablo_sayisi} tablo çıkacak")
    toplam=0
    for i in range(0,tablo_sayisi):
        tablo = []
        for j in range(1,n+1):
            j = bin(j)[2:]
            j = int(j)
            if (j//10**i) %10==1:
                j= int(str(j),2)
                tablo.append(j)
        print(f"tablo {i+1}: {tablo}")
        s=int(input("tuttuğunuz sayı bu tabloda varsa 1'i, yoksa 2'yi tuşlayın: "))
        if s==1:

            toplam=toplam+tablo[0];
print(f"tuttuğun sayı: {toplam}")
