#Matthew Nguyen
#UFID: 29993997

def encode():
    password = int(input('Please enter your password to encode: '))
    newpass = password + int('3' * 8)
    print('Your password has been encoded and stored!\n')

    return password, newpass

if __name__ == '__main__':
    keepGoing = True

    while keepGoing:

        print('Menu'
              '\n-------------'
              '\n1. Encode'
              '\n2. Decode'
              '\n3. Quit')

        option = int(input('\nPlease enter an option: '))

        if option == 1:
            password, newpass = encode()

        elif option == 2:
            print(f'The encoded password is {newpass}, and the original password is {password}.\n')
        elif option == 3:
            keepGoing = False

        else:
            keepGoing = False
