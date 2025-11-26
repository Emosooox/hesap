while True:
    n1 = int(input("İlk sayıyı giriniz: "))
    n2 = int(input("İkinci sayıyı giriniz: "))
    sonuc = 0
    islem = input(print("Yapmak istediğiniz işlemi yazın\nToplama için [1]\nÇıkarma için [2]\nÇarpma için [3]\nBölme için [4]"))
    if islem == "1":
        sonuc = n1 + n2
    elif islem == "2":
        sonuc = n1 - n2
    elif islem == "3":
        sonuc = n1 * n2
    elif islem == "4":
        sonuc = n1 / n2
    print("Sonuç:" + str(sonuc))
    c = input("Devam etmek istiyor musunuz? (y/n)")
    if c == "n":
        break