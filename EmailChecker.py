def emailChecking():
    email = input("Enter the Email : ")
    spacePresent = 0
    upperCasePresent = 0
    otherSpecialCharPresent = 0
    if len(email) >= 6:
        if email[0].isalpha():
            if("@" in email) and (email.count("@") == 1):
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if(i == i.isspace()):
                            spacePresent = 1
                            print("There should be no space in the email")
                        elif (i.isalpha()):
                            if i == i.upper():
                                upperCasePresent = 1
                                print(
                                    "There should be no capital letters in the email")
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            otherSpecialCharPresent = 1
                            print("Only _, . and @ special characters are allowed")
                    if spacePresent == 1 or upperCasePresent == 1 or otherSpecialCharPresent == 1:
                        pass
                    else:
                        print("Email is Valid")
                else:
                    print(
                        "root domain name is either not valid, or there is use of multiple .")
            else:
                print("Either @ is not present or is present multiple times")
        else:
            print("First character of Email can not be a number!")

    else:
        print("Please Enter a Valid Email")


emailChecking()
