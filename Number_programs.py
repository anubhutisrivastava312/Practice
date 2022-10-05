#program to reverse any given integer
# num=int(input("enter the number you want to reverse:"))
# reverse=0
# while num!=0:
#     reverse=num%10+reverse*10
#     num=num//10

# print("the number after reversing the original:",reverse)   



#program to check whether a number is armstrong number or not
# num=int(input("enter the num:"))
# sum=0
# temp=num
# order=len(str(num))
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**order
#     temp//=10

# if num==sum:
#     print(" armstrong")

# else:
#     print(" not armstrong")        


#program to print all the armstrong numbers in a specific range
# lower=int(input("enter the lower limit:"))
# upper=int(input(" enter the upper limit:"))
# num=int(input(" enter the number:"))
# for num in range(lower,upper+1):
#     order=len(str(num))
#     temp=num
#     sum=0
    
#     while temp>0:
#         digit=temp%10
#         sum=sum+digit**order
#         temp//=10
#     if num==sum:
#         print(num)    



#program to check whether a number is prime or not
# num=int(input(" enter the number:"))
# flag=0
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             flag=1
#     if flag==0:
#         print("prime number")

#     else:
#         print("not prime")         



#program to print the prime numbers in a given interval
# lower=int(input(" enter the lower limit:"))
# upper=int(input(" enter the upper limit:"))
# for num in range(lower,upper+1):
#     flag=0
#     for i in range(2,num):
#         if num%i==0:
#             flag=1
#             break
       
#     if flag==0:
        
#         print("the prime numbers are:",num)  




#program to print the fibonacii series using iterative method

# a=0
# b=1
# count=0
# terms=int(input("enter thr number of terms:"))
# if terms<0:
#     print("invalid term!")
# elif terms==1:
#     print(a)
# else:
#     while count<terms:
#         print(a)
#         c=a+b
#         a=b
#         b=c
#         count=count+1     




#program to print fibonacii series using recursive method(recursion)
# def fibonacii(n):
#     if n<=1:
#         return n
#     else:
#         result=fibonacii(n-1)+fibonacii(n-2)
#         return result    
# terms=int(input("enter the number of terms:"))
# if terms<0:
#     print("invalid term!")
# else:
#     for i in range(terms):
#         print(fibonacii(i))    



#program to print the palindrome number(example:101----->101)
# num=int(input("enter the number:"))
# reverse=0
# temp=num
# while temp>0:
#     reverse=temp%10+reverse*10
#     temp=temp//10

# if reverse==num:
#     print("palindrome")

# else:
#     print("not palindrome")    



#program to print the palindrome number using recursion
# reverse=0
# def palindrome(num):
#     global reverse
#     if num<=0:
#         return num
#     else:
#         reverse=num%10+reverse*10
#         palindrome(num//10)
#         return reverse    

# num=int(input(" enter the number:"))
# if palindrome(num)==num:
#     print("palindrome")
# else:
#     print("not palindrome")    



#program to check whether a number is binary or not
# num=int(input(" enter the number:"))
# while num>0:
#     i=num%10
#     if i!=0 and i!=1:
#         print(" the number is not binary")
#         break
#     num=num//10
#     if num==0:
#         print("the number is binary")


#program to print the sum of digits using iterative method
# num=int(input("enter the number:"))
# sum=0
# while num>0:
#     sum=num%10+sum
#     num=num//10
# print(" the sum is",sum)    


#program to print the sum of digits using recursion
# def recur_sum(num):
#     if num<=0:
#         return  num
#     else:
#         result=num%10+recur_sum(num//10) 
#         return result
# num=int(input(" enter the number:"))
# print(" the sum of digits is:",recur_sum(num))


#program to find  prime factors of a given integer
# def prime_factor(num):
#     c=2
#     while num>1:
#         if num%c==0:
#             print(c, end=" ")
#             num=num/c
# num=int(input(" enter the number:"))
# print(" the prime factors of a given number is:",prime_factor(num))        




#program to check whether a number is perfect number or not
# num=int(input("enter the number:"))
# sum=0
# for i in range(1,(num//2)+1):
#     remainder=num%i
#     if remainder==0:
#         sum=sum+i
# if sum==num:
#     print("perfect")
# else:
#     print(" not perfect")            




#program to find the average of numbers
# size_array=int(input(" enter the size of array:"))
# arr=[]
# for i in range(0,size_array):
#     element=int(input("value of "+str(i)+":"))
#     arr.append(element)

# avg=sum(arr)/size_array
# print("the average is:",avg)    


#program to calculate the factorial of a number using iterative method
# factorial=1
# num=int(input(" enter the number:"))
# if num<0:
#     print(" invalid term")
# elif num==1:
#     print(1)
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i

# print(" the factorial is:",factorial)    



#program to calculate the factorial of number using recursive method
# def factorial(num):
#     if num<=1:
#         return num
#     else:
#         result=num*factorial(num-1)
#         return result    

# num=int(input(" enter the number:"))
# print(" the factorial is:",factorial(num))        


#program to print the power of a number without using the pow function
# base=int(input(" enter the value for base:"))
# exponent=int(input(" enter the value for exponent:"))
# result=1
# while exponent!=0:
#     result=result*base
#     exponent=exponent-1
# print("the result is:",result)    




