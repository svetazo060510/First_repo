# import string
# def count_words (text: str) -> dict:
#     lower_text = text.lower()
#     cleaned_text = lower_text.replace('.', '').replace(',', '').replace('?', '').replace('!', '')
#     words_list = cleaned_text.split()
#     word_counts = {}
#     for word in words_list:
#         if word in word_counts:
#             word_counts[word] += 1
#         else: 
#             word_counts[word] = 1

#     return word_counts

# def main():
#     user_input = input("Enter a word or phrase: ")
#     counts = count_words(user_input)

#     print("--- Word Counts ---")
#     for word, count in counts.items():
#         print(f"{word}: {count}")   
    
# if __name__ == "__main__":
#     main()
##############################
# word = input("Enter a word or phrase: ")

# clean_word = word.lower().replace(" ", "").replace(",", "").replace("?", "").replace(".", "")
# reversed_word = clean_word[::-1]
# #print (reversed_word)

# if clean_word == reversed_word:
#     print (f"{clean_word} is a palindrome!")
# else:
#     print (f"{clean_word} is not a palindrome!")
#2V
# import string
# def is_palindrome(text: str) -> bool:
#     cleaned_text = "".join(char for char in text.lower() if char.isalnum())
#     return cleaned_text == cleaned_text[::-1]

# def main():
#     user_input = input("Enter a word or phrase: ")
    
#     if is_palindrome(user_input):
#         print(f"'{user_input}' is a palindrome!")
#     else:
#         print(f"'{user_input}' is not a palindrome!")
        
# if __name__ == "__main__":
#     main()
###################################
# ingredients1 = input("Enter ingredients for the first recipe: ")
# ingredients2 = input("Enter ingredients for the second recipe: ")

# # separate with ','
# ingredients1_list = ingredients1.split()
# ingredients2_list = ingredients2.split()

# #create a set from list
# set1 = set(ingredients1_list)
# set2 = set(ingredients2_list)

# common = (set1.intersection(set2))
# if not common:
#     print ("These recipes have no common ingredients.")
# else: 
#     formatted_common = ', '.join(common)
#     print(f"Common ingredients: {formatted_common}")

##################################
# def add_contact(contact_info, contacts_list):
#     parts = contact_info.split(',')
#     if len(parts) != 3:
#         print("Error: Invalid format. Please use Name, Phone, Email.")
#         return False
#     else:
#         contact_dictionary = {
#             "name": parts[0].strip(),
#             "phone": parts[1].strip(),
#             "email": parts[2].strip()
#         }
#         contacts_list.append(contact_dictionary)
#         return True

# def search_contact(search_name, contacts_list):
#     for contact in contacts_list:
#         if contact['name'].lower() == search_name.lower():
#             return contact    
#     return None

# def main():
#     contacts = []
#     print("--- Add Contacts ---")
#     while True:
#         contact_info = input("Enter contact as 'Name, Phone, Email' (or 'done' to finish): ")
#         if contact_info.lower() == "done":
#             break
#         add_contact(contact_info, contacts)

#     if contacts:
#         print("\n--- Search for a Contact ---")
#         search_name_input = input("Enter a name to search for: ")        
#         found_contact = search_contact(search_name_input, contacts)
        
#         if found_contact:
#             print("\n--- Contact Found ---")
#             print(f"Name: {found_contact['name']}")
#             print(f"Phone: {found_contact['phone']}")
#             print(f"Email: {found_contact['email']}")
#         else:
#             print("Contact not found.")
#     else:
#         print("Your contact book is empty.")

# if __name__ == "__main__":
#     main()

####################################
# inventory = []

# while True:
#     item_name = input("Enter the item's name (or 'done' to finish): ")
#     if item_name.lower() == "done":
#         break
#     item_quantity = int(input(f"Enter the quantity for {item_name}: "))
#     item_price = float(input(f"Enter the price for {item_name}: "))

#     item_dictionary = {
#         "name": item_name,
#         "quantity": item_quantity,
#         "price": item_price
#     }
#     inventory.append(item_dictionary)

#     if not inventory:
#         print("\nNo items in inventory.")
#     else:
#         total_value = 0.0
#         highest_price = -1.0
#         most_expensive_item = ""
#         for item in inventory:
#             total_value += item['quantity'] * item['price']
#             if item ['price'] > highest_price:
#                 highest_price = item['price']
#                 most_expensive_item = item['name']
#         total_unique_items = len(inventory)
        

# print("\n--- Inventory Report ---")
# print(f"Total unique items: {total_unique_items}")
# print(f"Total inventory value: {total_value:.2f}")
# print(f"Most expensive item: {most_expensive_item}")
#####################################
# student_grades = {}

# name = ""
# grade = int()
# while True:
#     name = input("Enter student's name (or 'done' to finish): ")
#     if name == "done":
#         break
#     grade = int(input(f"Enter grade for {name}: "))
#     student_grades[name] = grade

# all_grades = student_grades.values()
# total_students = len(student_grades)
# av_grade = sum(all_grades) / total_students
# max_grade = max(all_grades)

# top_student = ""
# for name, grade in student_grades.items():
#     if grade == max_grade:
#             top_student = name
#             break

# print("\n--- Class Report ---")
# print(f"Total students: {total_students}")
# print(f"Average grade: {av_grade:.1f}")
# print(f"Highest grade: {max_grade}")
# print(f"Top student: {top_student}")
####################################
# code = input("Enter your code: ")

# if '@' in code and len(code) == 8 and code[0] == "U" and code[-1].isdigit():
#     print(f"Access granted. Your code is {code}") 
# else:
#     print(f"Access denied. Your code is {code}") 
###################################
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year!")
# else:
#     print(f"{year} is not a leap year!") 
###################################

