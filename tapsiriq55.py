a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])









n=int(input("Enter number: "))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are :",count)









start=int(input("Enter the start of the range: "))
end=int(input("Enter the end of the range: "))

list_all=[]
for i in range(start,end+1):
    if (i%5==0) and (i%7!=0):
        list_all.append(str(i))

print("Result:")
print(",".join(list_all))

