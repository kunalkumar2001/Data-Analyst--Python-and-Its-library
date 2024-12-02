def func1():
  try:
    i = int(input("Enter the index: ")) 
    l = [1, 5, 6, 7]
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)
