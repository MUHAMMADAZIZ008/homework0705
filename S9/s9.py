"""My_sort nomli funksiya yarating va ushbu funksiya parameter sifatida faqat butun sonardan iborat List malumotlari 
beriladi. Sizing vazifangiz bu funksiyaga qiymat qaytarish sifatida Listning har bir elementarining raqamlar yig'indisi 
bo'yicha o'sish tartibida saralash kerak. Foydalanuvchi List elementlariga faqat musbat sonlar kirita oladi va shuni 
shartini ham exception orgali tekshirib oling."""
def my_sort(lst):
    lst1 = []
    for i, v in enumerate(lst):
        total = 0
        while lst[i] > 0:
            total += lst[i] % 10
            lst[i] //= 10
        lst1.append(total)
    lst1.sort()
    return lst1
n = int(input("Listga nechta son kiritmoqchisiz: "))
lst = []
try:
    for i in range(n):
        numLst = int(input(f"{i+1}: "))
        lst.append(numLst)
        if numLst == 0:
            raise ZeroDivisionError("Nol kiritib bo'lmaydi")
        elif numLst < 0:
            raise ValueError("Manfiy son kiritib bo'lmaydi")
except ZeroDivisionError:
    print("Xatolik yuzaga keldi")
except ValueError:
    print("Manfiy son kiritib bo'lmaydi")

print(my_sort(lst))