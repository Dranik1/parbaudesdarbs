import json
import datetime

apmekletaji=[]
def load_data():
    file=open('apmekletaji.json', 'r')
    data=json.load(file)
    file.close()
    global apmekletaji
    apmekletaji=data['apmekletaji']
    print("DATA LOADED")

def save_data():
    data = {'apmekletaji': apmekletaji}
    print('SAGLĀBA DATUS.....')
    file = open('apmekletaji.json', 'w',encoding="utf-8")
    json.dump(data, file,ensure_ascii=False, indent=4)
    print("DATI SAGLĀBATI")

def water():
    global bottle_num, maksa
    bottle_num=float(input('Dzeramo udeni daudzums: '))
    price=float(0.45)
    maksa=bottle_num*price
    

def add_person():
    person_name=input("Ievadiet apmekletaju vardu: ")
    person_number=input("Ievadiet apmekletaju numuru: ")
    person_id=input("Ievadiet apmekletaju id: ")
    person_city=input("Ievadiet apmekletaju pilsetu: ")
    
    x=datetime.datetime.now()
    time=x.strftime("%x")

    person={
        'name':person_name,
        'number':person_number,
        'id':person_id,
        'city':person_city,
        'registration_date':time,
        'apmeklejums':[]
    }

    while True:
        response=input("Vai vēlies pievienot apmeklejumu? y/n")
        if response=='y':
            print("Apmeklejuma informācija:")
            apmeklejuma_laiks=input('Cik ilgs apmeklejums: ')
            bernu_sk = input('Bernu skaits: ')
            apmeklejuma_id=input('Apmeklejuma id:') 
            apmeklejuma_datums=datetime.datetime.now().strftime('%x')
            water()
            apmeklejums = {
                'time': apmeklejuma_laiks,
                'children': bernu_sk,
                'bottle_num': bottle_num,
                'price': maksa,
                'id': apmeklejuma_id,
                'date': apmeklejuma_datums
            } 
            person['apmeklejums'].append(apmeklejums)
        elif response=='n':
            break
        else:
            print('Ludzu izvelies y vai n')
    apmekletaji.append(person)

def print_person():
    for a in apmekletaji:
        print("APMEKLETAJS")
        print(f"{a['name']}(id:{int(a['id'])}, {a['number']}, {a['city']})")

def find_by_id():
    id=input("Ievadiet cilveka id: ")
    for i in apmekletaji:
        if i['id']==id:
            print(f"{i['name']}(id:{int(i['id'])}, {i['number']}, {i['city']})")
            while True:
                response=input("Vai velaties izdarit jauno apmeklejuu? y/n")
                if response=="y":
                    print("Apmeklejuma informācija:")
                    apmeklejuma_laiks=input('Cik ilgs apmeklejums: ')
                    bernu_sk = input('Bernu skaits: ')
                    apmeklejuma_id=input('Apmeklejuma id:') 
                    apmeklejuma_datums=datetime.datetime.now().strftime('%x')
                    water()
                    apmeklejums = {
                        'time': apmeklejuma_laiks,
                        'children': bernu_sk,
                        'bottle_num': bottle_num,
                        'price': maksa,
                        'id': apmeklejuma_id,
                        'date': apmeklejuma_datums
                        } 
                    i['apmeklejums'].append(apmeklejums)
                elif response=='n':
                    break
                else:
                    print('Ludzu izvelies y vai n')
        else:
            pass

def main():
    load_data()
    
    while True:
        uzdevums=int(input('(1)Pievienot apmekletaju, (2)Noprintet visus apmekletajus, (3)Exit, (4)Atrast ar id: '))
        if uzdevums==1:
            add_person()
        elif uzdevums==2:
            print_person()
        elif uzdevums==3:
            save_data()
            exit()
        elif uzdevums==4:
            find_by_id()
        else:
            print('Jums vajag izvelet 1, 2, 3 vai 4')
            
    

main()