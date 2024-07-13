import string
import random

attributes = string.ascii_uppercase +string. ascii_lowercase+ string.digits + string.punctuation

print("Enter the length of password as you need \n:")

LEN = int(input())

passW = ''.join(random.choices(attributes, k=LEN))

print("Your required password is : ", passW)
