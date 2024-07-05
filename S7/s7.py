"""Foydalanuvchi tomonidan Dictionaryga keyga ismlar va valuega esa Boolean type(1 yoki 0) kiritadi.
Sizning vazifangiz eng kop ovoz berganlarning ismlarini chigarish. Agar durrang bolsa, ikkalsini ham
chiqarish kerak. Chigarishda birinchi gatorda qaysi qiymat kop ovoz berilganini va keying qatorda esa
Ismlarni chigarish kerak. Ma'lumotlarni chiqarish na'munada keltirilgandek bolishi kerak."""
dic = {}
inInfo = int(input("Nechta odamning ma'lumotini kiritmoqchisiz: "))

for i in range(inInfo):
    nameP = input("Isim kiriting: ")
    nameO = int(input("(Ha: 1 yoki Yo'q: 0) kiriting: "))
    dic[nameP] = nameO
# print(dic)
oneLst = []
zeroLst = []
count = 0
count2 = 0
for j in dic:
    if dic[j] == 1:
        oneLst.append(j)
        count += 1
    else:
        zeroLst.append(j)
        count2 += 1
if count > count2:
    print(f"{1}: ")
    for ix in oneLst:
        print(ix)
elif count == count2:
    print(f"{1}: ")
    for ix in oneLst:
        print(ix)
    print(f"{0}: ")
    for ix in zeroLst:
        print(ix)
else:
    print(f"{0}: ")
    for ix in zeroLst:
        print(ix)