import random
import string

def generate_password(length, lowercase=True, uppercase=True, digits=True, punctuation=True):
  """
  Generates a random password based on user-specified criteria.

  Args:
      length (int): Desired length of the password.
      lowercase (bool, optional): Include lowercase letters (default: True).
      uppercase (bool, optional): Include uppercase letters (default: True).
      digits (bool, optional): Include digits (default: True).
      punctuation (bool, optional): Include punctuation characters (default: True).

  Returns:
      str: The generated password.
  """

  char_sets = []
  if lowercase:
    char_sets.append(string.ascii_lowercase)
  if uppercase:
    char_sets.append(string.ascii_uppercase)
  if digits:
    char_sets.append(string.digits)
  if punctuation:
    char_sets.append(string.punctuation)

  # Combine all character sets into a single pool
  all_chars = ''.join(char_sets)

  # Use secrets module for secure random generation (recommended)
  password = ''.join(random.choices(all_chars, k=length))
  return password

def main():
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        print("Password length must be at least 8 characters.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Get user preference for complexity
  include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
  include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
  include_digits = input("Include digits (y/n)? ").lower() == 'y'
  include_punctuation = input("Include punctuation characters (y/n)? ").lower() == 'y'

  # Generate password based on user preferences
  password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_punctuation)

  # Display the generated password
  print(f"Your generated password is: {password}")

if __name__ == "__main__":
  main()
