print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis on sinu nimi: ")
print(nimi+", oi kui ilus nimi!")
leian=input(nimi+"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if leian=="1":
     pikkus=float(input("Sinu pikkus (cm): "))
     mass=float(input("Sinu mass (kg): "))
     indeks=mass/((0.01*pikkus)*2)
     x=round(indeks,1)
     print(nimi+"! Sinu keha indeks on: ")
     print(x)
     if x > 40:
        print("Tervisele ohtlik rasvumine")
     elif x > 34.9:
        print("Tugev rasvumine")
     elif x > 29.9:
        print("Rasvumine")
     elif x > 24.9:
        print("Ülekaal")
     elif x > 18.9:
        print("Normaalkaal")
     elif x > 15.9:
        print("Alakaal")
     else:
         print("Tervisele ohtlik alakaal")
else:
        print("Kahju! See on väga kasulik info!")
        print(" ")
        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
