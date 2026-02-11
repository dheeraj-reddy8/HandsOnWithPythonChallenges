reg=input("Enter your registration number:")
name=input("Enter your name:")

length=len(name)
num2=int(reg[len(reg)-2])
num1=int(reg[len(reg)-1])
last=num2*10+num1*1
cal=length+last


n=int(input("Enter No.of.Students:"))

marks=[0]*n
for i in range(n):
    marks[i]=int(input("Enter Marks:"))

print(marks)

valid=0
fail=0
bonus=0

for i in range(n):
    mark=marks[i]

    if (cal!=0 and mark % cal==0) or (mark!=0 and cal%mark==0):
        bonus=bonus+1


for i in range(n):
    mark=marks[i]

    if mark>=0 and mark<=100:
        origin=mark
        if bonus>0:
            if mark<=95:
                mark = mark + 5
                print("5 Marks were added to",origin,"New Marks are:",mark )

            else:

                mark=100
                print(origin, " Bonus adjusted to mark:", mark)
        else:
            if mark<=99:
                print("No Bonous applied: ")
                mark=mark+0
            else:
                print("No Bonous applied , but mark updated to: ")
                mark=100

        if mark <0 or mark>100:
            print(mark,"-> Invalid")

        elif mark>=90 and mark<=100:
            valid=valid+1
            print(mark,"-> Excellent")

        elif mark>=75 and mark<=89:
            valid=valid+1
            print(mark,"-> Very Good")

        elif mark>=60 and mark<=74:
            valid=valid+1
            print(mark,"-> Good")
        elif mark>=40 and mark<=59:
            valid=valid+1
            print(mark,"-> Average")
        elif mark>=0 and mark<=39:
            valid=valid+1
            fail=fail+1
            print(mark,"-> Fail")
        else :
            print(mark,"-> Invalid")


print("Total Valid Students:",valid)
print("Total Failed Students:",fail)