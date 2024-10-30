def rev(s):
    last= s[-1:]
    new_str= s[:-1][::-1]+last
    print(new_str)
s=input("enter a string")
rev(s)