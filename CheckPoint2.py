#!/usr/bin/env python
# coding: utf-8

# # Q1

# # Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# In[5]:


first_name = input()
last_name = input()
print(last_name+" "+first_name)


# # Q2

# # Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

# In[10]:


n=input("entre une valeur:",)
nn=n*2
nnn=n*3

sum = int(n) + int(nn) + int(nnn)

print(sum,"=",n,"+",nn,"+",nnn)


# # Q3

# # Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

# In[11]:


n= int(input("entre une valeur:"))
if n%2==0:
    print(n, "est pair")
else:
    print(n , "est impair")


# # Q4

# # Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a sequence on a single line.

# In[12]:


for i in range(2000,3201):
    if i%7==0 and i%5==0:
        print(i, end=",")


# # Q5

# # Write a program that can compute the factorial of a given number. The results should be printed in a sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320 

# In[14]:


n=int(input("entre un e valeur"))
if n==0 or n==1:
    print(1)
else:
    f=1
    for i in range(1,n+1):
        f=f*i
        print(f)


# # Q5 

# # Write a program to remove the characters which have odd index values of a given string.

# In[25]:


string= input("entre une chaine: ")
for i in range(0,len(string),2):
    print(string[i], end="")


# # #Q6

# # In this challenge, you must discount a price according to its value.
# 
# - If the price is 500 or above, there will be a 50% discount.
# 
# - If the price is between 200 and 500 (200 inclusive), there will be a 30% discount.
# 
# - If the price is less than 200, there will be a 10% discount.

# In[9]:


price= int(input('entrez un prix: '))
if price>=500:
    price=price*0.5
elif price>=200 and price<500:
    price=price*0.7
else:
    price=price*0.9
print('Discounted price: ', price)


# In[ ]:




