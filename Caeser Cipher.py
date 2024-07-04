import string
line= list(input('enter your text: \n').lower())
alphabet= string.ascii_lowercase + string.ascii_lowercase
agenda = input(
    'enter e to ENCRYPT, d to DECRYPT, e to EXIT \n').lower()
end= False
number= int(input('enter your number from 1 to 25: \n'))
while not end:
    if agenda== 'e':
        for i in range (len(line)):
            if line[i]==' ':
                line[i]=' '
            else:
                new_letter= alphabet.index(line[i]) + number
                line[i]= alphabet[new_letter]
        print(''.join(map(str,line)))
        end= True
    elif agenda== 'd':
        for i in range (len(line)):
            if line [i]==' ':
                line[i]=' '
            else:
                new_letter= alphabet.index(line[i]) - number
                line[1]= alphabet[new_letter]
        print(''.join(map(str,line)))
        end= True
    else:
        determine= input(
            'invalid entry, try again Y for YES, N for NO: \n').lower()
        if determine== 'y':
            line= list(input('enter your text: \n').lower())
            agenda = input(
                'enter e to ENCRYPT, d to DECRYPT, e to EXIT \n').lower()
            number= int(input('enter your number from 1 to 25: \n'))
        else:
            End= True