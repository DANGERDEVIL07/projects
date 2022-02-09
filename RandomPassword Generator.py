import random
import string

print("Welcome to Password generator tool")

length = int (input('\n Enter the length of password: '))

lower = string.ascii_lowercase
uppper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

temp = lower+ uppper+ num+ symbols
password = random.sample(temp, length)

print("".join(password) )
