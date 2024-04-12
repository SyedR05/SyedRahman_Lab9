
def encode(password):
    temp_pass_list = [int(num) for num in str(password)]
    temp_pass_list = [(num+3) for num in temp_pass_list]
    for i in range(len(temp_pass_list)):
        if temp_pass_list[i] >= 10:
            temp_pass_list[i] -= 10
    temp_pass_list = [str(num) for num in temp_pass_list]
    encodedpass = ''.join(temp_pass_list)
    encodedpass = int(encodedpass)
    return encodedpass

def decode(password):
    code = str(password)
    decoded_password = ""
    for item in range(len(code)):
        if code[item] == str(2):
            decoded_password += str(9)
        elif code[item] == str(1):
            decoded_password += str(8)
        elif code[item] == str(0):
            decoded_password += str(7)
        else:
            decoded_password += str(int(code[item]) - 3)
    return decoded_password

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def main():
    encoded_password = 0
    while True:
        menu()
        option = int(input('Please enter an option: '))

        match option:
            case 1:
                password = int(input('Please enter your password to encode: '))
                encoded_password = encode(password)
                print('Your password has been encoded and stored!')
                print()
            case 2:
                decoded_password = decode(encode(password))
                print("The encoded password is ", encoded_password, ", and the original password is ", decoded_password, ".", sep="")
                print()
            case 3:
                exit()


if __name__ == '__main__':
    main()
