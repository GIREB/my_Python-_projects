from userlogin import sys_user_name, password

print("""
****************************
WELCOME TO THE USER LOG IN PROGRAM
""")
sys_user_Name="can"
sys_Password="12345"
entree=3

while True:
    user_name=input("please,enter the name:")
    your_password=input("please,enter your password:")
    if(user_name!=sys_user_Name and your_password==sys_Password):
        print("your user name is wrong.")
        entree-=1
    elif(user_name==sys_user_Name and your_password!=sys_Password):
        print("your password is wrong")
        entree-=1
    elif (user_name != sys_user_Name and your_password != sys_Password):
        print("your password and user name are wrong")
        entree-=1
    else:
        print("you entered successfully!")
        break
    if(entree==0):
        print("you've run out of access!")
        break
