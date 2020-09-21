
import random

Name = input("What is your name? ") 
# Here the user is asked to enter the name first 

print("All the Best ! ", Name) 


f =input("Enter the name of the file: ")
if len(f)< 1:f="c"
with open("random.txt") as wordfile:   # with statement can handle closing the file automatically,random.txt is the name of the files
  words = wordfile.read().split()    #.read().split read words that are on separate lines from the file (.split() split the string into a list of strings)
random_word=random.choice(words)    #random.choice()  randomly select one word from the list


print("Guess the characters of the hidden word")
actual_char = ""  

count=10

while count>0:
  failed = 0   # count of no. of times the user fails

  for char in random_word:
    if char in actual_char:
      print(char)
    else:
      print("-")
      failed += 1
  if failed == 0:
    print(Name,"Won the game")
    print("The word is",random_word)    
    break

  actual = input("Enter the character: ")   
  actual_char+= actual  #every input character will be stored in actual_char

  if actual not in random_words:
    count -= 1
    print("Try Again!")
    print("You have ",count," left")  


    if count == 0:
      print(Name," you have lost the game!")
      print("The word was : ",random_word)
