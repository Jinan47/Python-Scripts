import random

# characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!”$%&*-_+/~')
# pass_len = int(input('Enter the length of the password u want:'))
# random.shuffle(characters)
# print(characters[:pass_len])


characters = list('abcdefghijklmnopqrstuvwxyz.0123456789!”$%&@#*-_+/~')
pass_len = int(input('Enter the length of the password u want:'))
random.shuffle(characters)
password = "".join(characters[:pass_len])
print(password)
