def mukemmelsayi(x):

    toplam = 0

    for i in range(1, x):
        if (x % i == 0):
            toplam += i

    if (x == toplam):
        print(x,"Mükemmel Sayidir.")
for x in range(1,1000):
    mukemmelsayi(x)
    x = x + 1