from random import shuffle
import random

def loe_failist(f:str,s:list):
    """Info failist f listisse l
    """
    fail=open(f,'r',encoding="utf-8-sig")
    for rida in fail:
        s.append(rida.strip())
    fail.close()
    return s

def perevod(rus:list,ang:list):
    slovo=input("Какое слово перевести? ")
    if slovo in rus:
        perevod=ang[rus.index(slovo)]
        print(slovo+"-"+perevod)
    elif slovo in ang:
        perevod=rus[ang.index(slovo)]
        print(slovo+"-"+perevod)
    else:
        print("Такого слова в словаре нету")

def add_slovo(f:str, v:str):
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(v+"\n")

def ispravlenie(slovo:str,l:list):
    for i in range(len(l)):
        if l[i]==slovo:
            new_slovo=slovo.replace(slovo,input("Новое слово: "))
            l.insert(i,new_slovo)
            l.remove(slovo)
    return l

def kontrol(l1:list,l2:list):
    vsego_ballov=0
    lists=[]
    lists.extend(l1)
    lists.extend(l2)
    random.shuffle(lists)
    print('random list ',lists)
    for i in range(len(l1)):
        otvet=input(f"Переведи данное слово - '{lists[i]}': ")
        if otvet in l1 or otvet in l2:
            if lists[i] in l1:
               if l1.index(lists[i])==l2.index(otvet):
                    vsego_ballov+=1
                    print("Правильно!")
                    print()
            elif lists[i] in l2:
                if l2.index(lists[i])==l1.index(otvet):
                    vsego_ballov+=1
                    print("Правильно!")
                    print()
        else:
            print("Неправильно!")
            print()
    resultat=(vsego_ballov/len(l1))*100
    print(f"Ваш результат: {resultat}%")



