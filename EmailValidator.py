email = input("Enter Email ID: ")

# email length should be atleast of 6 character
if len(email) >= 6:

    #first letter of entered email should be alphabet
    if email[0].isalpha():

        # email should have '@' in it and its count will be one only
        if "@" in email and email.count("@") == 1:

            # '.' should be placed at correct postion
            if email[-4] == "." ^ email[-3] == ".":

                #gmail does not contain any spaces in it
                if " " not in email:
                    pass

                else:
                    print("Wrong mail: There should not be any spaces in email address")

            else:
                print("Wrong mail: '.' should be placed at correct position")
        else:
            print("Wrong email: email must contain @ and it should be used once only")

    else:
        print("Wrong email: First letter of the email should be alphabet")

else:
    print("Wrong email: Length of email should contain atleast 6 character")