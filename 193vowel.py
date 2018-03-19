vowel=["a","e","i","o","u"]
a=raw_input("Enter a Alphabet")
print a
for i in vowel:
    if a==i:
        print("Yes this is a vowel")
        break
    else:
        print("No this is not a vowel")
