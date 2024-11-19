from Demos.win32ts_logoff_disconnected import username

print("""************

user login


************
""")
sys_user_name="can"
sys_password="12345"

user_name=input("please,enter the username...")
password=input("please,enter the password...")

if(user_name==sys_user_name and password!=sys_password):
    print("your password is wrong")
elif(user_name!=sys_user_name and password==sys_password):
    print("your username is wrong")
elif(user_name!=sys_user_name and password!=sys_password):
    print("both of them are wrong")
else:
    print("you succesfully entered the system.")
