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
    water()
    x=datetime.datetime.now()
    time=x.strftime("%x")
    person={
        'name':person_name,
        'number':person_number,
        'id':person_id,
        'city':person_city,
        'water_num': bottle_num,
        'nomaksaja': maksa,
        'registration_date':time
    }

    apmekletaji.append(person)

def print_person():
    for a in apmekletaji:
        print("APMEKLETAJS")
        print(f"{a['name']}(id:{int(a['id'])}, {a['number']}, {a['city']})")

def find_by_id():
    id=input("Ievadiet cilveka id: ")
    for i in apmekletaji:
        if i['id']==id:
            print(i)
            return

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