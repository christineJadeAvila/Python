# this was a c++ program and i want to make it a python program
# find the program in my CPE repo exam/Final-Plate

STUDENT_DATA = {
    'Abas' : [98, 98, 97, 89, 79, 78],
    'Erispe' : [98, 98, 99, 98, 99, 98],
}

STUDENT_ID = {
    '2133' : [98, 98, 97, 89, 79, 78],
    '1230' : [98, 98, 99, 98, 99, 98]
}

#OUTPUT
print('FIRST YEAR STUDENTS')
print("___________________________________________________")
NAME_ID =  {'Abas, Rene Rose': 2133,
           'Erispe, Erecka Lyn': 1230,}

#print the name and id for reference 
print('NAME\t', '\t\t\tSTUDENT ID')
for data in NAME_ID:
    print(data,"\t\t", NAME_ID[data])

#INPUT
print('')
print('Choose what surname or id:')
print("[1] Surname")
print('[2] Student ID')
print('Input your choice: ')
choice = input()
choose = int(choice) # convert string to int
print('')
 
if choose == 1:
    print('Enter Surname: ')
    sur = input()
    
    # condition
    if sur == 'Abas':
        print('Abas ' + str(STUDENT_DATA['Abas']))
    if sur == 'Erispe':
        print('Erispe ' + STUDENT_DATA['Erispe'])

elif choose == 2:
    print('Student ID:')
    id = str(input())

    if id == '2133':
        print('2133 ' + str(STUDENT_ID['2133']))
    if id == '1230':
        print('1230 ' + str(STUDENT_ID['1230']))

else:
    print('wrong input')

# I FIND C++ EASIER