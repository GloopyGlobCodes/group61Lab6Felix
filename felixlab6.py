
#Felix Lee, Group 61 Lab 6

# Gunnar Dougherty's Felix Lee Lab 6 contribution

def main():
    while True:
        value = menu()
        if value == 1:
           encoded = encode() 
        elif value == 2:
            decoded = decode(encoded) 
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
    return pick

def encode():
    password = input('Please enter your password to encode: ')
    ans = '' 
    for i in password:  
        newDig = (int(i) + 3) % 10 
        ans += str(newDig) 
    print('Your password has been encoded and stored!')
    print('') 
    return ans # this is what's stored into encoded in main.

def decode(encoded):
    decoded_password = '' # initialize empty new string
    for i in encoded: # iterate over every digit in str
        encoded_digit = (int(i)-3) % 10
        decoded_password += str(encoded_digit) # add decoded digit to new str
    print(f'The encoded password is {encoded} and the original password is {decoded_password}.', end = '\n')
    return decoded_password # new str


if __name__ == '__main__':
    main()
