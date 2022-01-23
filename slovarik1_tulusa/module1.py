def loe_failist(f:str,s:list):
    """Info failist f listisse l
    """
    fail=open(f,'r',encoding="utf-8-sig")
    for rida in fail:
        s.append(rida.strip())
    fail.close()
    return s
def perevod(rus:list,ang:list):
    s=input("Какое слово перевести? ")
    if s in rus:
        p=ang[rus.index(s)]
        print(s+"-"+p)
    elif s in ang:
        p=rus[ang.index(s)]
        print(s+"-"+p)
    else:
        print("Такого слова в словаре нету")
def add_slovo(f:str, v:str):
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(v+"\n")



