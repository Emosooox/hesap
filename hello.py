while True:
    while True:
        try:
            n1 = int(input("İlk sayıyı giriniz: "))
            break
        except:
            print("Lütfen geçerli bir sayı giriniz")
            continue
    while True:
        try:
            n2 = int(input("İkinci sayıyı giriniz: "))
            break
        except:
            print("Lütfen geçerli bir sayı giriniz")
            continue
    sonuc = 0
    while True:
        islem = input(print("Yapmak istediğiniz işlemi yazın\nToplama için [1]\nÇıkarma için [2]\nÇarpma için [3]\nBölme için [4]"))
        if islem == "1":
            sonuc = n1 + n2
            break
        elif islem == "2":
            sonuc = n1 - n2
            break
        elif islem == "3":
            sonuc = n1 * n2
            break
        elif islem == "4":
            sonuc = n1 / n2
            break
        else:
            print("Bu işlem mevcut değil 1-4 arasından seç")
            continue
    print("Sonuç:" + str(sonuc))
    c = input("Devam etmek istiyor musunuz? (y/n)")
    if c == "n":
        break