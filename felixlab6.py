
#Felix Lee, Group 61 Lab 6

def main():
    while True:
        value = menu()
        if value == 1:
           encoded = encode() 
        elif value == 2:
            decoded = decode() 
        elif value == 3:
            break

def menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')
    pick = int(input('Please enter an option: '))
    while True:
        if pick in (1, 2, 3):
            break

def encode():
    input = input('Please enter your password to encode: ')
    ans = '' 
    for i in input:  
        newDig = (int(i) + 3) % 10 
        ans += str(newDig) 
    print('Your password has been encoded and stored!')
    print('') 
    return ans # this is what's stored into encoded in main.


if __name__ == '__main__':
    main()
