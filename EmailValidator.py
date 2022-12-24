email = input("Enter Email ID: ")
space = upperAlpha = error = 0
# email length should be atleast of 6 character
if len(email) >= 6:

    #first letter of entered email should be alphabet
    if email[0].isalpha():

        # email should have '@' in it and its count will be one only
        if "@" in email and email.count("@") == 1:

            # '.' should be placed at correct postion
            if (email[-4] == ".") ^ (email[-3] == "."):

                #gmail must not contain any spaces,capital letters, special characters except '@','.','_'
                for i in email:
                    if i.isspace():
                        space = 1
                    elif i.isdigit():
                        continue
                    elif i.isalpha():
                        if i == i.upper():
                            upperAlpha = 1
                    elif i == "_" or i == "@" or i == ".":
                        continue
                    else:
                        error = 1
                if error == 1 or upperAlpha == 1 or space == 1:
                    print("Wrong email: Please follow the rules to enter a correct email address!")
                else:
                    print("Correct Email Address!")

            else:
                print("Wrong email: '.' should be placed at correct position")
        else:
            print("Wrong email: email must contain @ and it should be used once only")

    else:
        print("Wrong email: First letter of the email should be alphabet")

else:
    print("Wrong email: Length of email should contain atleast 6 character")