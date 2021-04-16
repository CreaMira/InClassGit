import random, string

length = int(input("Length of password = "))

password_characters = string.ascii_letters + string.digits + string.punctuation

password = []

for x in range(length):
  password.append(random.choice(password_characters)),

print ("Your password:","".join(password))
  
