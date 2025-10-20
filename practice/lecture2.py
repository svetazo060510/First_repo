# task 1
# num_input = input("Enter a number: ")
# try:
#     num = int(num_input)

#     # 1. Check most specific case first: divisible by BOTH 3 and 5
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")

#     # 2. Check general case: divisible by 3 (this only runs if #1 was False)
#     elif num % 3 == 0:
#         print("Fizz")

#     # 3. Check general case: divisible by 5 (this only runs if #1 and #2 were False)
#     elif num % 5 == 0:
#         print("Buzz")

#     # 4. Catch-all: runs if NONE of the above conditions were met
#     else:
#         print(num)

# except ValueError:
#     print("Invalid input. Please enter a whole number.")


# task 2
# def is_valid_password(password):
#     """
#     Checks if a password meets the required criteria using a single boolean expression.
#     Criteria:
#     1. Length is between 8 and 15 (inclusive).
#     2. Does not contain "password" (case-insensitive).
#     """

#     # --- Criterion 1: Length check ---
#     is_correct_length = len(password) >= 8 and len(password) <= 15
#     # Python allows chaining comparisons, which is even cleaner:
#     # is_correct_length = 8 <= len(password) <= 15 

#     # --- Criterion 2: Content check (case-insensitive) ---
#     is_safe_content = not ("password" in password.lower())

#     # Single conditional statement: both primary conditions must be True
#     if is_correct_length and is_safe_content:
#         return True
#     else:
#         # A more concise way to write this is 'return is_correct_length and is_safe_content'
#         return False

# # Test Cases
# test_cases = [
#     "myPass123",            # Valid (Length 9, OK content)
#     "too_short",            # Invalid length (7)
#     "SecurePassword12345",  # Invalid length (21)
#     "MyPASSWORD123",        # Invalid content (contains 'password')
#     "123456789012345",      # Valid (Length 15, OK content)
# ]

# print("--- Password Validation Results ---")
# for p in test_cases:
#     result = is_valid_password(p)
#     print(f"'{p}': {result}")

# task 3
