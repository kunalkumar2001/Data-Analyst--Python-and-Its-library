# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random


def encode(word):
  if len(word) >= 3:
    new_word = word[1:] + word[
      0]  # Remove the first letter and append it at the end
    new_word = ''.join(random.choices(
      'abcdefghijklmnopqrstuvwxyz', k=3)) + new_word + ''.join(
        random.choices(
          'abcdefghijklmnopqrstuvwxyz',
          k=3))  # Append three random characters at the start and end
  else:
    new_word = word[::-1]  # Reverse the string
  return new_word


def decode(word):
  if len(word) < 3:
    decoded_word = word[::-1]  # Reverse the word
  else:
    decoded_word = word[3:-3]  # Remove 3 random characters from start and end
    decoded_word = decoded_word[
      -1] + decoded_word[:
                         -1]  # Remove the last letter and append it to the beginning
  return decoded_word


action = input("Do you want to code (C) or decode (D) a message? ").upper()

if action == 'C':
  message = input("Enter the message to encode: ")
  encoded_message = ' '.join(encode(word) for word in message.split())
  print("Encoded message:", encoded_message)
elif action == 'D':
  message = input("Enter the message to decode: ")
  decoded_message = ' '.join(decode(word) for word in message.split())
  print("Decoded message:", decoded_message)
else:
  print(
    "Invalid action. Please choose 'C' to code or 'D' to decode a message.")