# weight = float(input("What is your weight in kilograms?:"))
# height = float(input("What is your height in meters?:"))

# bmi = weight / (height**2)
# #rounded_bmi = round(bmi, 2)

# if bmi <= 18.5:   
#     print(f"Your BMI is {bmi:.2f}. You are underweight.")
# elif bmi >= 25.0:
#     print(f"Your BMI is {bmi:.2f}. You are overweight.")
# else:
#     print(f"Your BMI is {bmi:.2f}")

###################################

# bill_str = input("What was the total bill?: $")
# bill_tip = input ("What percentage of tip would you like to give?: %")
# bill_split = input ("How many people are splitting the bill?: ")

# bill_float = float(bill_str)
# bill_tip_float = float(bill_tip)
# bill_split_int = int(bill_split)

# amount = (bill_float / bill_split_int)
# tip = amount * bill_tip_float / 100

# print (f"You have to pay ${amount + tip:.2f}")

#################################################

# Task 1
# user_ids = [1001, 1005, 1002, 1005, 1003, 1001, 1004]

# # Step 1 & 3: Convert list to set (removes duplicates) and back to list.
# unique_user_ids = list(set(user_ids))

# # Step 2: Calculate the count of unique IDs.
# unique_count = len(unique_user_ids)

# # Verification Output
# print(f"Original IDs: {user_ids}")
# print(f"Unique IDs List: {unique_user_ids}")
# print(f"Unique Count: {unique_count}")

# Task 2
# student_records = {"Alice": 95, "Bob": 88, "Charlie": 76}

# def get_score(student_name, records):
#     """
#     Retrieves a student's score from the records.
#     Returns the score (int) if found, or a string message if not found.
#     """
#     # FIX 1: Call .get() on the dictionary object ('records').
#     # FIX 3: Use the second argument of .get() to set the default return value.
#     # This single line handles both found and not-found cases, and returns the result.
#     return records.get(student_name, "Student not found")

# # --- Testing the corrected function ---

# # Test Case 1: Student Found
# score_alice = get_score("Alice", student_records) 
# print(f"Alice's Score: {score_alice}")

# # Test Case 2: Student Not Found
# # FIX 2: Pass the correct dictionary object (student_records).
# score_david = get_score("David", student_records) 
# print(f"David's Score: {score_david}")

# Task 3
# filename = "profile_photo.jpg"

# # 1. Slice to remove the last 4 characters (".jpg")
# # 2. Slice again with [::-1] to reverse the resulting string
# # 3. Use .upper() to convert the final result
# processed_name = filename[:-4][::-1].upper()

# print(f"Original: {filename}")
# print(f"Processed: {processed_name}")

# # Verification of the expected result
# # Original without extension: "profile_photo"
# # Reversed: "otohp_eliforp"
# # Uppercase: "OTOHP_ELIFORP"

# Task 4
# points = [(1, 2), (3, 4), (0, 7)]

# # --- Part 1: Access the y-coordinate of the third point ---
# # The third point is at index 2 (0-based indexing).
# # The y-coordinate is the second element within that tuple, at index 1.
# third_y = points[2][1]
# print(f"1. Y-coordinate of the third point: {third_y}") # Output: 7

# # --- Part 2: Add a new point (5, 5) to the end of the list ---
# # The new point must be wrapped in a tuple () to be added as a single element.
# points.append((5, 5)) 
# print(f"2. List after adding point: {points}") 
# # Output: [(1, 2), (3, 4), (0, 7), (5, 5)]

# Task 5
# inventory = {"apples": 50, "bananas": 100, "oranges": 75}
# shipment = {"bananas": 120, "grapes": 30, "apples": 50}

# inventory.update((shipment))
# print (inventory)

#Task 6
# red = 255
# green = 128
# blue = 0

# print(f"Before Swap: R={red}, G={green}, B={blue}")

# # --- SINGLE LINE SOLUTION ---
# # Python evaluates the right side (blue, red) first, forming a temporary tuple (0, 255).
# # Then it unpacks that tuple into the variables on the left side (red, blue).
# red, blue = blue, red

# print(f"After Swap:  R={red}, G={green}, B={blue}")
# green remains 128 as it was not included in the swap operation.

# task 7
# sequence = ['A', 'B', 'C', 'D', 'E', 'F']
# # 1. Even Indices (Start at 0, Step by 2)
# # Indices: 0, 2, 4 
# even_indices = sequence[::2] 
# print(f"Elements at Even Indices: {even_indices}") 

# # 2. Odd Indices (Start at 1, Step by 2)
# # Indices: 1, 3, 5
# odd_indices = sequence[1::2]
# print(f"Elements at Odd Indices: {odd_indices}")

#task 8
# sentence = "Python is powerful. Python is versatile."

# # 1. Lowercase and Clean Punctuation
# # We use .replace() to remove the period, then .lower()
# cleaned_sentence = sentence.replace(".", "").lower()

# # 2. Split into a List of Words
# # The .split() method now works perfectly, producing:
# # ['python', 'is', 'powerful', 'python', 'is', 'versatile']
# word_list = cleaned_sentence.split()

# # 3. Find Unique Words (Set)
# # This is a one-line conversion as you correctly implemented
# unique_words = set(word_list)

# # 4. Count Word Frequency (Dictionary)
# # We initialize an empty dictionary and iterate through the word list.
# word_counts = {}
# for word in word_list:
#     # Use the dict.get() method (from Task 5!) to safely increment the count.
#     # It gets the current count (defaulting to 0 if the word is new) and adds 1.
#     word_counts[word] = word_counts.get(word, 0) + 1

# print("--- Analysis Results ---")
# print(f"Original Sentence: {sentence}")
# print(f"1. Unique Words (Set): {unique_words}")
# print(f"2. Word Frequencies (Dict): {word_counts}")
