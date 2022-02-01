from module1 import *
rus_list=[]
ang_list=[]
rus_list=loe_failist("rus.txt",rus_list)
ang_list=loe_failist("ang.txt",ang_list)
try:
    a=int(input("Это словарик с русского на английский и с английского на русский, хочешь начать перевод?(1-ДА,2-нет) "))
    if a==1:
        while True:
            print("\nЧто ты хочешь сделать? \nУвидеть список всех слов - 1 \nПеревеcти - 2 \nДобавить слово в словарь - 3 \nКонтроль на знание слов - 4  \nИсправить ошибку - 5 \nХочу закончить - 6")
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
                    kontrol(ang_list,rus_list)
                elif b==5:
                    jazik=int(input("В каком языке ошибка? (1-русский, 2-английский) "))
                    if jazik==1:
                        rus_list=ispravlenie(input("Слово: "),rus_list)
                        failisse(rus_list,"rus.txt")
                    elif jazik==2:
                        ang_list=ispravlenie(input("Word: "),ang_list)
                        failisse(ang_list,"ang.txt")
                    else:
                        print("Такого варианта нету!")
                elif b==6:
                    print("Хорошо, до свидания!")
                    break
                else:
                    print("Такого варианта нету!")
            except:
                ValueError
    elif a==2:
        print("Хорошо, до свидания!")
except:
    ValueError

