Name=str(input("Enter Your Full name:"))
Email=str(input("Enter Your Email:"))
Mobile=(input("Enter Your Mobile:"))
Age=int(input("Enter Your Age:"))


if Name.count(" ")>=1:
    if Name[0]!=" ":
        if Name[len(Name)-1]!=" ":
            Name_valid=True
        else:
            Name_valid=False
    else:
        Name_valid=False
else :
    Name_valid=False

if '@' in Email :
    if '.' in Email :
        if Email[0]!='@' :
            Email_valid=True
        else :
            Email_valid=False
    else:
        Email_valid=False
else:
    Email_valid=False

if len(Mobile)==10:
    if Mobile.isdigit():
        if Mobile[0]!='0':
            Mobile_valid=True
        else :
            Mobile_valid=False

    else:
        Mobile_valid=False

else :
    Mobile_valid=False


if Age>=18 and Age<=60:
    Age_valid=True
else:
    Age_valid=False


if Name_valid==True and Email_valid==True and Mobile_valid==True and Age_valid==True :
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")