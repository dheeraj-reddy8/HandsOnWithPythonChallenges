

Student_ID=input("ID:")
Email_ID=input("Email:")
Password=input("Password:")
Referral_Code=input("Refferral Code:")

Registration_Number= input("Registration Number:")
Number=int(Registration_Number[len(Registration_Number)-1])

if Number%2==0 :
    if len(Student_ID) == 7:
        if Student_ID[0] == "C":
            if Student_ID[1] == "S":
                if Student_ID[2] == "E":
                    if Student_ID[3] == "-":
                        if Student_ID[4] >= "0" and Student_ID[4] <= "9":
                            if Student_ID[5] >= "0" and Student_ID[5] <= "9":
                                if Student_ID[6] >= "0" and Student_ID[6] <= "9":
                                    Student_valid = True
                                else:
                                    Student_valid = False
                            else:
                                Student_valid = False
                        else:
                            Student_valid = False
                    else:
                        Student_valid = False
                else:
                    Student_valid = False
            else:
                Student_valid = False
        else:
            Student_valid = False
    else:
        Student_valid = False

    if len(Password)>=7:
        if Password[0]>="A" and Password[0]<="Z":
            if Password[0].isdigit() or Password[1].isdigit() or Password[2].isdigit() or Password[3].isdigit() or Password[4].isdigit() or Password[5].isdigit() or Password[6].isdigit() or Password[7].isdigit():
                Password_valids="True"
            else:
                Password_valids="False"
        else:
            Password_valids="False"
    else:
        Password_valids="False"

else:
    if len(Password)>=7:
        if Password[0]>="A" and Password[0]<="Z":
            if Password[0].isdigit() or Password[1].isdigit() or Password[2].isdigit() or Password[3].isdigit() or Password[4].isdigit() or Password[5].isdigit() or Password[6].isdigit() or Password[7].isdigit():
                Password_valids="True"
            else:
                Password_valids="False"
        else:
            Password_valids="False"
    else:
        Password_valids="False"

    if len(Student_ID) == 7:
        if Student_ID[0] == "C":
            if Student_ID[1] == "S":
                if Student_ID[2] == "E":
                    if Student_ID[3] == "-":
                        if Student_ID[4] >= "0" and Student_ID[4] <= "9":
                            if Student_ID[5] >= "0" and Student_ID[5] <= "9":
                                if Student_ID[6] >= "0" and Student_ID[6] <= "9":
                                    Student_valid = True
                                else:
                                    Student_valid = False
                            else:
                                Student_valid = False
                        else:
                            Student_valid = False
                    else:
                        Student_valid = False
                else:
                    Student_valid = False
            else:
                Student_valid = False
        else:
            Student_valid = False
    else:
        Student_valid = False

if "@" in Email_ID:
    if "." in Email_ID:
        if Email_ID[0]!="@":
            if Email_ID[len(Email_ID)-1]!="@":
                if Email_ID[len(Email_ID)-4]==".":
                    if Email_ID[len(Email_ID)-3]=="e":
                        if Email_ID[len(Email_ID)-2]=="d":
                            if Email_ID[len(Email_ID)-1]=="u":
                                Email_valid="True"
                            else:
                                Email_valid="False"
                        else:
                            Email_valid="False"
                    else:
                        Email_valid="False"
                else:
                    Email_valid="False"
            else:
                Email_valid="False"
        else:
            Email_valid="False"
    else:
        Email_valid="False"
else:
    Email_valid="False"


if len(Referral_Code)==6:
    if Referral_Code[0]=="R":
        if Referral_Code[1]=="E":
            if Referral_Code[2]=="F":
                if Referral_Code[3]>="0" and Referral_Code[3]<="9":
                    if Referral_Code[4]>="0" and Referral_Code[4]<="9":
                        if Referral_Code[len(Referral_Code)-1]=="@":
                            Referral_Code_valid="True"
                        else:
                            Referral_Code_valid="False"
                    else:
                        Referral_Code_valid="False"
                else:
                    Referral_Code_valid="False"
            else:
                Referral_Code_valid="False"
        else:
            Referral_Code_valid="False"
    else:
        Referral_Code_valid="False"
else:
    Referral_Code_valid="False"


if Student_valid and  Referral_Code_valid and Password_valids and Email_valid:
    print("APPROVED")
else:
    print("REJECTED")