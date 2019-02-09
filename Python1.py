print('I \"m Peihao Fang') # I'm Peihao Fang

first=input("please input your first name")
family=input("please input your family name")
print(first[::-1],family[::-1])

firstNum=int(input("please input 1st number"))
secondNum=int(input("please input 2nd number"))
print("The result by multiplication is",first*family)


stc=input("please input a senctence")
print(stc)
isAlpha=0
isDigtal=0
isIllegal=0
isSpace=0
for aWord in stc:       #Once take out one character from stc give it to variable:aWord
    if aWord.isdigit():
        isDigtal +=1
    elif aWord.isalnum():
        isAlpha +=1
    elif aWord.isspace():
        isSpace +=1
    else: isIllegal +=1
print ("This sentence contains %d's digtals" %isDigtal)
print ("This sentence contains %d's letters" %isAlpha)
print ("This sentence contains %d's spaces" %isSpace)