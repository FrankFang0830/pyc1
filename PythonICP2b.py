
##stack
str=input("please input a stack")
str1=str.split()
print(str1)
ip=""
print('''1:output the top from the queue
2 :pop the element 
3 :pushing the element into queue
4 :quit''')
while(ip!='q'):
    ip=input("input an option")
    if(ip=="1"):
        print("the top of the stack is",str1[-1])
    elif(ip == "2"):   #catch unexpected
        try:
            print("we pop the element", str1.pop())
        except Exception as e:
            print(e)
    elif (ip == "3"):
        ip1=input("input a value")
        str1.append(ip1)
    elif (ip == "4"):
        print(str1)
    else :
        print("quit")
        break

##queue
qq=input("please input a queue")
qq1=qq.split()
print(qq1)
ip=""
print('''1:output the top from the queue
2 :pop the element 
3 :pushing the element into queue
4 :quit''')
while(ip!='q'):
    ip=input("please input an option")
    if(ip=="1"):
        print("the top of the queue is",qq1[-1])
    elif(ip == "2"):
        try:
            print("we pop the element", qq1.pop(0))
        except Exception as e:
            print(e)
    elif (ip == "3"):
        ip1=input("input a value")
        qq1.append(ip1)
    elif (ip == "4"):
        print(qq1)
    else :
        print("quit")
        break

