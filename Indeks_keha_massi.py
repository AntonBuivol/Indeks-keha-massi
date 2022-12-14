print("Tere! Olen sinu uus sõber - Python")
nimi=input("Sinu nimi on ")
if nimi.isalpha():
    print(f"{nimi} , oi kui ilus nimi")
    try:
        vastus=int(input(f"{nimi} ! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))

        if vastus == 1:
                pikkus = float(input("Kirjuta sinu pikkus "))
                mass = float(input("Kirjuta sinu mass "))
                if pikkus>0 and mass>0:
                    indeks = round(mass /(0.01*pikkus)**2,1)
                    print(nimi, "! Sinu keha indeks on: ", indeks)
                    if indeks<=16:
                        print("Tervisele ohtlik alakaal")
                    if indeks > 16 and indeks<=19:
                        print ("Alakaal")
                    if indeks > 19 and indeks <= 25:
                        print ("Normaalkaal")
                    if indeks > 25 and indeks <= 30:
                        print("Ülekaal")
                    if indeks > 30 and indeks <= 35:
                        print("Rasvumine")
                    if indeks > 35 and indeks <= 40:
                        print("Tugev rasvumine")
                    if indeks>40:
                        print("Tervisele ohtlik rasvumine")
        else:
            print("Kahju! See on väga kasulik info!")
            exit
    except:
        print("ValueError")