
# ejemplo almacenamiento de datos

libro = {
    'titulo': 'cien anos soledad',
    'autor': 'Gabo',
    'year': 1967
}

print('datos libro: ', libro)

print('\n----------------------------------------------\n')


# mostrar keys
book_keys = libro.keys()
print(book_keys)

print('\n----------------------------------------------\n')

# mostrar values
book_values = libro.values()
print(book_values)

print('\n----------------------------------------------\n')

# mostramos los pares clave : valor
pares_libro = libro.items()
print(pares_libro)

print('\n----------------------------------------------\n')

# agregar un clave y valor
libro['Nacionalidad'] = 'Colombiano'
print(libro)

print('\n----------------------------------------------\n')

# mostrar los pares de items
pares_libro = libro.items()
print(pares_libro)

print('\n----------------------------------------------')
print('----------------------------------------------\n')

# create a new dictionary of a person

person = {
    'personName': 'Orlando',
    'personAge': 48,
    'personProfession': 'Software Engineer',
    'personResidence': 'Medellin - Colombia'
}

print(person)

print('\n----------------------------------------------\n')

# acceder a valores por clave
print(person['personName'])
print(person['personProfession'])

print('\n----------------------------------------------\n')

# modificar un valor
person['personAge'] = 40

print('\n----------------------------------------------\n')

# agregar un nuevo par clave valor
person['personEmail'] = 'email@email.com'
print(person)

print('\n----------------------------------------------')
print('----------------------------------------------\n')

# encontrar datos del usuario

users = {
    'userA': {
        'Name': 'Juan',
        'Age': 39
    },
    'userB': {
        'Name': 'Sara',
        'Age': 35
    },
}

print(f'Data from de user userA: {users["userA"]}')

print('\n----------------------------------------------\n')

words = ['apple', 'banana', 'orange', 'apple', 'banana', 'pear', 'banana']
counter = {}

for fruit in words: 
    if fruit in counter:
        counter[fruit] += 1
    else:
        counter[fruit] = 1
print(f'Count:{counter}')

print('\n----------------------------------------------')
print('----------------------------------------------\n')

# Exercise

student = {
    'studentName': 'Carlos Alberto',
    'studentAge': 29,
    'studentCourses': ['Math', 'Physics', 'Chemistry'],
    'studentProm': 3
}
print(student)

# accedemos a clave y tomamos valores

studentName, studentAge, studentProm = student['studentName'], student['studentAge'], student['studentProm']
print(f'The student: {studentName} have {studentAge} years old and his prom is {studentProm}')

print('\n----------------------------------------------\n')

# mostramos claves

studentKeys = student.keys()
print(studentKeys)

print('\n----------------------------------------------\n')

# agregar una nueva clave valor

student['Graduado'] = False
print(student)

print('\n----------------------------------------------\n')
print('\n----------------------------------------------\n')

'''
Exercise
create an app that calculates the IMC

'''

patients = {}

# controlarlo con un ciclo
while True:
    patientName = input('Type the patient name: ')
    patientWeight = float(input('Type the weight of the patient (kg): '))
    patientHeight = float(input('Type the height of the patient (meters): '))

# procesar datos
    imc = patientWeight / (patientHeight ** 2)

    if imc < 18.5:
        category = 'Low weight'
    elif 18.5 <= imc < 25:
        category = 'Normal weight'
    elif 25 <= imc < 30:
        category = 'Overweight'
    else:
        category = 'Extremly Overweight'
    
    patients[patientName] = {
         'Weight': patientWeight,
         'Height': patientHeight,
         'IMC': imc,
         'Category': category
    }
       
    patientDataContinue = input('Do you want to add another patient? y/n: ')
    if patientDataContinue != 'y':
        break

print(f'Data created: {patients}')
print(f'\nPatient information:\n ')
    
for namePatient, dataPatient in patients.items():
    print(f'patientName: {namePatient}')
    print(f'patientWeight: {dataPatient['Weight']} kg')
    print(f'patientHeight: {dataPatient['Height']} m')
    print(f'IMC: {dataPatient['IMC']}')
    print(f'category: {dataPatient['Category']}')

    print('--' * 30)

print('\n----------------------------------------------\n')
print('\n----------------------------------------------\n')

# crear un conjunto de datos(data frame)
# libreria llamada Pandas

import pandas as pd

# (diccionario, modificacion)
# df = data frame
# 'index' va a ser indexado
df = pd.DataFrame.from_dict(patients,orient = 'index' )

# guardar el dataframe df en un archivo csv
df.to_csv('patients.csv', index_label= 'Name')

# guardar el df en formato excel
df.to_csv('patients.xlsx', index_label= 'Name')


'''
# creamos el data frame
datos = pd.read_csv('ruta del archivo')

'''


'''
# importar los archivos con comandos de terminal
# files = libreria
from google.colab import files
upload = files.upload()

'''

'''
# almacenamos el archivo guardado en colab
datos.to_csv('ruta donde quiero guardarlo')
'''

'''
# cargar el dataset desde colab
talento = pd.read_csv('ruta del archivo')
# visualizar el data set
talento.head()
'''




















