#program to remove a character in the given string
# def remove_char(str1,str2):
#     print(str1.replace(str2," "))

# str1=input("enter the string: ")
# str2=input(" enter the character which has to be removed from the string:")
# remove_char(str1,str2)    



#program to count the occurrence of acharacter in the given string
string=input(" enter the string: ")
character=input(" enter the character to be counted: ")
count=0
for i in range(len(string)):
    if string[i]==character:
        count=count+1
print("the number is :", count)        