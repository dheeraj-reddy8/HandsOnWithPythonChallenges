requests=[]
m=int(input("Enter No.of.Requests:"))

for i in range(m):
    n=int(input("Enter the requests :"))
    requests=requests+[n]

print(requests)

lowdemand=[]
moderate=[]
highdemand=[]
invalidrequests=[]

countses=0
ignore=0
remove=0

for i in requests:
    if i<0:
        ignore=ignore+1
        invalidrequests=invalidrequests+[i]
    elif i==0:
        print("No demand reported value is :",i)
        countses = countses + 1
    elif i>=1 and i<=20:
        lowdemand = lowdemand + [i]
        countses=countses+1
    elif i>=21 and i<=50:
        moderate = moderate + [i]
        countses=countses+1
    else:
        highdemand = highdemand + [i]
        countses=countses+1

name = input("Enter Your Name :")
nospace = ""

for ch in name:
    if ch != " ":
        nospace = nospace + ch

l = 0
for ch in nospace:
    l = l + 1

print("Length of your name without spaces:", l)

pli=l%3
print("PLI Value:",pli)

print(" Before Personalizing:")
print("Low Demand:",lowdemand)
print("Moderate:",moderate)
print("High Demand:",highdemand)
print("Invalid Demand:",invalidrequests)

print("Personalization Begins:")

print("Create a Finonacci list less than 50")
a=int(input("Enter first fibonacci number 0 or 1: "))
if a not in [0,1]:
    print("Invalid Input, changing first fibonacci number to 0")
    a=0

b=int(input("Enter second fibonacci number 0 or 1: "))
if b not in [0,1]:
    print("Invalid Input, changing second fibonacci number to 0 or 1")
    b=0

fibnum=[a,b]
number=int(input("Enter Fibonacci Number to generate less than 50:"))

for i in range(number-2):
    last=len(fibnum)-1
    slast=len(fibnum)-2
    next=fibnum[last]+fibnum[slast]

    if next<50:
        fibnum=fibnum+[next]

print("Your Fibonacci series:",fibnum)

user=[0]*len(fibnum)
print("Enter 0 or 1 to include each fibonacci number")


activefib = []
for i in range(len(fibnum)):


    if fibnum[i] == pli:
        print("Including", fibnum[i], "automatically (matches PLI)")
        user[i] = 1
        activefib = activefib + [fibnum[i]]

    else:
        val = input("Include " + str(fibnum[i]) + "? (0/1): ")
        val = val.strip()

        if val != "1":
            val = "0"

        user[i] = int(val)

        if user[i] == 1:
            activefib = activefib + [fibnum[i]]

print("Your Active Fibonacci list:", activefib)




if pli in activefib:

    if pli == 0:
        remove = len(lowdemand)
        lowdemand = []

    elif pli == 1:
        remove = len(highdemand)
        highdemand = []

    elif pli == 2:
        print(moderate)
        remove=len(lowdemand)+len(highdemand)
        lowdemand = []
        highdemand = []


else:
    remove = 0

print(" After Personalizing:")
print("Low Demand:",lowdemand)
print("Moderate:",moderate)
print("High Demand:",highdemand)
print("Invalid Demand:",invalidrequests)




print("Total Valid Entries:",countses)
print("Total Ignored Entries:",ignore)
print("Removed Entries after Personalization:",remove)







