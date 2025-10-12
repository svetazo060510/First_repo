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
red = 255
green = 128
blue = 0

print(f"Before Swap: R={red}, G={green}, B={blue}")

# --- SINGLE LINE SOLUTION ---
# Python evaluates the right side (blue, red) first, forming a temporary tuple (0, 255).
# Then it unpacks that tuple into the variables on the left side (red, blue).
red, blue = blue, red

print(f"After Swap:  R={red}, G={green}, B={blue}")
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
sentence = "Python is powerful. Python is versatile."

# 1. Lowercase and Clean Punctuation
# We use .replace() to remove the period, then .lower()
cleaned_sentence = sentence.replace(".", "").lower()

# 2. Split into a List of Words
# The .split() method now works perfectly, producing:
# ['python', 'is', 'powerful', 'python', 'is', 'versatile']
word_list = cleaned_sentence.split()

# 3. Find Unique Words (Set)
# This is a one-line conversion as you correctly implemented
unique_words = set(word_list)

# 4. Count Word Frequency (Dictionary)
# We initialize an empty dictionary and iterate through the word list.
word_counts = {}
for word in word_list:
    # Use the dict.get() method (from Task 5!) to safely increment the count.
    # It gets the current count (defaulting to 0 if the word is new) and adds 1.
    word_counts[word] = word_counts.get(word, 0) + 1

print("--- Analysis Results ---")
print(f"Original Sentence: {sentence}")
print(f"1. Unique Words (Set): {unique_words}")
print(f"2. Word Frequencies (Dict): {word_counts}")
