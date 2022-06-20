def mukemmelsayi(x):

    toplam = 0

    for i in range(1, x):
        if (x % i == 0):
            toplam += i

    if (x == toplam):
        print(x,"Mükemmel Sayidir.")
z = int(input("1'den kaça kadar olsun ?"))
for x in range(1,z):
    mukemmelsayi(x)
    x = x + 1