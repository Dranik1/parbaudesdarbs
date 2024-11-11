import json

'''apmekletaji=[]
def load_data():
    file=open('apmekletaji.json', 'r')
    data=json.load(file)
    file.close()
    global apmekletaji
    apmekletaji=data['apmekletaji']'''

def add_person():
    person_name=input("Ievadiet apmekletaju vardu: ")
    person_number=input("Ievadiet apmekletaju numuru: ")
    person_id=input("Ievadiet apmekletaju id: ")

    person={
        'name':person_name,
        'number':person_number,
        'id':person_id
    }

    personJson=json.dumps(person, indent=4)

    with open('apmekletaji.json', 'w') as f:
        f.write(personJson)

    #apmekletaji.append(person)

def main():
    #load_data()
    add_person()

main()