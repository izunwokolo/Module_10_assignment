import sys
#import re
#Izu Nwokolo 
def encryption(key):
    message = input()
    message = message.upper()

    #counter for character and colums 
    counter = 0
    count_col =0
    message_array = list(message)

    for i in message_array:
      index = message_array.index(i)
      if message_array[index].isalpha() == True:
        if ord(message_array[index]) + key > ord("Z"):
          diff =ord(message_array[index]) + key - ord(message_array[index]) - 1
          print(chr(ord("A") + diff), end ="")
        else:
          print(chr(ord(message_array[index]) + key), end ="")
        counter += 1
      
      if counter == 5:
        print(" ", end="")
        counter = 0
        count_col += 1
      if count_col == 10:
        print("")
        count_col = 0
      
      
encryption(int(sys.argv[1]))
