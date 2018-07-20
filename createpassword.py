import random

print("***Hello Friends***\nSupport : https://github.com/kamranabdullazade/createpassword\n")


a = list(range(10))


character = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]

k = ["!","@","#","$","%","/","^","&","*","(",")"]

e = ["*","j"]



b = k + a + character + a + character + k + e


while True:

  c = []
  random.shuffle(b)

  length = input("Number of symbols(exit=q) : ")
  if length.lower() == "q":
    break
  
  length2 = int(length)
  
  for i in range(0,length2):
      c.append(b[i])
        
  print(*c,sep="")
