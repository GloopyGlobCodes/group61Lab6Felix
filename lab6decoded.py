#Felix Lee, Group 61 Lab 6

def main():
    while True:
        choice = menu()
        if choice == 1:
           encoded = encode() 
        elif choice == 2:
            decoded = decode() 
        elif choice == 3:
            break

def menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode\n2. Decode\n3. Quit')
    print('')
    choice = int(input('Please enter an option: '))
    while True:
        if choice in (1, 2, 3):
            break
        else:
            choice = int(input('Invalid! Please enter an option: '))
    return choice


def encode():
    input = input('Please enter your password to encode: ')
    ans = '' 
    for i in input:  
        newDig = (int(i) + 3) % 10
        ans += str(newDig) 
    print('Your password has been encoded and stored!')
    print('') 
    return ans


if __name__ == '__main__':
    main()
