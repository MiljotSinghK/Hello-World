=int(input("Enter a number: "))
arm=n
compare_value=n
count=0
sum=0
while n>0:
 n//=10
 count+=1
while arm>0:
    a=arm%10
    sum=sum+a**count
    arm//=10
if sum==compare_value:
   print(f"the number {compare_value} is an Armstrong Number")
else:
   print(f"{compare_value} is not an armstrong  number")
