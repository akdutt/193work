import sys
k= raw_input("Want to Find maximum b/w two no? Plz. press Y for yes and any key to abort ")
if (k=="y"):
    a=raw_input("Enter 1st no : ")
    b=raw_input("Enter 2nd no : ")
    if (a==b):
        print("No are eqal")
        sys.exit(0)
    if (a > b):
        print("1st no is greater than 2nd no")
    else:
        print("2nd no is greater than 1st no")
else:
    sys.exit(0)
