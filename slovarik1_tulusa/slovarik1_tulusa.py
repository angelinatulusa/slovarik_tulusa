from module1 import *
rus_list=[]
ang_list=[]
rus_list=loe_failist("rus.txt",rus_list)
ang_list=loe_failist("ang.txt",ang_list)
try:
    a=int(input("Это словарик с русского на английский и с английского на русский, хочешь начать перевод?(1-ДА,2-нет) "))
    if a==1:
        while True:
            print("\nЧто ты хочешь сделать? \nУвидеть список всех слов - 1 \nПеревеcти - 2 \nДобавить слово в словарь - 3 \nИсправить ошибку - 4")
            try:
                b=int(input("Выбери чифру "))
                if b==1:
                    print(rus_list)
                    print(ang_list)
                elif b==2:
                    perevod(rus_list,ang_list)
                elif b==3:
                    add_slovo("rus.txt",input("Введите новое слово на русском "))
                    add_slovo("ang.txt",input("Введите новое слово на английском "))
                elif b==4:
                    print("К сожалению данная функция недоступна")#ne pridumala kak eto sdelat
                else:
                    print("Такого варианта нету!")
            except:
                ValueError


    elif a==2:
        print("Хорошо, до свидания!")
except:
    ValueError

