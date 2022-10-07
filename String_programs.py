#program to remove a character in the given string
# def remove_char(str1,str2):
#     print(str1.replace(str2," "))

# str1=input("enter the string: ")
# str2=input(" enter the character which has to be removed from the string:")
# remove_char(str1,str2)    



#program to count the occurrence of acharacter in the given string
# string=input(" enter the string: ")
# character=input(" enter the character to be counted: ")
# count=0
# for i in range(len(string)):
#     if string[i]==character:
#         count=count+1
# print("the number is :", count)      




#program to check whether the given two strings are anagram or not
# def anagram(str1,str2):
#     if sorted(str1)==sorted(str2):
#         return True
#     else:
#         return False

# str1=input(" enter the string1: ")
# str2=input(" enter the string 2: ")   
# if anagram(str1,str2):
#     print("Anagram!")
# else:
#     print("not anagram!")             



#program to check whether the given string is palindrome or not
# string=input(" enter the string: ")
# if string==string[::-1]:
#     print(" palindrome!")
# else:
#     print(" not palindrome!")    



#program to check whether a given character is a vowel or consonent
character=input(" enter the character: ")
list1=['a','i','e','o','u','A','E','I','O','U']
if character in list1:
    print("vowel!")
else:
    print(" consonent!")    
