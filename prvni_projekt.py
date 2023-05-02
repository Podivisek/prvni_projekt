"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Hynková
email: ba.hynkova@gmail.com
"""

import re, sys
registered_users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

def summarize_text():

    # Login the user
    username = input("username: ")
    password = input("password: ")

    if username in registered_users:
        if password != registered_users[username]:
            print("Password doesnt match.")
            sys.exit(0)
        else:
            print(f"Welcome to the app, {username}")
            print("We have 3 texts to be analyzed.")

            user_choice = input("Enter a number btw. 1 and 3 to select: ")

            if user_choice == "1":
                text = TEXTS[0]
            elif user_choice == "2":
                text = TEXTS[1]
            elif user_choice == "3":
                text = TEXTS[2]
            else: 
                print("Invalid input. Program is terminating...")
                sys.exit(0)


            # Extract words in the text
            words = re.findall(r'\b\w+\b', text)

            # Extract words in the text
            words = re.findall(r'\b\w+\b', text)
            # Extract titlecase words in the text
            titlecase_words = [w for w in words if w.istitle()]
            # Extract uppercase words in the text
            uppercase_words = [w for w in words if w.isupper()]
            # Extract lowercase words in the text
            lowercase_words = [w for w in words if w.islower()]
            # Extract numeric strings in the text
            numeric_strings = re.findall(r'\b\d+\b', text)
            # Calculate the sum of all the numbers in the text
            sum_of_numbers = sum(map(int, numeric_strings))

            # Print the summary
            print(f"There are {len(words)} words in the selected text.")
            print(f"There are {len(titlecase_words)} titlecase words. ")
            print(f"There are {len(uppercase_words)} uppercase words. ")
            print(f"There are {len(lowercase_words)} lowercase words. ")
            print(f"There are {len(numeric_strings)} numeric strings.")
            print(f"The sum of all the numbers {sum_of_numbers}")
    else:
        print("No user found.")
        sys.exit(0)

# Example usage
summarize_text()
