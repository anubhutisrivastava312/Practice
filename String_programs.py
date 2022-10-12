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
# character=input(" enter the character: ")
# list1=['a','i','e','o','u','A','E','I','O','U']
# if character in list1:
#     print("vowel!")
# else:
#     print(" consonent!")    


#program to check whether a character is digit or not
# ch=input("enter the character: ")
# list1=['0','1','2','3','4','5','6','7','8','9']
# if ch in list1:
#     print("charcater is digit ")
# else:
#     print("character is not digit")   


#program to check whether a charcter is digit or not by using isdigit() method
# ch= input("enter the character:")
# if ch.isdigit():
#     print("char is digit") 
# else:
#     print(" char is not digit")      




#program to replace the space from a given string and replace it with a character
# def remove_space(str1,str2):
#     print(str1.replace(' ',str2))
# str1=input(" enter the string: ") 
# str2=input(" enter the character with which you want to replace the space: ") 
# remove_space(str1,str2)
  
#program to replace all the vowels in the given string with a *
# str=input("enter the string: ")
# ch='*'
# result=''
# list1=['a','e','i','o','u','A','E','O','U','I']
# for i in str:
#     if i in list1:
#         i=ch
#     result=result+i
# print(" the new string: ",result) 





#program to convert all the lowercase characters in a given string to uppercase characters
# str=input(" enter the string: ")
# result=''
# for i in str:
#     if i.islower():
#         i=i.upper()#upper function to convert all the lowercase chars to uppercase
#     result=result+i    
# print(" the new string is: ",result)    


#program to convert all the uppercase characters in a given string to lowercase
# str=input(" enter the string: ")
# result=''
# for i in str:
#     if i.isupper():
#         i=i.lower()
#     result=result+i
# print("the new string is: ",result)        



#program to delete the vowels from a given string
# str=input(" enter the string: ")
# list1=['a','e','i','o','u','A','E','I','O','U']
# result=''
# for i in str:
#     if i in list1:
#         i=''
#     result=result+i 
# print(" the new string: ",result)       

#program to print the highest frequency character in string
# from collections import Counter

# str=input(" ener the string: ")
# result=Counter(str)
# result=max(result, key=result.get)
# print(" the maximum occuring character is: ",result)



#program to count the number of alphabets,digits and special characters



# str=input(" enter a string: ")
# alphabets=0
# digits=0
# consonents=0
# spc_char=0
# for i in str:
#     if i.isalpha():
#         alphabets=alphabets+1
#     elif i.isdigit():
#         digits=digits+1    
#     else:
#         spc_char=spc_char+1

# print(" the number of alphabets is:",alphabets,", digits:",digits," , special characters is: ",spc_char)



#program to remove blank space from string
# string=input(" enter the string: ")
# result=''
# for i in string:
#     if i!=' ':
#      result=result+i

# print(" the new string: ",result)



#program to remove repeated characters or duplicate characters from string
# string=input(" enter the string: ")
# result=''
# for i in string:
#     if i not in result:
#         result=result+i
# print(" the new string is : ",result)        


#program to sort a string lexicographically or sort alphabetically the words given in a string.
# str=input("enter a string: ")
# words=[i.lower() for i in str.split()]
# words.sort()
# for i in words:
#     print(i)