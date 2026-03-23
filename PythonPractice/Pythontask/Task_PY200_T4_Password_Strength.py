# password as input
password=input("Enter the password:")

has_upper=False
has_lower=False
has_digit=False

if len(password)<8:
    print("WEAK")
else:
    # isupper() checks weather the character is in upper case or not
    # islower() checks weather the character is in lower case or not
    # isdigit() checks weather the character is digit or not

    for character in password:
        if character.isupper():
            has_upper=True
        elif character.islower():
            has_lower=True
        elif character.isdigit():
            has_digit=True
    
    #for strong password checking weather the stated condition fullfilled or not.
    if(has_upper and has_lower and has_digit):
        print("STRONG")
    else:
        print("WEAK")