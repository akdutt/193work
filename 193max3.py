import sys
k= raw_input("Want to Find maximum b/w three no? Plz. press Y for yes and any key to abort ")
if (k=="y"):
    a=raw_input("Enter 1st no : ")
    b=raw_input("Enter 2nd no : ")
    c=raw_input("Enter 3rd no : ")
    if (a==b and b==c):
        print("No are eqal")
        sys.exit(0)
    elif (a>b and a>c):
        print("1st no is greater than 2nd & 3rd no")
    elif(b>a and b>c):
        print("2nd no is greater than 1st & 3rd no")
    else:
        print("3rd no is greater than 1st & 2nd no")
else:
    sys.exit(0)
