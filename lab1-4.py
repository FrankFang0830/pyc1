def solution(s):

    maxstring = ""
    string = ""
# find the current string:

    for letter in s:

        if letter not in string:
            string += letter

        else:
            if len(string) > len(maxstring):  # compare the length of current string and maxstring
                maxstring = string
            string = letter
    return maxstring


str = input("Input a string")
s = solution(str)
print("output: ", s, len(s))