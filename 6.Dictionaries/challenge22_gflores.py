import pprint
print("\t\t\t Welcome to the Database Admin Program")

user=input("Enter your username: ")
password=input("Enter your password: ")

if user=='admin00' and password=='admin1234':
    print(f"Hello {user}! You are logged in!")
print("Here is the current user database: ")

log_on_information=[
{'user':'admin00','password':'admin1234'},
{'user':'mooman74','password':'alskes145'},
{'user':'meramo1986','password':'kehns010101'},
{'user':'nickyD','password':'world1star'},
{'user':'george2','password':'booo3oha'}]

pprint.pprint(log_on_information)




