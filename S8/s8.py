"""Faylda bir nechta qatordan iborat IT kompaniya hodimlari to'g'risidagi ma'lumot yozilgan. Har bir qatorda
IT kompaniya hodimining ismi, lavozimi, oyligi, oyligiga bonus summa va qaysi bo'imda ishlashi. Ushbu
malumotlar ichidan bonuslari orasida musbat va manfiy qiymatlar mavjud. Kompaniyada yaxshi
uces ishlaganlar bonusi musbat, yomon ishlaganlar uchun manfiy qiymatlar bilan to'ldirilgan. Sizning vazifangiz
yaxshi ishlagan hodimlar ko'proq qaysi bo'limda ishlashini aniqlang. Agar shunday bo'limlar kop bolsa,
hammasini chiqaring."""
with open("S8/worker.txt") as f:
    lines = f.readlines()
    b1 = b2 = b3 = 0
    for line in lines:
        date = line[:-1].split(",")
        date[3] = int(date[3])
        if date[3] > 0 and date[4] == " 1-bo'lim":
            b1 += 1
        if date[3] > 0 and date[4] == " 2-bo'lim":
            b2 += 1
        if date[3] > 0 and date[4] == " 3-bo'lim":
            b3 += 1
    if b1 > b2 and b1 > b3:
        print("1-bo'lim")
    elif b1 < b2 and b2 > b3:
        print("2-bo'lim")
    elif b1 > b2 and b1 > b3:
        print("3-bo'lim")