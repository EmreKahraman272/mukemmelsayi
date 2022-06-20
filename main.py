def mukemmelsayi(x):

    toplam = 0

    for i in range(1, x):
        if (x % i == 0):
            toplam += i

    if (x == toplam):
        print(x,"Mükemmel Sayidir.")
z = int(input("kaçtan başlasın?"))
j = int(input("kaçta bitsin?"))
for x in range(z , j):
    mukemmelsayi(x)
    x = x + 1