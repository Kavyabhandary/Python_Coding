def reverse(s):
   rev = ""
   for char in s :
       rev= char+rev
   print(rev)   
s= input("enter a string")
reverse(s)