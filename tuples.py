my_tuple = [10, 20, 30, 40]

print(my_tuple)

print(my_tuple[2])

print('----------------------------')

# Data sets
A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}
C = {8,6,16,8,9,11}

# union 
data_union = A.union(B)
new_data_union = data_union.union(C)
print(data_union)
print(new_data_union)

print('----------------------------')

# intersection
inter = A.intersection(B)
new_inter = inter.intersection(C)
print(inter)
print(new_inter)

print('----------------------------')

# Difference

diff = A.difference(B)
reverse_diff = B.difference(A)
new_diff = reverse_diff.difference(C)
print(diff)
print(reverse_diff)
print(new_diff)

print('----------------------------')

# len method
subject = ('bases', 'logic', 'aritmetica')
print(len(subject))

print('----------------------------')


# union entre dos listas
lista1 = [9,8,7,6,5,4]
lista2 = [3,2,1,5,6,4]

lista1.extend(lista2)

print(lista1)

print('----------------------------')
# method reverse

lista2.reverse()
print(lista2)

print('----------------------------')

# Dictionaries

dictionarie = {
    'name': 'Andres',
    'age': 30,
    'city': 'Medellin'
}   

print(dictionarie)

myName = dictionarie['name']
myAge = dictionarie['age']
myCity = dictionarie['city']

print(f'My name is {myName}, my age is: {myAge} and the citi where I live is: {myCity}')

print('----------------------------')

addEmail = dictionarie['email:'] = 'anfefu1@gmail.com'
addPhone = dictionarie['phone:'] = 345675857
print(dictionarie)


print('----------------------------')

#for with dictionaries

for dataDescription, valueData in dictionarie.items():
    print(f'clave: {dataDescription}, Value: {valueData}')

print('----------------------------')
# database example

patientHistory = {
    'Wilson':{
    'Name': 'Wilson',
    'age': 20,
    'height': 1.56,
    'weight': 60.5,
    'diabetes': True
    },
    'Ana':{
    'Name': 'Ana',
    'age': 40,
    'height': 1.70,
    'weight': 70.5,
    'diabetes': False
    }
}

print(patientHistory)
print(patientHistory['Ana'])
print(patientHistory['Wilson']['diabetes'])


print('----------------------------')

'''
agenda = {}

print(f'Holi I am your agenda')

while True:
    agendaName = input('Please type your name sweetheart: ')
    if agendaName == '0':
        break
    else:
        phoneNumber = int(input('Please type your cellnumber: '))
        yourEmail = input('Please type your email: ')
        agenda[agendaName] = phoneNumber, yourEmail
        

for agendaName, inputData in agenda.items():
    print(f'\n\nThis is your agenda:\n Name is: {agendaName}\n Email is: {yourEmail}\n Phone number is:{phoneNumber}\n')

'''

print('----------------------------')
'''
team = {}

while True:
    teamName = input('Type the group name: ')
    if teamName == 'exit':
        break
    else:
        name1 = input('type the first name: ')
        name2 = input('type the second name: ')
        team[teamName] = name1, name2

for name1, name2 in team.items():
    print(team)   
'''

equipo = {
    'grupo1': ['Pablo', 'Andres'],
    'grupo2': ['Carlos', 'Laura'],
    'grupo3': ['Marcela', 'Andrea']
}

#for
for nombres in equipo:
    print(nombres, equipo[nombres])

print(equipo['grupo2'])

equipo['grupo4'] = ['Luis', 'Pablo']
print(equipo['grupo4'])


print('----------------------------')

# exercise
'''

create a dictionary that represents the university info
Dictionary must contain:

University name

two dictionaries inside the main with:

faculty:
faculty name
students name
a list with acdemic programs

general services:
Library with hour of open, number of books to rent
Cafeteria with menu and people capacity

Contact Info:
phone
email
web page
'''

university = {
    'universityName': 'UCLA',
        'faculties': [
        {
            'facultyName': 'Engineering faculty',
            'facultyPeople': 2000,
            'academicPrograms':['environmental engineer', 'physics','math']
        
        },
        {
            'facultyName': 'Health faculty',
            'facultyPeople': 2000,
            'academicPrograms':['medicine', 'ondontology']
        
        }
    ],

    'general services':{

        'library':
            {
                'shedule': '8am to 8pm',
                'booksAvailabe': 3000
            },
        'cafeteria':
            {
                'menu': ['sandwich', 'salad', 'hot dog'],
                'cafeteriaCapacity': 200
            }
    },
    'contactInfo':{
        'phone': 34567866,
        'email': 'uclamail@ucla.com',
        'webPage': 'www.ucla.com'
    }

    

    
    
}









print('----------------------------')
























