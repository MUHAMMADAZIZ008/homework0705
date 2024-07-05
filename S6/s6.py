"""Foydalanuvchi tomonidan Listda faqat butun sonlardan iborat List kiritilgan. Sizning vazifangiz ushbu
Listda qo'shni bir xil ishorali elementlarni chigaring. Agar qo'shni elementlarning ishoralari bir biridan farqli
bolsa, sonlar chiqarilmasin. Har bir masala shartiga mos qo'shni elementlarni alohida gatorda chiqarilsin."""

def result_lst(lst):
    len_lst = len(lst)
    addition = 1
    for i in range(len_lst):
        if i != len_lst-1:
            if lst[i] > 0 and lst[addition] > 0 or lst[i] < 0 and lst[addition] < 0:
                if lst[i] > 0 and lst[addition+1] > 0 or lst[i] < 0 and lst[addition+1] < 0:
                    print(lst[i], lst[addition+1])
                addition += 1

n = int(input("Nechta son kiritmoqchisiz: "))
lst = []
for i in range(n):
    creatLst = int(input(f"{i+1}: ")) 
    lst.append(creatLst)
result_lst(lst)