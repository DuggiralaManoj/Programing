import random
Letters=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
Numbers=['1','2','3','4','5','6','7','8','9','0']
Symbols=['!','@','#','$','%','^','&','*','(',')','_','+']

print("Welcome to the password Genarator!")
n_Letters=int(input("How many letters you want in your password:"))
n_Numbers=int(input("How many numbers you want in your password:"))
n_Symbols=int(input("How many symbols you want in your password:"))
password_list=[]

for i in range(0,n_Letters+1):
    password_list+=random.choice(Letters)
for i in range(0,n_Numbers+1):
    password_list+=random.choice(Numbers)
for i in range(0,n_Symbols+1):
    password_list+=random.choice(Symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""

for i in password_list:
    password+=i
print("Your password is:",password)