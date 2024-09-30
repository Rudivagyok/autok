#forras=open('autok.txt','rt', encoding='utf-8')
#print(forras.readline().strip())
#print(forras.readline().strip())
#forras.close()
autok=[]
with open('autok.txt', 'r' , encoding='utf-8') as forras, \
    open('autok_api.txt','w',encoding='utf-8') as cel:
    db=forras.readline()
    fejlec=forras.readline()
    for sor in forras:
        adat=sor.strip().split(',')
        auto={'rendszam':adat[0],'tipus':adat[1],'kor':int(adat[2])}
        autok.append(auto)
        print(auto,file=cel)
print(f'{autok}')