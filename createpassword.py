import random

print("***Hello Friends***\nSupport : https://github.com/kamranabdullazade/createpassword\n")

length = int(input("Number of symbols : "))

a = list(range(10))

c = []

e = random.randint(1,9)
e = str(e)

character = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]

k = [*"!@#$%^&*()\/"]





b = k + a + character + a + character + k

random.shuffle(b)


for i in range(0,length):
    c.append(b[i])
        
print(*c,sep="")