Regno=(input("Enter your Registration Number :"))
ls=int(Regno[len(Regno)-1])

Name=(input("Enter your Name :"))
ln=len(Name)

ld=ls+ln


fib = [0] * 50


fib[0] = 0
fib[1] = 1


for i in range(2, 50):
    fib[i] = fib[i-1] + fib[i-2]
    if fib[i] > 50:
        break


if ld in fib:
    ld = 5
else:
    ld = 7

print("Number of Transactions to entered",ld)

transactions=[]
for i in  range(ld):

    ta=int(input("Enter Transaction Number Amount  :"))
    transactions=transactions+[ta]

categories={
    "normal":[],
    "large":[],
    "high_risk":[],
    "invalid":[]
}

for ta in transactions:
    if ta<=0:
        categories["invalid"]=categories["invalid"]+[ta]
    elif ta<=500:
        categories["normal"]=categories["normal"]+[ta]
    elif ta<=2000:
        categories["large"]=categories["large"]+[ta]
    else:
        categories["high_risk"]=categories["high_risk"]+[ta]

valid_transactions=[ta for ta  in transactions if ta>0]

total_value=0

for ta in valid_transactions:
    total_value=total_value+ta

summary=(total_value,len(transactions))

count=len(transactions)
if count>5:
    frequent=True
else:
    frequent=False

if total_value >5000:
    large_spending=True
else:
    large_spending=False


high_risk_count=0

for ta in categories["high_risk"]:
    high_risk_count=high_risk_count+1

if high_risk_count>=3:
    suspicious=True
else:
    suspicious=False

if suspicious:
    risk="High Risk"

elif frequent or large_spending:
    risk="Moderate Risk"

else:
    risk="Low Risk"

print("Transaction categories")
print("Normal:",categories["normal"])
print("Large:",categories["large"])
print("High Risk:",categories["high_risk"])
print("Invalid:",categories["invalid"])

print("Summary:",summary)
print("Total Transaction Value:",summary[0])
print("Number of Transactions:",summary[1])

print("Final Risk Level:",risk)



