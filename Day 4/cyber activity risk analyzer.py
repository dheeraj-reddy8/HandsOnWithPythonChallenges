Registration_num=input("Enter Registration Number:")
led=int(Registration_num[len(Registration_num)-1])

print("Registration Number last Digit:",led)

m=int(input("Enter number  of scores :"))
score=[0]*m
print(score)
for i in range(m):
    score[i]=int(input("Enter Score:"))

print(score)

lowrisk=[]
mediumrisk=[]
highrisk=[]
criticalrisk=[]

valid=0
ignore=0
remove=0

for i in range(len(score)):
    main=score[i]

    if main<0:
        ignore=ignore+1
    else:
        valid=valid+1

        if  main>=0 and  main<=30:
             lowrisk=lowrisk+[main]

        elif  main>=31 and main<=60:
            mediumrisk=mediumrisk+[main]

        elif main>=61 and  main<=100:
            highrisk=highrisk+[main]

        else:
            criticalrisk=criticalrisk+[main]

print(" Before Personalizing:")
print("Low Risk:",lowrisk)
print("Median Risk:",mediumrisk)
print("High Risk:",highrisk)
print("Critical Risk:",criticalrisk)


print("Create a Finonacci list less than 9")
a=int(input("Enter first fibonacci number 0 or 1: "))
if a not in [0,1]:
    print("Invalid Input, changing first fibonacci number to 0")
    a=0

b=int(input("Enter second fibonacci number 0 or 1: "))
if b not in [0,1]:
    print("Invalid Input, changing second fibonacci number to 0 or 1")
    b=0

fibnum=[a,b]
number=int(input("Enter Fibonacci Number to generate less than 9:"))

for i in range(number-2):
    last=len(fibnum)-1
    slast=len(fibnum)-2
    next=fibnum[last]+fibnum[slast]

    if next<9:
        fibnum=fibnum+[next]

print("Your Fibonacci series:",fibnum)

user=[0]*len(fibnum)
print("Enter 0 or 1 to include each fibonacci number:")

for i in range(len(fibnum)):
    val= input("Include " + str(fibnum[i]) + "? (0/1): ")
    if val!="1":
        val="0"
    user[i]=int(val)


activefib=[0]*len(fibnum)
count=0
for i in range(len(fibnum)):
    if user[i]==1:
        activefib[i]=fibnum[i]
        count=count+1

final=[0]*count
for i in range(count):
    final[i]=activefib[i]

activefib=final
print("Your Active Fibonacci list:",activefib)


if led in activefib:
    remove = len(lowrisk)
    lowrisk = []
else:
    remove = len(criticalrisk)
    criticalrisk=[]


print(" After Personalizing:")
print("Low Risk:",lowrisk)
print("Median Risk:",mediumrisk)
print("High Risk:",highrisk)
print("Critical Risk:",criticalrisk)



print("Total Valid Entries:",valid)
print("Total Ignored Entries:",ignore)
print("Removed Entries after Personalization:",remove)



