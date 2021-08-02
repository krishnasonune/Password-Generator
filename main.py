import random


a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
c = '1234567890'
d = '!@#$%^&*()_-/*<>,.:;[]{}+'

z = a + b + c + d
length = 8
password = "".join(random.sample(z, length))
print(password)