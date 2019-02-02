##Caculate average
m=int(input("please input the total number of plants"))
num=[]
sum=0
i=0
str=input("please input each number of plants")
str1=str.split() #split int from string give it to str1
while i<m:
     num.append(float(str1.pop()))
     i=i+1;
j=0
while j< len(num):
    sum=sum+num[j]
    j=j+1
print("The average of this height is %.3f" %(sum/m))



##covert cases
str=input("please input a string")
print( str.swapcase())