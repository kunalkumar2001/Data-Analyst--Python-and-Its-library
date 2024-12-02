with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())
# with open('file.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)

#   # Save the current position
#   print(f.tell())
#   print(data)

#   # # Seek to the saved position
#   # f.seek(current_position)
#   # print(current_position)
