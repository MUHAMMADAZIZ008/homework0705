"""Tasavvur qiling-a, sizda berilgan naqshga muvofiq turli xil ranglar bilan
to ldirishingiz kerak bolgan kvadratchalar qatori bor. Kvadratchalarni ketma-ket
bo yash kerak, ya'ni keyingi kvadrat boshqa rangda bo'lsa, qalamni o zgartirishingiz kerak bo ladi.
Eslatma: Barcha ma'lumotlarni foydalanuchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo yiladi.
Ranglar ro'yxatini oladigan va butun naqshni to'ldirish uchun zarur bo'lgan
vagning qymatini (soniyalarda) qaytaradigan funksiyani yozing."""

def find_color(colors):
    time = 0
    color_current = ""
    for color in colors:
        if color != color_current:
            time += 1
            color_current = color
        time += 2
    return time-1


n = int(input("Nechta rang kiritasiz: "))
colors = []
for i in range(n):
    colorLst = input("Rang kiting: ")
    colors.append(colorLst)
print(find_color(colors))