# import string
# k = string.ascii_uppercase
# print(k)
import random
import sys


salpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
balpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
basic_symbols = ['+', '-', '*', '/']
medium_symbols = ['@', '!', '#', '%']
advance_symbols = ['?', ':', ';', '&', '$', '_']


def password():
    user = str(input("""Enter The Type of Password You Want.
                1 - Basic (8 Characters) {"Only Alphabets & Numbers"}
                2 - Medium (12 Characters) {Alphabets, Numbers & Basic Symbols}
                3 - Advance (16 Characters) {Alphabets, Numbers & Medium Symbols}
                4 - Most Advance (18 Characters) {Alphabets, Numbers & Advance Symbols}
                
                ENTER THE SPECIFIC OPTION NUMBER BELOW FOR THE SPECIFIC SELECTING OPTION
                
                ENTER HERE :  """))
    
    sa1 = random.choice(salpha)
    ba1 = random.choice(balpha)

    sa2 = random.choice(nums)
    ba2 = random.choice(salpha)

    sa3 = random.choice(balpha)
    ba3 = random.choice(nums)

    sa4 = random.choice(salpha)
    ba4 = random.choice(balpha)

    print("\n")

    if "q" in user:
        sys.exit()

    elif "1" in user:
        print("A Ramdom Password For You Is Below")
        print("\n")

        print(sa1+ba1+sa2+ba2+sa3+ba3+sa4+ba4)
        print("\n")

    elif "2" in user:
        print("A Ramdom Password For You Is Below")
        print("\n")

        bsymbol1 = random.choice(basic_symbols)
        bsymbol2 = random.choice(basic_symbols)
        bsymbol3 = random.choice(basic_symbols)

        print(sa1+ba3+bsymbol1+sa4+ba2+ba1+bsymbol3+sa1+bsymbol2+ba4+sa2+ba3)
        print("\n")

    elif "3" in user:
        print("A Ramdom Password For You Is Below")
        print("\n")

        msymbol1 = random.choice(medium_symbols)
        msymbol2 = random.choice(medium_symbols)
        msymbol3 = random.choice(medium_symbols)
        msymbol4 = random.choice(medium_symbols)

        print(msymbol1+sa4+ba3+msymbol3+ba1+sa2+ba4+sa1+msymbol2+sa1+msymbol4+ba3+sa4+sa3+ba1+sa4+sa1+ba3)
        print("\n")

    elif "4" in user:
        print("A Ramdom Password For You Is Below")
        print("\n")

        asymbol1 = random.choice(advance_symbols)
        asymbol2 = random.choice(advance_symbols)
        asymbol3 = random.choice(advance_symbols)
        asymbol4 = random.choice(advance_symbols)
        asymbol5 = random.choice(advance_symbols)

        print(asymbol1+sa2+ba3+asymbol3+ba4+sa1+ba3+sa1+asymbol2+sa1+asymbol5+ba3+sa4+sa3+ba1+sa4+sa1+ba3+sa2+asymbol1)
        print("\n")

    else:
        print("You Pressed the wrong key. Try again")
        print("\n")

password()