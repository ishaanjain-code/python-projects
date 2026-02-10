import string 
import random 
def password_strength_checker(password):
    length=len(password)>=8
    digit=any(char.isdigit() for char in password)
    upper=any(char.isupper() for char in password)
    lower=any(char.islower() for char in password)
    special=any(not char.isalnum() for char in password)
    
    score= sum([length,digit,lower,upper,special])
    if score<=2:
        return "password strength is weak ❌"
    elif score<=4:
        return "password strength is medium ⚠"
    else:
        return "password strength is strong 👍"
    
password=input("enter password: ")
strength=password_strength_checker(password)
print(strength)
if strength=="password strength is weak ❌":
    suggested_password= random.choices(string.ascii_lowercase+ string.ascii_uppercase + string.digits + string.punctuation, k=8)
    print("Suggested strong password:", ''.join(suggested_password))
elif strength=="password strength is medium ⚠":
    suggestion=input("Do you want a suggested strong password? (yes/no): ")
    while suggestion.lower()=="yes":
    
        suggested_password= random.choices(string.ascii_lowercase+ string.ascii_uppercase + string.digits + string.punctuation, k=8)
        print("Suggested strong password:", ''.join(suggested_password))
        suggestion=input("Do you want another suggested strong password? (yes/no): ")
else :
    print("you are ready to go 👍")

