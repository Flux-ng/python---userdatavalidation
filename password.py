import random
import string

#User details
task_2 = "users' details Validation"
print(task_2.upper())

users = {}
while True:
    print("New User? Register here!")
    first_name = input("Enter First name: ")
    last_name = input("Enter Surname: ")
    e_mail = input("Enter a valid email: ")
    generated_password = ""
    password_input = ""

#genarated password for users combining the first two letters of their first and last name and random string.
    stringLength = 5
    lettersAndDigits = string.ascii_letters + string.digits
    rand = ""
    for i in range(stringLength):
        rand += random.choice(lettersAndDigits)
    generated_password += first_name[0:2] + last_name[-2:] + rand
    print("Suggested password: " + generated_password)

#password choice, for users to either accept the randomly generated password or create one manually.
    password_acceptance = input('Is the password good enough for you? yes/no: ').lower()
    if password_acceptance == 'yes':
        print("Congratulations! Registration completed.")
        print("Password saved as: " + generated_password)
    elif password_acceptance == 'no':

#This while/loop will allow only the password acceptance prompt to run until the condition
# is met and not the entire program.
        pw_input = True
        while pw_input:
            password_input = input("Enter new password: ")
            if len(password_input) < 7:
                print("Password must be 7 characters or more.")
            else:
                print("Congratulations! Registration completed.")
                print("Password saved as: " + password_input)

                break

#container where users' details are stored.
    def data():
        user = []
        for i in range(1):
            user.append(f"firstName:{first_name}")
            user.append(f"lastName:{last_name}")
            user.append(f"email:{e_mail}")
            user.append(f"suggestedPassword:{generated_password}")
            user.append(f"createdPassword:{password_input}")
            return user

    data()
    print(data())



#I think this program makes it easy to identify each users' detail as it collects and save per registration. the
#program is allowed to run to accommodate as many user as possible.




























