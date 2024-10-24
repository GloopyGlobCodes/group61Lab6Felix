#Felix Lee, Group 61 Lab 6, contribution to Gunnar Dougherty's Code with decode function implemented

def menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode\n2. Decode\n3. Quit')
    print('')  # instructions pdf shows double space between menu and input
    choice = int(input('Please enter an option: '))
    while True:
        if choice in (1, 2, 3):
            break
        else:
            choice = int(input('Invalid! Please enter an option: '))
    return choice  # menu option choice


def encode():
    password = input('Please enter your password to encode: ')
    encoded_password = '' # initialize new string
    for digit in password:  # iterate through each digit in string
        encoded_digit = (int(digit) + 3) % 10  # encoding is add 3, keep one digit, hence modulus 
        encoded_password += str(encoded_digit)  # add incoded digit to new string
    print('Your password has been encoded and stored!')
    print('')  # instructions pdf shows double space between confirmation output and menu
    return encoded_password

def decode():
  password = encoded_password
  decodedPass = '' # initialized string answer
  for i in password: # indexing through string
    oldDigit = (int(i)-3) % 10 #reverting encoding process
    decodedPass += str(oldDigit) # adding decoded digit to the string answer
  print("The encoded password is", password, "and the original password is", decodedPass)
  print('')
  return decoded_password

def main():
    while True:
        choice = menu()
        if choice == 1:
            encoded_password = encode() # stores encoded password as variable
        elif choice == 2:
            decoded_password = decode() # storing decoded password as variable
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
